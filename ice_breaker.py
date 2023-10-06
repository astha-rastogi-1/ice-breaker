import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


from third_parties.linkedin import scrape_linkedin_profile
from third_parties.linkedin_lookup_agent import lookup

load_dotenv()
information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of September 2023, according to the Bloomberg Billionaires Index, and $253 billion according to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.[4][5]
"""

if __name__=="__main__":
    print("Hello langchain")

    linkedin_profile_url = lookup(name="Eden Marco")
    print(f"URL: {linkedin_profile_url}")

    summary_template = """
        given the LinkedIN information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile("https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json")

    print(chain.run(information=linkedin_data.json()))