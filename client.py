from openai import OpenAI
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general task like alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)
print(completion.choices[0].message.content)


# #pip install openai