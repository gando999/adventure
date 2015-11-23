class BaseScene(object):
    def _load_text(self):
        return 'Some text from {} - choose left or right'.format(self.name)

    def is_terminal(self):
        if self.choices:
            return False
        return True
