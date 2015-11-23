from adventure.base import Scene

class SubScene(Scene):
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices