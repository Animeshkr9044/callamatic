import os
import openai
from dotenv import load_dotenv, find_dotenv
import panel as pn

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = "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"

def collect_messages(prompt):
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#FF0000'})))

    return pn.Column(*panels)

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

panels = []  # collect display
context = [{'role': 'system', 'content': """
you are a ai salesbot, automated servise to collect the  infromation for loan inquiry\
you first greet the user,\
then start the message is the user intresed in loan\
and then if the user agrees then ask user about the amount of loan they are willing to take \
then aks the user user about the purpose of loan like CAR/BUSSINESS/PERSONAL\
then ask the user about his ITR status wheater he files a ITR or not \
then ask the the profession of the user \
if user profession is Business,then ask anual Turnover from the GST\
and if the user profession was any other than Business then ask about the annual salary as per salary slips\
and then ask the user have any queries \
\once the information is obtained and conservation is over \
ai salesbot should end the convesation with a goodbye message

"""}]  # accumulate messages

prompt = input("Enter your message: ")
dashboard = collect_messages(prompt)
dashboard.servable()
