# 🔐 Python Security Audit Demo

This repository is part of an **internship task** to demonstrate secure coding practices in Python.  
It contains both **vulnerable code** and a **secure remediated version** inside a single file.

---

## 📌 Objective
The goal of this task is to:
- Identify common security vulnerabilities in Python applications.
- Perform a **code review** and use tools like **Bandit** for static analysis.
- Fix the vulnerabilities by applying **secure coding best practices**.
- Document findings for professional reporting.

---

## 📝 Contents
- **app_audit.py** → Single file with:
  - ❌ Vulnerable code example
  - 🔒 Secure fixed version
  - 🚀 Demo showing how SQL Injection works in vulnerable code and is prevented in secure code
- **bandit_report.txt** → Static analysis results from [Bandit](https://bandit.readthedocs.io/)

---

## ⚠️ Vulnerabilities Found
1. **Hardcoded Database Path**  
   → Fixed by using environment variables.  

2. **SQL Injection**  
   → Fixed by parameterized queries (`?` placeholders).  

3. **Insecure Error Handling**  
   → Fixed by safe exception handling with generic error messages.  

4. **Information Disclosure**  
   → Removed debug statements that leaked sensitive info.

---

## 🛠️ Tools Used
- **Bandit** (static analyzer for Python)  
  Install & run:
  ```bash
  pip install bandit
  bandit app_audit.py -f txt -o bandit_report.txt
