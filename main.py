import os
from dotenv import load_dotenv
from src.graph import build_graph

def main():
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

    graph_app = build_graph()
    print("AI ready to go!")
    print("type 'exit' to quit")

    while True:
        user_input = input("Enter your input: ")
        if user_input.lower() == "exit":
            break
        if user_input:
            print('processing')
            for output_chunk in graph_app.stream({"input": user_input}):
                for key, value in output_chunk.items():
                    if key == "agent_outcome":
                        print(f"AI: {value.get('agent_outcome')}")
            print("\n---\n")

if __name__ == "__main__":
    main()

