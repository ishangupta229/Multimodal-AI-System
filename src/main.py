from agents import RetrievalAgent, TableRetrievalAgent, ImageRetrievalAgent
from feedback import FeedbackAgent
from evaluator import EvaluationAgent

def main():
    print("----- Running RetrievalAgent (vector search) -----")
    retrieval_agent = RetrievalAgent()
    results = retrieval_agent.run("What is the use of multimodal RAG?")
    for r in results:
        print(f"Retrieved: {r}")

    print("\n----- Running TableRetrievalAgent (CSV table) -----")
    table_agent = TableRetrievalAgent()
    csv_path = "data/sample.csv"
    table = table_agent.run(csv_path)
    if table is not None:
        print(table.head())

    print("\n----- Running ImageRetrievalAgent (image OCR) -----")
    image_agent = ImageRetrievalAgent()
    image_path = "data/sample.png"
    image_text = image_agent.run(image_path)
    print(f"Extracted text from image: {image_text}")

    print("\n----- Running FeedbackAgent -----")
    feedback_agent = FeedbackAgent()
    feedback_response = feedback_agent.run(agent_output=results)
    print(feedback_response)

    print("\n----- Running EvaluationAgent -----")
    evaluator = EvaluationAgent()
    evaluation_result = evaluator.run(agent_outputs=[results, table, image_text])
    print(evaluation_result)

if __name__ == "__main__":
    main()
