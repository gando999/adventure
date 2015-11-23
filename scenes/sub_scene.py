from base import BaseScene


class SubScene(BaseScene):
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices
