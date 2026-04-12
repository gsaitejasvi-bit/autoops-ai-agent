def prioritize_issue(issue):
    if "bug" in issue["title"].lower():
        priority = "high"
    else:
        priority = "medium"

    return {"id": issue["id"], "priority": priority}