# Personalized Job Application Email Generator

## Overview

The **Personalized Job Application Email Generator** automates the process of creating tailored cold emails for job applications. By leveraging job description scraping and matching skills with your portfolio, this project efficiently generates personalized emails for job applications. The system utilizes **LangChain**, **ChromaDB**, **GroqCloud**, and **Streamlit** to create a seamless user experience.

## Table of Contents

- [How the Project Works](#how-the-project-works)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Conclusion](#conclusion)

## How the Project Works

1. **Scrape Job Descriptions**: The app accepts a job posting URL as input, scrapes the job description using **LangChain**, and processes the data.

2. **Match with Portfolio**: Utilizing **ChromaDB**, the scraped job description is compared to your portfolio (stored in a CSV file). The relevant projects from your portfolio are selected based on the required skills.

3. **Generate Cold Email**: The app employs **GroqCloud's AI** models to generate a personalized cold email, incorporating both the scraped job description and your portfolio data.

4. **Streamlit Interface**: A user-friendly interface built with **Streamlit** allows users to input the job URL and review the generated email.

## Technologies Used

- **LangChain**: For scraping job descriptions and orchestrating workflow logic.
- **ChromaDB**: To store and retrieve portfolio data for skill matching.
- **GroqCloud**: AI models used for generating customized cold emails.
- **Streamlit**: Provides the interactive user interface for the application.

## How They Work Together
1. **User Input**: The user inputs a job URL into the Streamlit app.
2. **Data Extraction**: The app uses WebBaseLoader (from LangChain) to fetch and load the job content from the URL.
3. **Data Cleaning**: The clean_text function sanitizes the loaded content by removing HTML tags, URLs, and extra spaces, ensuring that only meaningful text is processed.
4. **Job Details Extraction**: The cleaned job content is sent to the LangChain components to extract relevant job details, including the role and required skills.
5. **Portfolio Query**: The extracted skills are used to query the ChromaDB database for relevant links from the user's portfolio.
6. **Email Generation**: The LLM from GroqCloud is then used to generate a tailored email using the job details and the relevant portfolio links.
7. **Output Display**: The generated email is displayed in the Streamlit app for the user to see.

## Prerequisites
- Python 3.x
- Required libraries (listed in `requirements.txt`)

## Installation Instructions
```bash
pip install -r requirements.txt
```
## Setup Instructions
Set Up GroqCloud API: Add your GroqCloud API key to your environment variables:
```bash
export GROQCLOUD_API_KEY=your-api-key
```

## Prepare Your Portfolio CSV: Ensure your portfolio CSV file is placed in the resources/ folder. The CSV should contain:

Techstack: List of technologies used in each project.
Links: Links to project details or GitHub repositories.
(A sample file is uploaded)

## Running the Project
Start the Streamlit App:
```bash
streamlit run app.py
```

## Usage
1. Input Job Posting URL: Paste a job URL into the Streamlit interface.
2. Portfolio Matching: The app compares the job description with your portfolio and retrieves matching projects.
3. Generate Email: A cold email is automatically generated, which you can edit and copy for your application.


## Troubleshooting
1. Check your API key configuration if the email generation fails.
2. Ensure your portfolio CSV is correctly formatted.
   
## Future Improvements
1.Adding features to save generated emails to a file.
2.Enhancing the matching algorithm for better accuracy.

## Conclusion
The Personalized Job Application Email Generator streamlines the job application process by automating cold email creation. It combines advanced AI from GroqCloud with LangChain for scraping and ChromaDB for portfolio matching, all within a user-friendly Streamlit interface.

