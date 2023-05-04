##This bot is just built with openai API, a LangChain Integration is next...

import openai
import os

# Set up OpenAI credentials
openai.api_key = "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"

# Define a function to handle user input
def handle_input(user_input, model, prompt):
    # Use OpenAI to answer the question
    prompt += user_input + "\n"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=.5,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Return the OpenAI response as the bot's answer
    answer = response.choices[0].text.strip()
    prompt += answer + "\n"
    return answer, prompt

# Define the initial prompt
prompt = "The following questions will be asked from a UChicago \
         Class canvas quiz assignment.The class in Economics in a \
            globalized world. Respond 'true' or 'false' depending on \
                if the statements entered are true or false.\n"

# "Ask me anything!\n"

# Define the model to use
model = "text-davinci-002"

# Loop to keep the chat program running
while True:
    user_input = input("What is your question? ")   
    if user_input.lower() in ["exit", "quit"]:
        break
    answer, prompt = handle_input(user_input, model, prompt)
    print("Answer: " + answer)




