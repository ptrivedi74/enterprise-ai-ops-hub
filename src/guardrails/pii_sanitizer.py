import re


class PIISanitizer:
    def __init__(self):
        self.email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        self.phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    def sanitize(self, text: str) -> str:
        """Redacts sensitive PII before payload reaches external LLM endpoints."""
        clean_text = re.sub(self.email_pattern, '[REDACTED_EMAIL]', text)
        clean_text = re.sub(self.phone_pattern, '[REDACTED_PHONE]', clean_text)
        return clean_text


if __name__ == "__main__":
    sanitizer = PIISanitizer()

    sample_text = "Contact patient John Doe at john.doe@example.com or 555-123-4567."
    print("Sanitized Output:", sanitizer.sanitize(sample_text))
