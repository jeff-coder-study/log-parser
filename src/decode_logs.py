import json 
import os 

def decode_severity(severity_value):
    # turns severity into string names for readability 
    severity_names = {
        0: "Emergency",
        1: "Alert",
        2: "Critical",
        3: "Error",
        4: "Warning",
        5: "Notice",
        6: "Informational",
        7: "Debug"
    }
    return severity_names.get(severity_value, "Unknown")

def read_logfile(filepath): 
    full_path = os.path.expanduser(filepath)
    data = [] 
    try:
        with open(full_path, "r") as file:
            for line in file: 
                if line.strip():
                    data.append(json.loads(line))
        return data

    except FileNotFoundError:
        print("Error: json log file was not found.")
        return []

def extract_data(entry): 
    try:
        priority_num = int(entry.get("PRIORITY", 6))
    except (ValueError, TypeError):
        priority_num = 6

    severity_label = decode_severity(priority_num)
    service = entry.get("_SYSTEMD_UNIT", entry.get("SYSLOG_IDENTIFIER", "unknown"))
    message = entry.get("MESSAGE", "").strip()

    # extract just the text inside the message
    if 'msg="' in message:
        message = message.split('msg="')[1].split('"')[0]

    return {
        "severity": severity_label,
        "service": service,
        "message": message
    }


if __name__ == "__main__":
    raw_logs = read_logfile("sample_logs/example_logs.json")

    for log in raw_logs:
        summary = extract_data(log)
        if summary["severity"] in ["Error", "Critical", "Alert", "Emergency", "Warning", "Notice"]:
            print(f"[{summary['severity']}] {summary['service']}: {summary['message']}")