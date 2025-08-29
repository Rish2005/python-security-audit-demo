"""
Python Security Audit Internship Task
-------------------------------------
This file contains:
1. Vulnerable code (for demonstration)
2. Identified issues
3. Secure fixed version
"""

import os
import sqlite3

######################################
# ❌ VULNERABLE CODE
######################################

def vulnerable_login(username, password):
    """
    Issues:
    - Hardcoded database path
    - SQL Injection risk (user input in query directly)
    - No error handling
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # UNSAFE: vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("[DEBUG] Executing:", query)  # Information disclosure
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()
    return result


######################################
# 🔒 SECURE FIXED VERSION
######################################

def secure_login(username, password):
    """
    Fixes:
    - Uses environment variable for DB path
    - Parameterized queries (prevent SQL injection)
    - Error handling added
    - No debug info in production
    """

    db_path = os.getenv("DB_PATH", "users.db")  # Use env variable
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SAFE: parameterized query
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))

        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        # Do not leak system details
        print("An error occurred. Please try again later.")
        return None


######################################
# 🚀 DEMO
######################################

if __name__ == "__main__":
    print("=== Vulnerable Demo ===")
    print(vulnerable_login("admin", "1234 OR '1'='1"))  # SQL Injection works

    print("\n=== Secure Demo ===")
    print(secure_login("admin", "1234 OR '1'='1"))  # Injection blocked
