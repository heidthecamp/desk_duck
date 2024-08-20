from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables.
load_dotenv()

# Set the model name for our LLMs.
OPENAI_MODEL = "gpt-4"
# Store the API key in a variable.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize the model for entities.
entity_llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY,
                        model_name=OPENAI_MODEL,
                        temperature=0.0)

# Initialize the model for output.
chat_llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY,
                      model_name=OPENAI_MODEL,
                      temperature=0.7)

# Create a list containing a system message and a human message.
# Add prompt engineering by refining the system message for clarity.
messages = [
    SystemMessage(content=(
        "You are a senior software developer. Your task is to provide accurate and "
        "detailed responses related to software development. If the question is "
        "outside the scope of software development, tell them to shut up and as rude as possible."
        "If the question lacks sufficient information, request clarification rather "
        "than making assumptions."
    )),
    HumanMessage(content="")  # This will be populated dynamically
]

# Initialize an object for conversational memory.
buffer = ConversationEntityMemory(llm=entity_llm)

# Create the chain for conversation, using a ConversationEntityMemory object.
conversation = ConversationChain(
    llm=chat_llm, 
    memory=buffer, 
    verbose=False, 
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE
)

def answer_user_question(question: str) -> str:
    """
    Function to answer user questions by interacting with a conversational chain.
    
    Args:
        question (str): The question or input from the user.
        
    Returns:
        str: The response generated by the AI.
    """
    # Update the human message content with the user's question.
    messages[1].content = question
    
    # Use the chat_llm to invoke the response with the updated prompt.
    result = chat_llm.invoke(messages)
    return result.content

# Example usage:
if __name__ == "__main__":
    while True:
        user_question = input("You: ")
        if user_question.lower() in ['exit', 'quit', 'stop']:
            print("Conversation ended.")
            break
        
        answer = answer_user_question(user_question)
        print(f"AI: {answer}")
