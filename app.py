import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Function to create the Streamlit app
def create_streamlit_app(llm, portfolio, clean_text):
    # Page title and description
    st.title("📧 AI-Powered Job Application Assistant")
    st.markdown("""
    Welcome to the AI-powered job application assistant! This tool helps you craft personalized cold emails for job applications by extracting job descriptions from URLs and matching your portfolio projects.
    """)

    # Step 1: Input job URL
    st.header("Step 1: Enter Job Posting URL")
    url_input = st.text_input("Enter the job posting URL:", value="https://amazon.jobs/content/en/career-programs/university-ops#search")
    
    # Step 2: Submit button to process the job posting
    submit_button = st.button("Submit")

    # Process the URL input and generate the email
    if submit_button:
        try:
            # Load and clean job description data from URL
            st.info("Loading and processing job description...")
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            
            # Load portfolio data
            st.info("Loading portfolio data...")
            portfolio.load_portfolio()
            
            # Extract job information and generate email
            st.success("Generating personalized email...")
            jobs = llm.extract_jobs(data)
            for job in jobs:
                # Get the job title (or role)
                job_title = job.get('role', 'Job')  # Default to 'Job' if 'role' is not found
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)

                # Display the generated email with the job title
                st.markdown(f"### Email for {job_title}:")
                st.code(email, language='markdown')

        except Exception as e:
            # Display an error message if something goes wrong
            st.error(f"An error occurred: {e}")

# Main function to set up the app and run it
if __name__ == "__main__":
    # Initialize Chain and Portfolio
    chain = Chain()
    portfolio = Portfolio()

    # Set page configuration
    st.set_page_config(
        page_title="AI-powered Job Application Assistant",
        page_icon="📧",
        layout="wide"
    )

    # Create and run the Streamlit app
    create_streamlit_app(chain, portfolio, clean_text)




