from logger import logger

class EvaluationAgent:
    def __init__(self, name="EvaluationAgent"):
        self.name = name

    def run(self, agent_outputs):
        logger.info(f"Evaluating outputs: {agent_outputs}")
        # Placeholder: could run quality heuristics, score results, etc.
        return "Evaluation complete"
