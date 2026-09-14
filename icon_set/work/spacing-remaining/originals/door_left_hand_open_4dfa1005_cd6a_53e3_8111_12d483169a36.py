'Open door: straight perspective edges, a balanced leaf and a clear handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dfa1005-cd6a-53e3-8111-12d483169a36'
SOURCE_PATH = 'icons-json/building/door left hand open_4dfa1005-cd6a-53e3-8111-12d483169a36.json'
AUTHOR = 'gpt-6'

class DoorLeftHandOpen(Solo48):
    icon_id = 'door-left-hand-open'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'left', 'hand', 'open', 'building')

    def build(self):
        # Open door: straight perspective edges, a balanced leaf and a clear handle.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('frame',(8,44),(8,4),(40,4),(40,44))
        p('leaf',(40,4),(20,12),(20,36),(40,44))
        link('connect','frame','leaf')
        self.add_dot('knob',(30,25))
