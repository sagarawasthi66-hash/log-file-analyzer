import argparse
import json
import re
from collections import Counter, deque
from datetime import datetime

LEVEL_RE = re.compile(r'\b(INFO|WARN|WARNING|ERROR|DEBUG|CRITICAL)\b', re.IGNORECASE)
IP_RE = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

def analyze_lines(lines):
    level_counts = Counter()
    ip_counts = Counter()
    messages = Counter()
    total = 0

    for line in lines:
        total += 1

        # Count log levels
        lev = LEVEL_RE.search(line)
        if lev:
            level_counts[lev.group(1).upper()] += 1

        # Count IP addresses
        for ip in IP_RE.findall(line):
            ip_counts[ip] += 1

        # Count messages
        msg = line.strip()
        if msg:
            messages[msg] += 1

    return {
        "total_lines": total,
        "levels": level_counts,
        "top_ips": ip_counts.most_common(5),
        "top_messages": messages.most_common(5)
    }

def main():
    parser = argparse.ArgumentParser(description="Log File Analyzer")
    parser.add_argument("file", help="Log file name")
    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            report = analyze_lines(f)

        print("\nLog Analysis Summary")
        print("====================")
        print("Total lines:", report["total_lines"])

        print("\nLevels:")
        for k, v in report["levels"].items():
            print(f"{k}: {v}")

        print("\nTop IPs:")
        for ip, count in report["top_ips"]:
            print(ip, ":", count)

        print("\nTop Messages:")
        for msg, count in report["top_messages"]:
            print(f"({count}) {msg}")

    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    main()