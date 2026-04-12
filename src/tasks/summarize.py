def summarize_issue(issue):
    summary = issue["title"] + " - " + issue["body"][:50]
    return {"id": issue["id"], "summary": summary}