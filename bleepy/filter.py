class Bleepy:
    """A simple foul language filter."""

    def __init__(self, replacement: str = "*"):
        self.replacement = replacement

    def clean(self, text: str) -> str:
        """Replace foul words in text with the replacement character."""
        return text

    def contains(self, text: str) -> bool:
        """Return True if the text contains foul language."""
        return False
