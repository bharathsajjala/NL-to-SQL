
# Natural Language to SQL (NL → SQL) Agent

### **LangChain • LLMs • Oracle / MySQL / Postgres / SQLite support**

![https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/02/22/ML-16098-image01-Architecture.png](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/02/22/ML-16098-image01-Architecture.png)

![https://media.geeksforgeeks.org/wp-content/uploads/20240417181953/Untitled-drawing.jpg](https://media.geeksforgeeks.org/wp-content/uploads/20240417181953/Untitled-drawing.jpg)

![https://www.ema.co/_next/image?q=75&url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fq7d1vb20%2Fproduction%2F926064e050d97effa9f8f4256ac9a5863b5928b2-1600x635.png&w=3840](https://www.ema.co/_next/image?q=75&url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fq7d1vb20%2Fproduction%2F926064e050d97effa9f8f4256ac9a5863b5928b2-1600x635.png&w=3840)

4

This project converts **natural-language questions** into **executable SQL queries**, runs them on a target database, and returns clean results.

It uses **LangChain SQL Agent**, **LLMs (OpenAI / OCI / HF)**, and database connectors to automatically generate safe and accurate SQL queries.

# 🚀 Features

-   🧠 Convert natural language to SQL (`"Show total sales by region"`)
    
-   🗂 Schema-aware SQL generation
    
-   🔍 Automatic SQL validation & error correction
    
-   🛡 Safe/Read-only query mode (prevents destructive SQL)
    
-   💬 Optional UI (Gradio / Streamlit)
    
-   🛢 Supports multiple SQL databases
    
-   🧩 Extensible architecture for enterprise use
    

----------

# 🧩 System Architecture

## 🔷 High-Level Overview

![https://www.researchgate.net/publication/378870692/figure/fig1/AS%3A11431281228744917%401710190618076/Attack-pipeline-for-the-LLM-architecture-fingerprinting.png](https://www.researchgate.net/publication/378870692/figure/fig1/AS%3A11431281228744917%401710190618076/Attack-pipeline-for-the-LLM-architecture-fingerprinting.png)

![https://images.ctfassets.net/xjan103pcp94/1vCYZeIqmd03ECO3UXcCSi/374c494a8be6000ccb7570afe40ff182/social-rag-based-llm.png](https://images.ctfassets.net/xjan103pcp94/1vCYZeIqmd03ECO3UXcCSi/374c494a8be6000ccb7570afe40ff182/social-rag-based-llm.png)

![https://www.researchgate.net/publication/380990621/figure/fig1/AS%3A11431281248166393%401717076883495/A-simple-Text-to-SQL-diagram.png](https://www.researchgate.net/publication/380990621/figure/fig1/AS%3A11431281248166393%401717076883495/A-simple-Text-to-SQL-diagram.png)

### Pipeline Explained

1.  **User asks a natural language question**  
    → “List employees hired after 2020”
    
2.  **LLM parses intent**  
    → Table selection + filter identification
    
3.  **LangChain SQL Agent generates SQL query**  
    → Uses schema inspection + prompt templates
    
4.  **Query Validator**  
    → Allows only safe `SELECT` queries  
    → Prevents destructive commands
    
5.  **Database Execution**  
    → Executes validated query  
    → Returns rows, JSON, or tables
    
6.  **LLM optional post-processing**  
    → Turns rows into readable English explanations
# Setup

### 1. Create virtual environment

`python3 -m venv .venv source .venv/bin/activate` 

### 2. Install dependencies

`pip install -r requirements.txt` 

### 3. Add environment variables

Create **`.env`**:

`OPENAI_API_KEY=your_key LLM_MODEL=gpt-4o-mini DB_TYPE=oracle DB_HOST=localhost DB_PORT=1521  DB_NAME=ORCL DB_USER=admin DB_PASSWORD=****` 

----------

# ▶️ Running the Project

`python app/main.py` 

Example Input:

`"Show top 5 employees with highest salary"` 

Output:

`SELECT name, salary FROM employees ORDER  BY salary DESC  FETCH  FIRST  5  ROWS  ONLY;` 

Result:

`[
  ["Alice", 120000],
  ["Sam", 110000],
  ["Ravi", 109000]
]` 

----------

# 🛡 SQL Safety Layer

Before executing SQL:

-   Only `SELECT` queries allowed
    
-   Detects destructive keywords:
    
    -   `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, `TRUNCATE`, `MERGE`
        
-   Rejects multiple statements (`;`)
    

Example:

❌ User: “Delete all users”  
✔ System: “This action is not allowed.”
