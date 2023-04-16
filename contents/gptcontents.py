from trash_objects import objects_list
import os
import openai
import config #key stored in config.py
openai.api_key = config.OPENAI_API_KEY

my_list = objects_list()

def diy_generation(query):
    # print(my_list.get(0))
    #response = openai.Completion.create(
        # model="gpt-3.5-turbo",
        # prompt="Imagine you are a professional hobbyist, Generate a DIY project utilizing any combination of the following supplies: {}".format(query),
        # temperature=0.7,
        # max_tokens=300,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional hobbyist, with vast experience in DIY projects."},
            #{"role": "user", "content": 'Come up with a DIY project using the following materials:  "{text}.format(text=query)}"'}
            {"role": "user", "content": f'Come up with a DIY project using the following materials: "{query}"'}
            # {"role": "hobbyist", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            # {"role": "user", "content": "Where was it played?"}
        ]
    )
        

    #print(response) to find format of gpt response
    if 'choices' in response:
        if len(response['choices']) > 0:
            raw_answer = response['choices'][0]['message']['content']
        else:
            "Sorry, I don't have an answer for that."
    else:
        "Sorry, I don't have an answer for that."
    
    return raw_answer
    
# query = '1 plastic bottle, 1 wooden box, 1 cloth'
# diy_generation(query)

# {
#   "choices": [
#     {
#       "finish_reason": "length",
#       "index": 0,
#       "logprobs": null,
#       "text": ", a small wooden box, and a piece of cloth.\n\nStep 1:\n\nTake one plastic bottle and cut it into two parts.\n\nStep 2:\n\nDrill a hole on the bottom, and insert the box.\n\nStep 3:\n\nTake the remaining bottle and cut it into two parts, then place it on the upper part of the wooden box.\n\nStep 4:\n\nTake the piece of cloth and place it on the top of the"
#     }
#   ],
#   "created": 1681625113,
#   "id": "cmpl-75pndM5aO7chwkJQn9pawFItlSEMx",
#   "model": "davinci",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 100,
#     "prompt_tokens": 21,
#     "total_tokens": 121
#   }
# }


    
