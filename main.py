import requests
import argparse
from bs4 import BeautifulSoup
import os
import textwrap
import sys
import wikipedia
from GPT_API import *

sources = ['wikipedia', 'wiki', 'google', 'stackoverflow']

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--site", default="wikipedia", choices=sources)
parser.add_argument("-q", "--query", default="", required=True, help="command to search")

args = parser.parse_args()
print("Want to know about the command : " + args.query)
print("Fetching information for the command "+args.query+" from "+args.site+".")
if(args.site == "wikipedia" or args.site == "wiki"):
	
    result = wikipedia.summary("'%s' linux command" %args.query, sentences = 7)
    print(result)
                      
# soup=BeautifulSoup(html_doc, 'html.parser')
# print(soup)
'''for p in soup.find_all('p'):
            # print textwrap.fill(p.get_text())
            # print textwrap.dedent(p.get_text()).strip()
            print textwrap.fill(textwrap.dedent(p.get_text()).strip(), initial_indent='', subsequent_indent='    ')

'''
# This code for Openai with langchain
print(" DO you want to use GPT with langchain choose options ")
print("1 Yes")
print("2 No")

try :
    choice = int(input("Enter the option "))
    if choice == 1:
        print("What do you want to select the choice ")
        print("1 Normal GPT")
        print("2 GPT with langchain")
        print("3 GPT with langchain using chatbot")
        Gpt_choice = int(input("Enter the option "))
        if Gpt_choice == 1:
            Question = input("What is your question ")
            answer = get_message(Question)
            print(answer)
        elif Gpt_choice == 2:
            Question = input("What is your question ")
            answer = LLMPromptTemplate(Question)
            print(answer)
        else:
            Question = input("What is your question ")
            answer = Chatbot(Question)
            print(answer)
except Exception as e :
    print("the error is:", e)