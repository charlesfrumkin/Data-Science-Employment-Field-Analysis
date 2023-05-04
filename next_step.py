#langchainintegration 
#imports
import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage, Document
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.embeddings import OpenAIEmbeddings



#key
openai.api_key = "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"

##llms import, basic    
text ='What is the capital of Romania?'
llm=OpenAI(temperature =.9, openai_api_key = "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")
print(llm(text))


#text schema
chat = ChatOpenAI(temperature = .7, openai_api_key = "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")

chat(
    [
        SystemMessage(content = "You are a nice AI bot that helps a use figure out what to eat in one short sentence"),
        HumanMessage(content = "I like tomatoes, what should I eat?")
    ]
)

## more advanced multi chat schema model setup
chat(
    [
        SystemMessage(content = "You are a nice AI bot that helps a user figure out where to travel"),
        HumanMessage(content= 'I like the beaches where should I go'),
        AIMessage(content = 'You should go to Nice, France'),
        HumanMessage(content = "what else should I do when I am there?")  
    ]
)

##  Brink Use Case Chat, system message

chat(
    [
        SystemMessage(content = "You are a nice AI bot that returns your response in german if the word 'Briink'\
                                 is mentioned in the content of the human message"),
        HumanMessage(content= 'Someone at Briink was wondering: what is the square root of 8?'),
    ]
)

## Documents Schema Practice

Document(
    page_content="This is my document. It is full of text that I've gathered from other places",
    metadata={
        'my_document_id' : 234234,
        'my_document_source' : 'The LangChain Papers',
        'my_document_create_time' : 1680013019
    })


## Prompt Templates with multiple input variables

llm = OpenAI()

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["adjective", "product"],
    template="What is a good {adjective} name for a company that makes {product}?"
)

# Use the prompt template to create a prompt string
prompt = prompt_template.format(adjective="itchy", product="socks")

# Create a chain using the prompt and the language model
chain = LLMChain(llm=llm, prompt=prompt)

# Generate a response from the chain
response = chain.run()

# Print the response
#print(response)

## Embeddings
embeddings = OpenAIEmbeddings(openai_api_key = "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")
text = "Hi! It's time for the beach"

text_embedding = embeddings.embed_query(text)
#print (f"Your embedding is length {len(text_embedding)}")
#print(f"Here's a sample: {text_embedding[:5]}")















