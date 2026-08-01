import os
os.environ['GOOGLE_API_KEY']=""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2 )

prompt1 = PromptTemplate(
    input_variables=["cusine_name"],
    template="Give me one restaurent name for {cusine_name} served their" )

prompt2 = PromptTemplate(
    input_variables=["menue"],
    template="give me menue:\n{menue}" )

chain1 = prompt1 | llm
chain2 = prompt2 | llm

def generate_rnames(cuisine):
    restaurant = chain1.invoke({"cusine_name": cuisine})
    menu = chain2.invoke({"menue": restaurant.content})
    return {
        "restaurant_name": restaurant.content,
        "menu_items": menu.content
    }

if __name__ == "__main__":
    cuisine = "Italian"
    response = generate_rnames(cuisine)
    print(response)
