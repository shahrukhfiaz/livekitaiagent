import openai
import config

def get_llm_response(prompt):
    openai.api_key = config.OPENAI_API_KEY
    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI agent."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion['choices'][0]['message']['content']
