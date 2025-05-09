from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END


class AgentState(TypedDict):
    input: str
    chat_history: list
    output: str

def simple_agent_node(state: AgentState):
    print("Executing")
    user_input = state.get("input", "")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = llm.invoke(f"You are a helpful assistant. The user said: '{user_input}'."
                          f"Briefly acknowledge it.")
    print(f"Response: {response}")
    return {"agent_outcome": response.content}

def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("simple_agent", simple_agent_node)
    workflow.set_entry_point("simple_agent")
    workflow.add_edge("simple_agent", END)

    app = workflow.compile()
    print("graph compiled")
    return app

if __name__ == "__main__":
    app = build_graph()
    inputs = {"input": "Hello, how are you?"}
    for output_chunk in app.stream(inputs):
        for key, value in output_chunk.items():
            print(f"Output: {key}")
            print("---")
            print(value)
        print("\n---\n")