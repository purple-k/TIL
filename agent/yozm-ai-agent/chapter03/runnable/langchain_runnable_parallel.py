from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = ChatPromptTemplate.from_template("주어진 '{word}'와 유사한 단어 3가지를 나열해주세요. 단어만 나열합니다.")
model = ChatOpenAI(model="gpt-5-mini")
parser = StrOutputParser()

analysis_chain = RunnableParallel(
    synonyms=prompt | model | parser,
    word_count=RunnableLambda(lambda x: len(x["word"])),
    uppercase=RunnableLambda(lambda x: x["word"].upper()),
)

result = analysis_chain.invoke({"word": "peaceful"})
print(result)
