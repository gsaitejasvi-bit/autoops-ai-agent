from src.agent import AutoOpsAgent
from src.environment import load_issues, ENV_STATE
from src.agent import AutoOpsAgent


def main():
    agent = AutoOpsAgent()
    load_issues()

    for issue in ENV_STATE["issues"]:
        triage = agent.step("triage", issue)
        summary = agent.step("summarize", issue)
        priority = agent.step("prioritize", issue)
        fix = agent.step("fix", issue)
        print("\n--- LOG ANALYSIS ---")

        log = "ERROR 500 at /login - NullPointerException"

        log_result = agent.step("log_analysis", log)

        print(fix)

        print("\nFinal Output:")
        print(triage)
        print(summary)
        print(priority)
        print("\n===== AUTOOPS OUTPUT =====")
        print(f"Issue ID: {issue['id']}")
        print(f"Triage: {triage}")
        print(f"Summary: {summary}")
        print(f"Priority: {priority}")
        print(f"Fix: {fix}")

if __name__ == "__main__":
    main()