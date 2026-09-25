'Open door: straight perspective edges, a balanced leaf and a clear handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed7f90b7-559a-4f11-8523-8dc4daea49e1'
SOURCE_PATH = 'pictographic-primitives/furnitures/door_ed7f90b7-559a-4f11-8523-8dc4daea49e1.svg'
AUTHOR = 'gpt-6'

class Door(Solo48):
    icon_id = 'door'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'state')
    aliases = ()
    keywords = ('door', 'furnitures')

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
