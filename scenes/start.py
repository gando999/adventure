from adventure.scenes.sub_scene import SubScene


_description = "In the begining, we find ourselves faced with several choices"

_choices = {'go left': 'scene002', 'go right': 'scene003', 'go home': 'terminal'}

scene = SubScene(_description, _choices)
