import re

class Settings():
    """Settings for extracting events."""
    
    def __init__(self):
        """Initialize the settings."""
        self.pattern = r"""(?x)
            (?:[ \.]?[A-Z]+\w*[ \.]?)+           # Abbreviations
            |\$?[(INR )(Rs.)]?\d+(?:[:\.]\d+)?%? # Money/Percentages
            |\w+(?:[-'@]\w+)*                    # Hyphen/e-mail
        """
