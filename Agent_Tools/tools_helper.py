from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
import os
os.environ['GOOGLE_API_KEY']="AQ.Ab8RN6JPFVJCDl-596Yha-krhSHlwnlyrLF4Ij28OVfQR5Pbzw"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
    )
def write_para(topic):
    prompt=f"Generate a paragraph related to this topic: {topic}"
    ans=llm.invoke(prompt)
    return ans.content 

