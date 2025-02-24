



import re
text = "Contact me at test@example.com and support@email.org."
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)  # Output: ['test@example.com', 'support@email.org']