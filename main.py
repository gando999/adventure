import importlib
import sys


class Controller(object):
    def __init__(self, package):
        self.package = package
        self._import_scene()

    def _import_scene(self, module_name='start'):
        scene_module = importlib.import_module('.'.join([self.package, module_name]))
        self.scene = scene_module.scene

    def main(self):
        while self.scene.choices:  # or prettier: while not self.scene.is_terminal()?
            # print self.scene.name
            # print
            print self.scene.description
            print
            print "Your choices: ",
            print ', '.join(self.scene.choices.keys())

            self._setup_next()

        print
        print "THE END"

    def _setup_next(self):
        while True:
            response = raw_input('--> ')
            try:
                next = self.scene.choices[response]
            except KeyError:
                print "Come on, try a little harder!"
                continue

            try:
                self._import_scene(next)
            except ImportError:
                print "An engineering error causes the ceiling to collapse! Try a different option."


if __name__ == '__main__':
    try:
        adventure = sys.argv[1]
    except IndexError:
        print "USAGE: python main.py ADVENTURE"
        sys.exit(2)

    try:
        controller = Controller(adventure)
    except ImportError:
        print "Unknown adventure, make sure you used the correct name."
        sys.exit(2)

    controller.main()
