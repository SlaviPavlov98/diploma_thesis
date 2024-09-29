import openai
import os

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)


def get_openai_response():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-4o-mini",
    )

    return chat_completion.choices[0].message.content


response = get_openai_response()
print(f'Response: {response}')