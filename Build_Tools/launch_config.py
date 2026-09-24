"""Launch settings shared by every build script.

Everything here is a placeholder until the owner creates the account or buys the domain.
Fill a value in, re-run the build scripts, and every PDF, page and email picks it up.
Never put passwords or API keys in this file: it is committed to the repository.
"""
STORE_URL = ""        # e.g. https://bandofone.gumroad.com  (after the Gumroad account exists)
SITE_URL = ""         # e.g. https://bandofone.co           (after a domain is bought)
NEWSLETTER_URL = ""   # e.g. the MailerLite/Kit hosted signup page
SUPPORT_EMAIL = ""    # e.g. hello@bandofone.co              (a real inbox the owner monitors)


def link(value: str, label: str) -> str:
    """Return the real value, or a clearly visible placeholder that the launch QA check flags."""
    return value if value else f"[{label}: add before launch]"
