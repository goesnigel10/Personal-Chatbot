import random
import re
from datetime import datetime


class JarvisBot:
    """
    A simple rule-based chatbot that responds to greetings
    and basic conversational prompts using regex matching.
    """

    def __init__(self):
        self.intents = [
            {
                "name": "greeting",
                "pattern": re.compile(
                    r'\b(hello|hi|hey|yo|yooo|good morning|good afternoon|good evening|jarvis|jarvis i need your help|was good jarvis)\b'
                ),
                "responses": [
                    "Hello! Nice to meet you!",
                    "Hi there! How are you doing?",
                    "Hey! Great to see you!",
                    "Hello! Hope you're having a good day!",
                    "Jarvis at your assistance."
                ]
            },
            {
                "name": "status",
                "pattern": re.compile(
                    r'\b(how are you|how.*doing|how.*going|what.*up)\b'
                ),
                "responses": [
                    "I'm doing great, thanks for asking! How about you?",
                    "I'm good! How are you doing today?",
                    "I'm fine, thank you! How are things with you?",
                    "All good here! How's your day going?"
                ]
            },
            {
                "name": "math",
                "pattern": re.compile(r'\b\d+\s*[\+\-\*/]\s*\d+\b')
            },
            {
                "name": "time",
                "pattern": re.compile(r'\b(time|what.*time)\b')
            }
        ]

        self.default_responses = [
            "I'm still learning! Try greeting me or asking how I'm doing.",
            "I didn't quite understand that. Say hi or ask how I am!",
            "Hmm, I'm not sure how to respond to that yet."
        ]

    def should_exit(self, user_input: str) -> bool:
        return user_input in {"quit", "exit", "bye"}

    def get_time(self) -> str:
        current_time = datetime.now().strftime("%H:%M")
        return f"The time right now is {current_time}."

    def solve_math(self, user_input: str) -> str:
        match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', user_input)

        if not match:
            return "Please enter a simple math expression like '2 + 2'."

        num1, operator, num2 = match.groups()
        num1, num2 = int(num1), int(num2)

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Division by zero is not allowed."
            result = num1 / num2

        return f"The answer is {result}."

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower().strip()

        for intent in self.intents:
            if intent["pattern"].search(user_input):

                if intent["name"] == "time":
                    return self.get_time()

                if intent["name"] == "math":
                    return self.solve_math(user_input)

                return random.choice(intent["responses"])

        return random.choice(self.default_responses)

    def chat(self):
        print("Jarvis: Hi! I'm Jarvis 🤖")
        print("Jarvis: I can respond to greetings, time, and math.")
        print("Jarvis: Type 'quit' to exit.")
        print("-" * 40)

        while True:
            user_input = input("You: ").strip()

            if not user_input:
                print("Jarvis: Please type something!")
                continue

            if self.should_exit(user_input.lower()):
                print("Jarvis: Goodbye! Thanks for chatting!")
                break

            response = self.get_response(user_input)
            print(f"Jarvis: {response}")


if __name__ == "__main__":
    bot = JarvisBot()
    bot.chat()
