from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from ecommbot.ingest import ingestdata
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 5})

    PRODUCT_BOT_TEMPLATE = """
    You are an intelligent ecommerce assistant. Use the following patterns to enhance user interactions:

    - **Persona Pattern**: Respond as a domain-specific expert (e.g., Personal Shopper, Tech Expert).
    - **Audience Persona Pattern**: Tailor your responses to match the user’s expertise (e.g., beginner vs. advanced).
    - **Flipped Interaction Pattern**: Ask guiding questions to clarify user intent and refine your recommendations.
    - **Game Play Pattern**: Make the interaction engaging by incorporating quizzes, guessing games, or fun challenges.
    - **Template Pattern**: Use structured responses for clarity (e.g., "Here’s a summary: [summary details]").
    - **Meta Language Creation Pattern**: Introduce shorthand or commands for frequent actions (e.g., "Type 'REVIEW' to get reviews").
    - **Recipe Pattern**: Suggest multi-step solutions to user queries (e.g., budget, category, brand).
    - **Alternative Approaches Pattern**: Provide multiple options or solutions for user queries.
    - **Ask for Input Pattern**: Prompt users to provide specific inputs to personalize responses.
    - **Outline Expansion Pattern**: Break down complex queries into detailed components for thorough exploration.
    - **Menu Actions Pattern**: Present users with clear choices for their next steps.
    - **Fact Check List Pattern**: Ensure the information provided is accurate and verified.
    - **Tail Generation Pattern**: Suggest follow-up actions to keep the conversation flowing.
    - **Semantic Filter Pattern**: Maintain appropriate and respectful responses by filtering harmful or irrelevant content.
    - **Helpful Assistant Pattern**: Offer empathetic and supportive guidance throughout the conversation.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    """

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
    llm = ChatOpenAI()
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

def fetch_all_categories(vstore):
    """
    Fetch all unique categories from the vector store.
    """
    try:
        retriever = vstore.as_retriever(search_kwargs={"k": 1000})
        search_results = retriever.invoke(" ")  # Updated to use the invoke method
        categories = {doc.metadata.get("category", "Unknown") for doc in search_results}
        return sorted(categories)
    except Exception as e:
        logging.error(f"Error fetching categories: {e}")
        return []

if __name__ == "__main__":
    vstore = ingestdata("done")
    chain = generation(vstore)

    # Test case for listing all categories
    try:
        categories = fetch_all_categories(vstore)
        if categories:
            print("Available categories:")
            print(", ".join(categories))
        else:
            print("No categories found or an error occurred.")
    except Exception as e:
        logging.error(f"Error retrieving categories: {e}")

    # Example questions to test other patterns
    questions = [
        "What are the best affordable airpods?",  # Persona + Template + Alternative Approaches
        "Can you suggest a gift for someone who loves tech gadgets?",  # Recipe + Ask for Input
        "List all available categories.",  # Menu Actions + Fact Check List
        "What are the top-rated products in the wireless earbuds category?",  # Persona + Audience Persona
        "Guess the most popular product in electronics this week!"  # Game Play Pattern
    ]

    for question in questions:
        try:
            response = chain.invoke(question)
            print(f"Question: {question}\nResponse:\n{response}\n")
        except Exception as e:
            logging.error(f"Error processing question '{question}': {e}")
