import openai
openai.api_key = "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"
model_engine = "gpt-3.5-turbo" 
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, ChatGPT!"},
    ])

message = response.choices[0]['message']
print("{}: {}".format(message['role'], message['content']))