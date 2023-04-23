import os
import openai



openai.api_key = "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"




start_sequence = "\nFRIDAY:"
restart_sequence = "\n\nUser:"
session_prompt = "FRIDAY created by rexy is an AI assistant that is helpful,funny,sarcastic,entertaining, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nFRIDAY:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop= ["\nFRIDAY"],
    )
    print(response)
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
