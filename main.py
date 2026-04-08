from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
app = FastAPI()

class RequestModel(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Working ✅"}

@app.post("/run")
def run(req: RequestModel):
    query = req.query.lower()

    # ---- Smart Issue Analysis ----
    if "issues" in query:
        issues = get_issues("microsoft/vscode")

        summary = []
        for issue in issues:
            if "bug" in issue["title"].lower():
                priority = "High 🔴"
            elif "feature" in issue["title"].lower():
                priority = "Medium 🟡"
            else:
                priority = "Low 🟢"

            summary.append({
                "title": issue["title"],
                "priority": priority,
                "status": issue["state"]
            })

        return {
            "type": "AI Analysis",
            "data": summary
        }

    # ---- Dataset Cleaning ----
    elif "clean" in query:
        return {
            "type": "Processed Data",
            "data": clean_dataset()
        }

    # ---- Smart Chat ----
    elif "hello" in query:
        return {
            "type": "AI Response",
            "data": "Hello! 👋 I automate developer workflows."
        }

    else:
        return {
            "type": "AI Response",
            "data": f"I analyzed your request: {req.query}"
        }
    @app.get("/ui", response_class=HTMLResponse)
    def ui():
           with open("index.html") as f:
            return f.read()