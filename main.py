
import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'
#Pass the message to Chatgbt ai  .send() to answer

@cl.on_message
async def main(message : str):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "assistant" ,"content": "You are a helpful assistant but always starts a Joke."},
            {"role": "user", "content":message}
        ],
        temperature = 1,

    )
    await cl.Message(content = response['choices'][0]['message']['content']).send()