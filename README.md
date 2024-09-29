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

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/personalized-job-application-email-generator.git
   cd personalized-job-application-email-generator
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up GroqCloud API:

Add your GroqCloud API key to your environment variables:
bash
Copy code
export GROQCLOUD_API_KEY=your-api-key
Prepare Your Portfolio CSV:

Ensure your portfolio CSV file is placed in the resources/ folder. The CSV should contain:
Techstack: List of technologies used in each project.
Links: Links to project details or GitHub repositories.
Running the Project
Start the Streamlit App:

bash
Copy code
streamlit run app.py
Generate Cold Emails:

Enter the job posting URL into the app.
The system scrapes the job description, matches it against your portfolio, and generates a personalized cold email.
Usage
Input Job Posting URL: Paste a job URL into the Streamlit interface.

Portfolio Matching: The app compares the job description with your portfolio and retrieves matching projects.

Generate Email: A cold email is automatically generated, which you can edit and copy for your application.

Conclusion
The Personalized Job Application Email Generator streamlines the job application process by automating cold email creation. It combines advanced AI from GroqCloud with LangChain for scraping and ChromaDB for portfolio matching, all within a user-friendly Streamlit interface.
