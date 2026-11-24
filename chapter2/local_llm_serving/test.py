from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy" # ollama不需要真实key，随便填字符串
)

resp = client.chat.completions.create(
    model="happyai",
    messages=[{"role": "user", "content": "10-4等于多少 /think"}]
)
print(resp.choices[0].message.content)