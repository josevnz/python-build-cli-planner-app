class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """

    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'


class PoliteReminder(PrefixedReminder):

    def __init__(self, text: str, date: str = None):
        super().__init__(f"Please")
        self.text = f"{self.prefix}{text}"

    def __iter__(self):
        return iter([self.text])


