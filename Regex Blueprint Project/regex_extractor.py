import re

class RegexExtractor:
    def __init__(self, text):
        self.text = text

    def extract_digits(self):
        return re.findall(r'\d+', self.text)

    def extract_words(self):
        return re.findall(r'\b\w+\b', self.text)

    def extract_emails(self):
        return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', self.text)

    def extract_phone_numbers(self):
        return re.findall(r'\+?\d[\d\s\-\(\)]{7,}\d', self.text)

    def extract_urls(self):
        return re.findall(r'https?://[^\s]+', self.text)

    def extract_ipv4_addresses(self):
        return re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', self.text)

    def extract_custom(self, pattern):
        """Extract based on any custom pattern you pass."""
        return re.findall(pattern, self.text)
