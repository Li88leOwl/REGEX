from regex_extractor import RegexExtractor

def test_extractor():
    text = """
    Contact me at john.doe@example.co.ke or visit https://example.com.
    My backup IP is 192.168.1.1, and my number is +254-724-123-4567.
    Total amount: KES 123.45
    """

    rex = RegexExtractor(text)

    print("📧 Emails:", rex.extract_emails())
    print("🌐 URLs:", rex.extract_urls())
    print("📞 Phone Numbers:", rex.extract_phone_numbers())
    print("🔢 Digits:", rex.extract_digits())
    print("💬 Words:", rex.extract_words())
    print("🖧 IPs:", rex.extract_ipv4_addresses())
    print("🎯 Custom (money):", rex.extract_custom(r'\$\d+\.?\d*'))

if __name__ == "__main__":
    test_extractor()
