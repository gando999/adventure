
class Scene(object):
    def __init__(self, name, left, right):
        self.name = name
        self.choices = {'left': left, 'right': right}

    def _load_text(self):
        return 'Some text from {} - choose left or right'.format(self.name)

    def _is_terminal(self):
        return self.choices['left'] is None and self.choices['right'] is None

    def action(self):
        if not self._is_terminal():
            print self._load_text()
            response = raw_input('--> ')
            if response not in ('left', 'right'):
                print 'Bad choice!'
                return self.action()
            return self.choices[response].action()
        else:
            print 'Congrats you are done!'


### Set up

root = Scene(
    'root',
    Scene('scene1', None, None),
    Scene('scene2', None, None)
)

root.action()
