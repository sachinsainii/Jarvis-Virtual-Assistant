from openai import OpenAI
client = OpenAI(
    api_key = "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"
)
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general task like alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)
print(completion.choices[0].message.content)


#pip install openai