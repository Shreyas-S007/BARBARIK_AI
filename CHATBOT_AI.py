import streamlit as st
import google.generativeai as genai
from pymongo import MongoClient
import os
from datetime import datetime

# Configure API keys and connections
GOOGLE_API_KEY = <add your API_KEY>
MONGODB_URI = "mongodb://localhost:27017/"

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# MongoDB connection
client = MongoClient(MONGODB_URI)
db = client['BARBARIK']
collection_name = 'CUSTOMERS_DETAILS'
collection = db[collection_name]

# Configure Streamlit page
st.set_page_config(
    page_title="BARBARIK_AI CHATBOT",
    page_icon="🤖",
    layout="wide"
)


def fetch_data():
    """Fetch all data from the collection."""
    documents = list(collection.find())
    if not documents:
        return None
    # Build context with clear field descriptions
    context = f"=== Data from {collection_name} ===\n"
    for doc in documents:
        context += "\nRecord:\n"
        for key, value in doc.items():
            if key != '_id':
                context += f"{key}: {value}\n"
    return context


def get_gemini_response(question, context):
    """Get response from Gemini API based on the context."""
    # Provide a detailed and explicit prompt
    prompt = f"""You are an intelligent assistant helping answer questions about customer data. 
    Use the data provided below to answer the question accurately. If the data does not contain the answer, 
    respond with: "I cannot find the answer in the provided data."

    Data:
    {context}

    Question: {question}
    """
    response = model.generate_content(prompt)

    # Extract and return the response content
    if response and response.candidates:
        return ''.join(part.text for part in response.candidates[0].content.parts)
    else:
        return "No valid response from the Gemini API."


def initialize_session_state():
    """Initialize session state variables."""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []


def main():
    initialize_session_state()

    # Main UI
    st.title("🤖 BARBARIK_AI CHATBOT")
    st.write("Ask questions about your customer data!")

    # Display the data
    st.markdown("### Data Preview:")
    data_context = fetch_data()
    if data_context:
        with st.expander("Show All Data"):
            st.text(data_context)
    else:
        st.error(f"No data found in the collection `{collection_name}`.")
        return

    # Chat UI
    st.markdown("### Chat History:")
    if st.session_state.chat_history:
        for entry in st.session_state.chat_history:
            st.markdown(f"**You:** {entry['question']}")
            st.markdown(f"**Gemini:** {entry['answer']}")

    # Query input
    question = st.text_input("Enter your question:")

    if st.button("Send"):
        with st.spinner("Fetching answer..."):
            if not data_context:
                st.error(f"No data found in the collection `{collection_name}`.")
                return

            # Get response from Gemini
            answer = get_gemini_response(question, data_context)

            # Update chat history
            st.session_state.chat_history.append({"question": question, "answer": answer})

            # Display latest response
            st.markdown("### Latest Response:")
            st.markdown(f"**Gemini:** {answer}")

            # Log the interaction
            log_collection = db.get_collection('query_logs')
            if log_collection is not None:
                log_collection.insert_one({
                    "timestamp": datetime.now(),
                    "question": question,
                    "answer": answer,
                    "collection_used": collection_name,
                    "context_used": data_context
                })

    # Usage instructions
    with st.expander("How to use"):
        st.markdown("""
        1. Enter your question in the text input field.
        2. Click 'Send' to receive a response.
        3. The chat history will display your previous questions and Gemini's answers.
        4. Expand "Show All Data" to view the data being used for the response.
        """)


if __name__ == "__main__":
    main()
