ENV_STATE = {
    "issues": [],
    "summaries": {},
    "priorities": {}
}

def load_issues():
    ENV_STATE["issues"] = [
        {"id": 1, "title": "Bug: login fails", "body": "User cannot login"},
        {"id": 2, "title": "Feature: add dark mode", "body": "Users want dark theme"},
    ]