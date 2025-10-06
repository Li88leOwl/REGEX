# ✅ What is Regex?

**Regex** (short for *Regular Expression*) is a mini-language for searching and matching text patterns. It's widely used in:

- ✅ Validating inputs (e.g. email, phone number)
- 🔍 Finding or extracting text (e.g. dates, numbers)
- 🔁 Replacing patterns (e.g. censoring bad words)

Regex is supported in most programming languages including **Python** (`re` module), **JavaScript**, **Java**, **Go**, and many more.

---

## 🧱 Basic Building Blocks

| **Symbol** | **Meaning**                             | **Example** | **Matches**        |
|------------|------------------------------------------|-------------|--------------------|
| `.`        | Any character (except newline)           | `a.c`       | `abc`, `a_c`, `a9c`|
| `\d`       | A digit (0–9)                            | `\d`        | `5`, `2`, `9`      |
| `\D`       | Not a digit                              | `\D`        | `a`, `#`, `X`      |
| `\w`       | Word character (letters, digits, `_`)    | `\w`        | `a`, `Z`, `7`, `_` |
| `\W`       | Not a word character                     | `\W`        | `!`, `@`, ` `      |
| `\s`       | Whitespace (space, tab, newline)         | `\s`        | `' '`, `\n`, `\t`  |
| `\S`       | Not whitespace                           | `\S`        | `a`, `1`, `#`      |
| `[...]`    | Match one character in brackets          | `[abc]`     | `a`, `b`, `c`      |
| `[^...]`   | Match anything *except* what's inside    | `[^0-9]`    | `a`, `!` (not digits) |

---

## 🔢 Quantifiers (How Many Times?)

| **Symbol**  | **Meaning**                | **Example**   | **Matches**             |
|-------------|-----------------------------|---------------|--------------------------|
| `*`         | 0 or more                   | `a*`         | `""`, `a`, `aaa`         |
| `+`         | 1 or more                   | `a+`         | `a`, `aa`, `aaaa`        |
| `?`         | 0 or 1                      | `a?`         | `""`, `a`                |
| `{n}`       | Exactly n times             | `a{3}`       | `aaa`                    |
| `{n,}`      | n or more times             | `a{2,}`      | `aa`, `aaa`, `aaaa`      |
| `{n,m}`     | Between n and m times       | `a{1,3}`     | `a`, `aa`, `aaa`         |

---

## 🧱 Anchors (Position in Text)

| **Symbol** | **Meaning**       | **Example** | **Matches**                          |
|------------|-------------------|-------------|--------------------------------------|
| `^`        | Start of string   | `^Hi`       | `Hi there`, but not `Say Hi`         |
| `$`        | End of string     | `end$`      | `the end`, but not `end of`          |

---

## 🧃 Grouping and Alternation

| **Symbol**     | **Meaning**                    | **Example**         | **Matches**                 |
|----------------|--------------------------------|----------------------|-----------------------------|
| `(…)`          | Grouping                       | `(abc)+`             | `abc`, `abcabc`             |
| `a\|b`         | Alternation (OR)               | `cat\|dog`           | `cat` or `dog`              |
| `(?:…)`        | Non-capturing group            | `(?:abc)+`           | Same match, not captured    |

---

## 🎯 Special Escape Sequences

| **Pattern** | **Meaning**           |
|-------------|------------------------|
| `\.`        | Matches a literal `.`  |
| `\\`        | Matches a literal `\`  |
| `\t`        | Matches a tab          |
| `\n`        | Matches a newline      |

---

## 📦 Practical Examples

### ✅ 1. Match a phone number: `123-456-7890`

```regex
\d{3}-\d{3}-\d{4}
