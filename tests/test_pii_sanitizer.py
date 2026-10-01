import sys
import os

# Add src to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from guardrails.pii_sanitizer import PIISanitizer

def test_email_redaction():
    sanitizer = PIISanitizer()
    raw_text = "Please reach out to support@example.com for assistance."
    sanitized = sanitizer.sanitize(raw_text)
    assert "[REDACTED_EMAIL]" in sanitized
    assert "support@example.com" not in sanitized

def test_phone_redaction():
    sanitizer = PIISanitizer()
    raw_text = "Call customer service at 555-123-4567."
    sanitized = sanitizer.sanitize(raw_text)
    assert "[REDACTED_PHONE]" in sanitized
    assert "555-123-4567" not in sanitized

if __name__ == "__main__":
    test_email_redaction()
    test_phone_redaction()
    print("All unit tests passed successfully!")