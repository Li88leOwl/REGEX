# text = """
# Agent X1A-23 reported success.
# Contact: AGENT B7Z-99 via secure channel.
# Invalid: Agent-77C-00 (fake).
# Also spotted AGENT q2p-11 and agent P9M-42 near HQ.
# """
# Each valid code follows this rule:
# Starts with the word “Agent” or “AGENT” (case-insensitive)
# Followed by a space
# Then a 3-character alphanumeric code pattern like X1A
# A dash -
# And a two-digit number like 23

# 🎯 Task:
# Write a regex that extracts all valid agent codes (e.g. "X1A-23", "B7Z-99", "q2p-11", "P9M-42") 
# but ignores the invalid "77C-00" (because it’s missing the proper prefix format).

# 1) Regex that requires the literal "Agent" (case-insensitive) followed by whitespace,
#    then captures the 3-alnum + dash + 2-digit code.
pattern = r'\bAgent\s+([A-Za-z0-9]{3}-\d{2})\b'

valid_codes = re.findall(pattern, text, flags=re.IGNORECASE)

# For comparison: find all 3-characters + dash + 2-digits anywhere (this will include invalid)
all_code_like = re.findall(r'\b[A-Za-z0-9]{3}-\d{2}\b', text)

print("=== Source text ===")
print(text.strip())
print("\n=== Regex used ===")
print(pattern)
print("\n=== Valid codes (with 'Agent' prefix) ===")
print(valid_codes)
print("\n=== All code-like patterns found (includes invalid) ===")
print(all_code_like)
STDOUT/STDERR
=== Source text ===
Agent X1A-23 reported success.
Contact: AGENT B7Z-99 via secure channel.
Invalid: Agent-77C-00 (fake).
Also spotted AGENT q2p-11 and agent P9M-42 near HQ.

=== Regex used ===
\bAgent\s+([A-Za-z0-9]{3}-\d{2})\b

=== Valid codes (with 'Agent' prefix) ===
['X1A-23', 'B7Z-99', 'q2p-11', 'P9M-42']

=== All code-like patterns found (includes invalid) ===
['X1A-23', 'B7Z-99', '77C-00', 'q2p-11', 'P9M-42']
