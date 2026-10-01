from typing import Dict, Any


class OperationAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def process_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        # Simulated agent logic for document evaluation
        urgency = "HIGH" if "urgent" in task_data.get("details", "").lower() else "NORMAL"
        requires_human_review = urgency == "HIGH"

        return {
            "agent": self.name,
            "status": "PROCESSED",
            "urgency": urgency,
            "requires_human_approval": requires_human_review,
            "recommended_action": f"Draft priority response for task ID {task_data.get('id')}"
        }


if __name__ == "__main__":
    agent = OperationAgent(name="LogisticsRouter", role="Exception Classifier")
    result = agent.process_task({"id": "TASK-102", "details": "Urgent shipment delay at regional hub"})
    print("Agent Decision:", result)
