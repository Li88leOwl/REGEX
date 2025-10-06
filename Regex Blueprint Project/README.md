# 🐍 Regex Pattern Extractor

A **Python-powered pattern extractor** that uses regular expressions (regex) to pull out useful patterns from text.

---

### 🔍 Supported Features

| ✅ Feature         | 🔎 Example                 |
|-------------------|---------------------------|
| **Digits**         | `123`, `007`, `404`        |
| **Words**          | `hello`, `world`, `regex`  |
| **Emails**         | `me@example.com`           |
| **Phone Numbers**  | `+1-555-1234`              |
| **URLs**           | `https://example.com`      |
| **IP Addresses**   | `192.168.1.1`              |
| **Custom Patterns**| _Anything you define_      |

---

### 🧠 Powered by Python + 🧪 Regex

Easily extendable and perfect for parsing logs, validating input, or scraping data.

> 🛠️ Build it. 🕵️ Extract it. 🔁 Repeat.

---

### 🚀 Get Started

```bash
git clone https://github.com//regex-pattern-extractor.git
cd regex-pattern-extractor
python extractor.py
```


# 🔍 Regex Pattern Cheatsheet

A quick reference for common regular expression patterns.

---

## Common Patterns

| **Pattern**                                               | **Matches**                          |
|-----------------------------------------------------------|--------------------------------------|
| `\d+`                                                     | Digits                               |
| `\b\w+\b`                                                 | Words                                |
| `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`           | Email addresses                      |
| `https?://[^\s]+`                                         | URLs                                 |
| `\+?\d[\d\s\-\(\)]{7,}\d`                                 | Phone numbers                        |
| `\b(?:\d{1,3}\.){3}\d{1,3}\b`                             | IPv4 addresses                       |
| `\$\d+\.?\d*`                                             | Dollar amounts                       |
| `.{8,}`                                                   | Strings with 8 or more characters (passwords) |

---

### 🚀 Quick Tips

- **`\d`**: Matches any digit (0-9).
- **`\w`**: Matches any word character (letters, digits, and underscores).
- **`\b`**: Word boundary.
- **`+`**: Matches one or more of the preceding token.
- **`{n,}`**: Matches **n** or more of the preceding token.
- **`[ ]`**: A character class to match one of the enclosed characters.
- **`?`**: Matches zero or one of the preceding token (makes it optional).
  
---

### ⚡ Customize Your Regex

Feel free to modify and adapt these patterns to your needs. Regex is powerful when you know how to fine-tune it!

> **Pro Tip**: Always test your regular expressions with a tool like [regex101](https://regex101.com/) before using them in your code.


