# Log File Analyzer

A Python-based tool to analyze log files and extract useful insights such as error frequency, IP activity, and message patterns.

---

## Features

* Count log levels (INFO, ERROR, WARNING, DEBUG, CRITICAL)
* Identify top IP addresses
* Detect repeated log messages
* Simple command-line interface
* Fast and lightweight

---

## 🛠️ Technologies Used

* Python
* Regular Expressions (re)
* Collections (Counter)

---

## 📂 Project Structure

log_project/
│
├── log_analyzer.py
├── sample.txt
├── README.md

---

## ▶️ How to Run

1. Open terminal in project folder
2. Run the command:

python3 log_analyzer.py sample.txt

---

## 📄 Sample Input

INFO System started 192.168.1.2
ERROR Login failed 192.168.1.1

---

## 📊 Output

* Total number of log entries
* Count of each log level
* Top IP addresses
* Most repeated messages

---

## Use Cases

* System monitoring
* Cybersecurity log analysis
* Debugging server issues

---

## Description

This project processes log files and extracts meaningful insights using Python. It helps in identifying errors, monitoring activity, and analyzing system behavior efficiently.

---

## Author

Sagar Awasthi
