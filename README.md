# Personal-Chatbot
A personal chatbot project for answering general questions, built with Python and evolving toward pre-trained large language models.
This project integrates an open-source, pre-trained conversational language model
(Microsoft DialoGPT) as a fallback for open-ended user queries.

- Rule-based intent handling is used for greetings, time, and math.
- If no intent matches, the chatbot falls back to DialoGPT.
- The model runs locally using PyTorch and Hugging Face Transformers.
- No paid APIs or external services are used.
