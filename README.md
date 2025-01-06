# Amazon Electronics Recommender Bot 🔍

The **Amazon Electronics Recommender Bot** is a next-generation AI-powered chatbot that enhances the shopping experience by providing real-time product recommendations based on user queries. The chatbot leverages natural language processing (NLP) techniques to understand user queries and generate appropriate responses. The chatbot integrates with the e-commerce store's product database to provide personalized recommendations and information about available products. By leveraging advanced AI technologies, this bot supports multimodal inputs such as text and voice to offer personalized product insights.

---
![image](https://github.com/user-attachments/assets/2b9d3a34-1a95-47b8-b3a9-9f75f9c787a6)


## Features 🚀

### Analyze & Recommend

- Upload text, voice, or image inputs to receive product recommendations.
- Combines multimodal inputs for better user interaction.

### Real-Time Web Scraping from Amazon

- Scrapes product data in real-time from Amazon, including titles, descriptions, prices, and ratings.
- Ensures that the bot provides up-to-date product information.

### Semantic Search & Embeddings

- Uses OpenAI embeddings to convert product descriptions and queries into vector representations.
- Enables semantic search, allowing the bot to understand and respond to user queries based on meaning rather than exact keyword matches.

### Product Information Retrieval

- Access detailed product descriptions, reviews, and ratings using AstraDB Vector Store.
- Provides personalized shopping assistance based on user needs.

### Multimodal Processing

- **Text Input:** Processed by OpenAI's language model.
- **Voice Input:** Converted to text using Whisper AI.
-

---

## Technologies Used 🧰

- **Frontend:** HTML, CSS, JavaScript (jQuery)
- **Backend:** Flask (Python)
- **AI Models:** OpenAI, Whisper
- **Vector Store:** AstraDB VectorStore
- **Web Scraping:** BeautifulSoup, Requests
- **Multimodal Tools:** gTTS, Pandas, LangChain

---

## How It Works 📚

1. **User Input (Text/Voice/Image):**
   - Users provide input through an interactive interface.
2. **Frontend (HTML/CSS/JS):**
   - The input is captured through a web-based user interface.
3. **Backend (Flask App):**
   - The Flask application processes requests and manages AI model interactions.
4. **Web Scraping:**
   - The bot scrapes Amazon's website in real-time to retrieve product information.
5. **Multimodal Processing:**
   - Handles text, voice inputs to ensure robust interaction.
6. **Semantic Search with Embeddings:**
   - Converts user queries and product data into embeddings using OpenAI models.
   - Allows the bot to understand user intent and provide more relevant responses.
7. **AI Model (OpenAI):**
   - Processes queries to provide intelligent responses.
8. **Vector Store (AstraDB):**
   - Stores and retrieves product data for faster responses.
9. **Response to User:**
   - The bot returns a response in text or audio format, providing product links, descriptions, and recommendations.

---

![image](https://github.com/user-attachments/assets/9988a276-c70b-48af-8fdd-04c329de192f)


## Installation 💻

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anjalikabra/AmazonElectronicsBot.git
   cd AmazonElectronicsBot
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables:**
   Create a `.env` file with the following keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ASTRA_DB_API_ENDPOINT=your_astra_db_endpoint
   ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
   ASTRA_DB_KEYSPACE=your_astra_db_keyspace
   ```
5. **Run the Flask App:**
   ```bash
   python app.py
   ```

---


## Usage ✨

1. **Launch the Application:**
   ```bash
   python app.py
   ```
2. **Interact with the Bot:**
   - Open your browser and go to `http://localhost:5000`.
   - Type queries or record audio for personalized recommendations.

---

## Workflow Flowchart 📊

**User Input ➡️ Frontend (HTML/CSS/JS) ➡️ Flask Backend ➡️ Web Scraping ➡️ Multimodal Processing ➡️ Semantic Search & Embeddings ➡️ AI Model (OpenAI) ➡️ Vector Store (AstraDB) ➡️ Response to User**




## Contributing 🤝

We welcome contributions! Follow the steps below:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** and submit a pull request.

---

## License 📜

This project is licensed under the MIT License.

---

## Contact 📧

**Anjali Kabra**\
GitHub: [Anjali Kabra](https://github.com/anjalikabra)

