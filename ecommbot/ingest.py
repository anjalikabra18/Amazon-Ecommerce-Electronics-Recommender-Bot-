from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
from langchain_core.documents import Document

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def ingestdata(status):
    """
    Ingest the dataset into the vector store.
    """
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name="amazonecom",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )

    if status is None:
        # Load and process the dataset
        file_path = "C:\\Users\\anjal\\OneDrive\\Desktop\\Github\\Amazon_Ecommerce_bot\\data\\Simulated_Product_Data.csv"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        product_data = pd.read_csv(file_path)

        # Create documents
        docs = []
        for _, row in product_data.iterrows():
            metadata = {
                "product_name": row["Title"],
                "price": row["Price"],
                "category": row["Category"],
                "ratings": row["Ratings (out of 5)"],
                "recommended": row["Recommended"],
                "product_link": row["Product Link"],
            }
            content = f"Description: {row['Product Description']}\nReview: {row['Customer Reviews']}"
            doc = Document(page_content=content, metadata=metadata)
            docs.append(doc)

        # Add documents to vector store
        print("Ingesting data into AstraDB...")
        inserted_ids = vstore.add_documents(docs)
        print(f"Ingested {len(inserted_ids)} documents into the vector store.")
        return vstore, inserted_ids
    else:
        return vstore

if __name__ == "__main__":
    vstore, inserted_ids = ingestdata(None)
    print(f"Successfully ingested {len(inserted_ids)} documents.")
