def analyze_log(log_text):
    if "NullPointerException" in log_text:
        cause = "Null value accessed"
        fix = "Check for null before accessing object"
    elif "500" in log_text:
        cause = "Server error"
        fix = "Check backend API and database"
    else:
        cause = "Unknown error"
        fix = "Check logs manually"

    return {
        "cause": cause,
        "fix": fix
    }