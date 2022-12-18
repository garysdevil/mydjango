from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

import os
import openai


def import_env():
    if os.path.exists('.env'):
        print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            key, value = var[0].strip(), var[1].strip()
            os.environ[key] = value
import_env()
openai.api_key = os.getenv("OPENAI_API_KEY")
print(f'ENV openai.api_key={openai.api_key}\n')
    

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def chat(request, prompt):
    # if request.method == "POST":
    #     data = request.POST
    #     prompt = data.get("prompt")
    # print("=", prompt)

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.9,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        stop = [" Human:", " AI:"]
    )
    responce = response['choices'][0]['text']
    print(responce)
    return HttpResponse(responce)