#  Multi-Agent Research Assistant

An AI-powered Multi-Agent Research Assistant built using **LangChain**, **Groq LLM**, **Tavily Search**, and **Streamlit**.

The application automatically researches a topic, reads relevant web pages, generates a structured research report, and provides critical feedback on the generated report.

---

##  Features

###  Research Agent

* Searches the web using Tavily Search API
* Finds relevant and recent information
* Collects sources and URLs automatically

###  Reader Agent

* Extracts content from URLs
* Cleans webpage content using:

  * Trafilatura
  * Readability
  * BeautifulSoup
* Generates concise summaries of webpages

###  Writer Agent

* Creates detailed research reports
* Generates:

  * Introduction
  * Key Findings
  * Conclusion
  * Sources

###  Critic Agent

* Reviews generated reports
* Provides:

  * Score
  * Strengths
  * Areas for Improvement
  * Final Verdict

###  Streamlit UI

* Modern dark-themed interface
* Interactive research workflow
* Real-time report generation

---


#  Tech Stack

## AI & LLM

* LangChain
* Groq API
* Llama 3 Models

## Search & Retrieval

* Tavily Search API
* Requests

## Web Scraping

* BeautifulSoup4
* Trafilatura
* Readability-LXML

## Frontend

* Streamlit

## Deployment

* Docker
* AWS EC2
* Amazon ECR
* GitHub Actions

---

#  Project Structure

```text
Multi-Agent/
│

├── app.py

├── main.py

├── requirements.txt

├── Dockerfile

├── .env

│

├── src/

│   ├── agents/

│   │   └── agents.py

│   │

│   ├── tools/

│   │   └── tools.py

│   │

│   └── workflow/

│       └── workflow.py

│

├── research_report.md

│

└── .github/

    └── workflows/

        └── deploy.yml
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/kanishka-rani-2005/Multi-Agent.git

cd Multi-Agent
```

## Create Virtual Environment

### Windows

```bash
python -m venv env

env\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv env

source env/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

#  Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---


#  AWS Deployment

The project supports:

* AWS EC2
* Amazon ECR
* GitHub Actions CI/CD
* Docker-based deployment

---

#  CI/CD

GitHub Actions automatically:

* Builds Docker image
* Pushes image to Amazon ECR
* Pulls latest image on EC2
* Restarts application
* Deploys new version automatically

---


### Output

✔ Research Sources

✔ Webpage Summaries

✔ Detailed Research Report

✔ AI-Based Critique

---


#  Author

**Kanishka Rani**

B.Tech Computer Science Engineering

Thapar Institute of Engineering and Technology

---

