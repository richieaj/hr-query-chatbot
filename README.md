# 🤖 HR Query Chatbot

A lightweight AI-powered chatbot built with FastAPI and SentenceTransformers to help HR teams **instantly find top-matching employees** based on natural language queries like:

> *"Looking for someone with 3 years of AWS experience"*  
> *"Need ML engineers who’ve worked in healthcare"*  

## 🚀 Features

- 🔍 **Semantic Search** using `MiniLM-L6-v2` from `SentenceTransformers`
- 📁 Simple and clean employee database in JSON
- 🌐 FastAPI backend with interactive Swagger UI
- 🧠 Cosine similarity to match HR queries with employee profiles
- 🖥️ Lightweight HTML frontend for demo
- 🎯 Returns **natural language summaries** of the best-matching employees

---

## 🛠️ Tech Stack

Backend = FastAPI | Embeddings = SentenceTransformers | ML Model = `all-MiniLM-L6-v2` | Similarity = scikit-learn (cosine) | Frontend = Plain HTML + JS Fetch 

## 📂 Project Structure

├── App
│ ├── init.py
│ ├── rag.py # Core logic: encoding, searching, response narration
│
├── Data
│ └── employees.json # List of employee profiles
│
├── Frontend.html # Simple UI for demo
├── main.py # FastAPI app entry point
├── .gitignore

## 🧪 How It Works

1. **Run the app** locally:
   ```bash
   uvicorn main:app --reload
Open your browser at http://127.0.0.1:8000

Enter any HR-style query (e.g. "AI in healthcare") and press Search

App shows top-matching employees with natural-language summaries

🧠 Example Response
Query: "Looking for 3 years of experience in AWS"
Response:
Tony Iommi has 6 years of experience, worked on projects like Serverless Infrastructure, skilled in AWS, Lambda, CloudFormation, and is currently not available.

📝 Notes
This is a non-LLM version. It does not retain conversational memory.

It uses static employee profiles for quick lookup.

Built and demo-ready in under 2 hours 🚀 (yep, really).

📹 Demo Video
🎥 Demo.mp4 – (link here once uploaded to Google Drive or YouTube)

📜 License
This project is licensed under the MIT License – feel free to use, modify, or fork.

🙋‍♂️ Author
Jolinson Richie
🔗 GitHub

🤝 Contributions
Pull requests welcome. For major changes, please open an issue first.
