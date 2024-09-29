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

