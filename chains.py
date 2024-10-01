
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            json_res = json_parser.parse(res.content)

            # Ensure the output is always a list
            if isinstance(json_res, list):
                return json_res  # Return as is
            elif isinstance(json_res, dict):
                return [json_res]  # Wrap dict in a list

        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are John Doe, a recent graduate from Stanford University, where you completed your majors in Data Science. 
            You possess a strong understanding of machine learning, artificial intelligence, data analysis, cloud computing, and other related technologies. 
            During your academic career, you have successfully completed various projects that demonstrate your expertise in these fields, including predictive analytics, 
            natural language processing, and big data management. 
            Your job is to write a cold email to the hiring manager describing your qualifications and how they align with the requirements mentioned in the job description above. 
            Additionally, include relevant projects from the following portfolio links: {link_list} to showcase your work and capabilities.
            Highlight how these projects demonstrate your proficiency in handling real-world problems and providing effective solutions. 
            Maintain a professional tone and emphasize your passion for data-driven solutions. 
            Do not provide a preamble.

            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))


