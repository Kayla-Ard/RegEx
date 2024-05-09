# Lesson 4: Assignments | Regex
# 1. Python Regular Expressions Deep Dive
# Task 1: Email Extraction Enhancement
# Problem Statement: You have a script that extracts email addresses from a text,
# but needs to be refined to exclude certain domains (e.g., 'exclude.com').
# Modify the script to extract all email addresses except those from the specified domain.
# Expected Outcome:
# Adapt the regex pattern to exclude email addresses from 'exclude.com'.
# Ensure the script still extracts all other valid email addresses.

# Code Example: 
# text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9À-ÿ._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", text)
extracted_emails = [email for email in emails if "user2@exclude.com" not in email ]
print(extracted_emails)

# This way also works 
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails= re.findall(r"\b[A-Za-z0-9À-ÿ._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", text)
print(emails)