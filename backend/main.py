from langgraph.graph import StateGraph, END
from typing import TypedDict
import random
import string
from agents.answerQnaAgent import AnswerQnaAgent
from agents.answerRagAgent import AnswerRagAgent
from agents.decisionAgents import isQueryRelevantAgent
from agents.intialAnsweringAgent import InitialAnsweringAgent
from agents.qnaDbAgents import QuestionFinderAgent,add_qna_to_backend

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class GraphState(TypedDict):
    question: str
    query_relevance: str  # will hold "yes" or "no"
    x: list|str  # hold the formatted documents (question + objectID)
    final_answer: str

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def isQueryRelevantNode(state: GraphState) -> GraphState:
    """ Check if the query is relevant. """
    print("🤖 Checking query relevance...")
    query = state["question"]
    relevance = isQueryRelevantAgent(query)
    print(f"Query relevance: {relevance}")
    state["query_relevance"] = relevance
    return state

def checkRelevance(state: GraphState) -> str:
    """Conditional router based on query relevance."""
    if state["query_relevance"] == "yes":
        return "yes"  
    else:
        return "no"  # no ya error ane pe idhar jayega --> direct answer InitialAnsweringNode ke paas


def InitialAnsweringNode(state: GraphState) -> GraphState:
    """ Returns an answer directly for irrelevant queries. """
    print("🤖 Providing initial answer...")
    query = state["question"]
    answer = InitialAnsweringAgent(query)
    state["final_answer"] = answer
    return state

def QuestionFinderNode(state: GraphState) -> GraphState:
    """ Either Find related questions and return documents with object IDs. or no  """
    # Simulate documents with object IDs (you can implement a real search here)
    print("🤖 Finding related questions...")
    query = state["question"]
    output = QuestionFinderAgent(query, k=4)
    state["x"] = output
    if(output == "no"):
        print("No related questions found.")
    else:
        print(f"Related questions found:")
    return state

def checkRedundence(state: GraphState) -> str:
    """ Check if the question is redundant. """
    print("🤖 Checking for redundancy...")
    if state["x"] == "no":
        return "no"  # name of the next node for 'yes'
    else:
        return "yes"   # name of the next node for 'no'

def AnswerQnaNode(state: GraphState) -> GraphState:
    """ Process query and documents to generate the final answer. """
    print("🤖 Answering using QnA...")
    query = state["question"]
    related_qa = state["x"]
    answer = AnswerQnaAgent(query, related_qa)
    state["final_answer"] = answer
    return state

def AnswerRagNode(state: GraphState) -> GraphState:
    """ Generate final answer using RAG (Retrieval-Augmented Generation) Node. """
    print("🤖 Answering using RAG...")
    query = state["question"]
    vectorstore_name = "faiss_vector_store"
    answer = AnswerRagAgent(query, vectorstore_name)
    state["final_answer"] = answer
    return state

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

workflow = StateGraph(GraphState)

workflow.add_node("is_query_relevant", isQueryRelevantNode)
workflow.add_node("initial_answering", InitialAnsweringNode)
workflow.add_node("question_finder", QuestionFinderNode)
workflow.add_node("answer_qna", AnswerQnaNode)
workflow.add_node("answer_rag", AnswerRagNode)

workflow.set_entry_point("is_query_relevant")
workflow.add_conditional_edges(
    "is_query_relevant",
    checkRelevance,
    {
        "yes": "question_finder",
        "no": "initial_answering",
    },
)
workflow.add_edge("initial_answering", END)
workflow.add_conditional_edges(
    "question_finder",
    checkRedundence,
    {
        "yes": "answer_qna",
        "no": "answer_rag",
    },
)
workflow.add_edge("answer_qna",END)
workflow.add_edge("answer_rag",END)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

app = workflow.compile()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def run_qna_workflow(query: str) -> str:
    """Runs the QnA LangGraph workflow and returns the final answer."""
    input_state = {
        "question": query,
        "query_relevance": "",  
        "x": "",                 
        "final_answer": ""       
    }
    final_state = app.invoke(input_state)
    return final_state.get("final_answer", "⚠️ No answer generated.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # query = "What is the capital of France?"
    # query = "How do I fix segmentation faults in MATLAB?"
    query = "What is ldd:FATAL: Could not load library xyz.so? How do I fix it?"
    print("Query:")
    print(query)
    final_answer = run_qna_workflow(query)
    print("Final Answer:")
    print(final_answer)