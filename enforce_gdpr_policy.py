import json
import sys

def evaluate_gdpr_compliance(report_path):
    try:
        with open(report_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: Report file '{report_path}' not found.")
        sys.exit(1)

    critical_violations = []

    # Parse Bearer scan findings
    findings = data.get("findings", [])
    for finding in findings:
        rule_id = finding.get("rule_id", "")
        title = finding.get("title", "")
        severity = finding.get("severity", "")
        
        # Flag any unencrypted PII logging or leaks
        if "logging" in rule_id or "leak" in rule_id or severity == "high":
            critical_violations.append({
                "rule": rule_id,
                "title": title,
                "severity": severity
            })

    print("==================================================")
    print("      GDPR AUTOMATED COMPLIANCE EVALUATION        ")
    print("==================================================")
    
    if critical_violations:
        print(f"❌ FAILED: Found {len(critical_violations)} violation(s) against GDPR Art. 25/32:\n")
        for v in critical_violations:
            print(f"  - [{v['severity'].upper()}] {v['rule']}: {v['title']}")
        print("\nDeployment blocked. Remediate PII logging/exposure before merging.")
        sys.exit(1)
    else:
        print("✅ PASSED: No critical GDPR violations detected. Safe for deployment.")
        sys.exit(0)

if __name__ == "__main__":
    report_file = sys.argv[1] if len(sys.argv) > 1 else "bearer-report.json"
    evaluate_gdpr_compliance(report_file)
    