import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

load_dotenv()
information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of September 2023, according to the Bloomberg Billionaires Index, and $253 billion according to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.[4][5]
"""

if __name__=="__main__":
    print("Hello langchain")
    # print(os.environ['OPENAI_API_KEY'])

    summary_template = """
        given the information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))