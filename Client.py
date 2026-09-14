from openai import OpenAI;

# If you Saved the Key Under a Different Environment Variable Name, You can do Something Like.
client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud",
        },
        {"role": "user", "content": "what is coding"},
    ],
)
print(completion.choices[0].message.content)