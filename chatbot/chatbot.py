from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# You must start the ollama server by using the command ollama serve


#creates a template for the prompt
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model  # Links the prompt to the LLM

def handle_conversation():
    context = ""
    print()
    print("Welcome to the AI Chatbot, Type 'exit' to quit.")
    print()
    while True:
        user_input = input("You: ")
        print()
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Chatbot: ", result)
        print()
        context += f"\nUser {user_input}\nAi {result}"

if __name__ == "__main__":  # only runs if this is the main python file.
    handle_conversation()





