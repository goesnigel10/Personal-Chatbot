import random
import re


class JarvisBot:
    """
    A simple rule-based chatbot that responds to greetings
    and basic conversational prompts using regex matching.
    """

    def __init__(self):
        # Intent-based patterns
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
                "pattern": re.compile(
                    r'\b(math|solve.*problem)\b'
                ),
                "responses": [
                    "I can't solve math problems yet, but I will soon!",
                    "Math support is coming in a future update."
                ]
            },
            {
                "name": "time",
                "pattern": re.compile(
                    r'\b(time|what.*time)\b'
                ),
                "responses": [
                    "I can't tell the time yet, but I'll learn soon!",
                    "Time awareness isn't enabled yet."
                ]
            }
        ]

        self.default_responses = [
            "I'm still learning! Try greeting me or asking how I'm doing.",
            "I didn't quite understand that. Say hi or ask how I am!",
            "Hmm, I'm not sure how to respond to that yet."
        ]

    def should_exit(self, user_input: str) -> bool:
        """Check if the user wants to exit the chat"""
        return user_input in {"quit", "exit", "bye"}

    def get_response(self, user_input: str) -> str:
        """Return a response based on matching intent"""
        user_input = user_input.lower().strip()

        for intent in self.intents:
            if intent["pattern"].search(user_input):
                return random.choice(intent["responses"])

        return random.choice(self.default_responses)

    def chat(self):
        """Main chat loop"""
        print("Jarvis: Hi! I'm Jarvis 🤖")
        print("Jarvis: I can respond to greetings and basic questions.")
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
