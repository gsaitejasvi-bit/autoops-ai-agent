
from src.tasks.summarize import summarize_issue
from src.tasks.prioritize import prioritize_issue
from src.utils import log_step
from src.tasks.triage import triage_issue
from src.tasks.fix import generate_fix
from src.tasks.log_analysis import analyze_log

class AutoOpsAgent:
    

    def step(self, task_name, input_data):
        if task_name == "triage":
            result = triage_issue(input_data)

        elif task_name == "summarize":
            result = summarize_issue(input_data)

        elif task_name == "prioritize":
            result = prioritize_issue(input_data)
        elif task_name == "fix":
            result = generate_fix(input_data)  
        elif task_name == "log_analysis":
            result = analyze_log(input_data)      

        else:
            raise ValueError(f"Unknown task: {task_name}")

        log_step(task_name, result)
        return result