Barbarik AI Chatbot
A smart chatbot designed to interact with customer data using a user-friendly interface. It combines secure data storage in MongoDB with AI-powered natural language processing through Google APIs.

Features
Secure Data Storage: MongoDB is used to store datasets efficiently.
Google APIs Integration: Utilizes Google API as the Large Language Model (LLM) for natural language understanding.
Customer Data Analysis: Query customer information dynamically (e.g., products purchased).
Interactive Interface: Built with Streamlit for a seamless user experience.

Steps to Run the Project
Step 1: Run data_upload.py
Purpose: Upload datasets to MongoDB for customer data storage.
Process:
Connect to MongoDB using pymongo and upload the dataset.
Datasets must be structured appropriately (e.g., customer details, purchase history).
The script validates the database connection and ensures the data is successfully uploaded.
Technologies Used:
pymongo: For MongoDB integration.
os: For file handling and constructing dataset paths.
Goal: Prepare the database for the chatbot’s queries.


Here’s how your Barbarik AI Chatbot project description can be restructured in a similar format to the ZENO.V example, with clear steps and concise explanations:

Barbarik AI Chatbot
A smart chatbot designed to interact with customer data using a user-friendly interface. It combines secure data storage in MongoDB with AI-powered natural language processing through Google APIs.

Features
Secure Data Storage: MongoDB is used to store datasets efficiently.
Google APIs Integration: Utilizes Google API as the Large Language Model (LLM) for natural language understanding.
Customer Data Analysis: Query customer information dynamically (e.g., products purchased).
Interactive Interface: Built with Streamlit for a seamless user experience.
Steps to Run the Project
Step 1: Run data_upload.py
Purpose: Upload datasets to MongoDB for customer data storage.
Process:
Connect to MongoDB using pymongo and upload the dataset.
Datasets must be structured appropriately (e.g., customer details, purchase history).
The script validates the database connection and ensures the data is successfully uploaded.
Technologies Used:
pymongo: For MongoDB integration.
os: For file handling and constructing dataset paths.
Goal: Prepare the database for the chatbot’s queries.

Step 2: Run config_google_api.py
Purpose: Configure Google API credentials for LLM integration.
Process:
Obtain API credentials from Google Cloud Console.
Enable required APIs for natural language processing.
Save the credentials securely and update the configuration file (config.py) with the API key.
Technologies Used:
Google Cloud APIs for natural language processing and context-aware responses.
Goal: Set up the foundation for AI-driven interactions.

Step 3: Run streamlit_app.py
Purpose: Launch the chatbot’s interactive interface.
Process:
The Streamlit-based UI lets users input queries.
The chatbot verifies user inputs, queries MongoDB for data, and provides intelligent responses.
Example Queries:
"List all the products purchased by Customer X."
"What is the most popular product category?"
Technologies Used:
Streamlit: For the web-based interface.
pymongo: For database queries.
