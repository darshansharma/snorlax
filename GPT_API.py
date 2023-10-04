import openai
import os
from dotenv import main
main.load_dotenv()

# Langchain
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains.conversation.memory import ConversationBufferMemory

API_KEY = os.getenv('API_KEY')
try :
    openai.api_key = API_KEY
except Exception as e:
    print("The error is:", e)
# This just Open AI Using gpt-3.5-turbo
def get_message(usermessage):
    usermessage = (usermessage)

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = usermessage
    )
    response = response['choices'][0]['message']['content']
    return response

# This Open AI with Langchain 

# Prompt Template
def LLMPromptTemplate(Question):
    # This temperature is to make llm model to thing creative 
    llm = OpenAI(temperature = .5)
    # This custom template so any user can edit this template
    template = """Your are a amazing coder with loneliness Your duty to wite code and make more bug reports.Your job to find bugs in code
                Question: {text}
                Answer: 
    """

    # We add input in {text}
    prompt_template = PromptTemplate(input_variables = ["text"], template = template)
    answer = LLMChain(llm=llm, prompt= prompt_template)
    return answer.run(Question)

def Chatbot(Question):
    llm = OpenAI(temperature = 0.5)
    # Make custom template so any user
    template = """ I'm BATMAN 
                {chat_history}
                Human : {Question}
                AI:
    """
    # Add input in Question and chat history is used to store the answer history
    prompt_template = PromptTemplate(input_variables = ["chat_history", "Question"], template = template )
    # storing the answer history
    memory = ConversationBufferMemory(memory_key = "chat_history")
    answer = LLMChain(
                llm = llm,
                prompt = prompt_template,
                 verbose = True,
                 memory = memory,
    )
    return answer.predict(Question)
