import json
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

dp = os.path.join(os.path.dirname(__file__), '..', 'Data', 'employees.json')
with open(dp, 'r') as f:
    emp = json.load(f)['employees']

def fp(em):
    return f"{em['name']} {' '.join(em['skills'])} {em['experience_years']} years {' '.join(em['projects'])}"
flat = [fp(e) for e in emp]
prof = model.encode(flat)

def search(query,top_k=3):
    qv = model.encode([query])
    sim = cosine_similarity(qv, prof)[0]
    top= sim.argsort()[::-1][:top_k]
    return [emp[i] for i in top], sim[top].tolist()


#for verification, uncomment the following lines
# if __name__ == "__main__":
#     results, scores = search("Looking for 3 years GCP experience", top_k=3)
#     for r, s in zip(results, scores):
#         print(f"{r['name']} - Score: {s:.2f}")

def for_response(candi, scores):
    response = []
    for emp, score in zip(candi, scores):
        name = emp['name']
        experience = emp['experience_years']
        projects = ', '.join(emp['projects'])
        skills = ', '.join(emp['skills'])
        available_raw = emp.get('available', False)
        available = (
            available_raw if isinstance(available_raw, bool)
            else str(available_raw).strip().lower() == 'true'
        )
        summary = (
            f"{name} has {experience} years of experience, worked on projects like {projects}, "
            f"skilled in {skills}."
        )
        response.append(summary)
    return "Based on your query, here are the top candidates:\n\n" + "\n\n".join(response)