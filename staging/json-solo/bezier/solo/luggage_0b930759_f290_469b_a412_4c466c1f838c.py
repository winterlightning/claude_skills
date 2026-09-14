"""Luggage (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = 'icons-json/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.json'
AUTHOR = 'json_to_solo'

class LuggageState(Solo48):
    icon_id = 'luggage-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('luggage', 'state')

    def build(self):
        self.add_line('e0', (19, 10), (19, 5))
        self.add_line('e1', (21, 4), (28, 4))
        self.add_line('e2', (29, 5), (29, 10))
        self.add_line('e3', (11, 40), (11, 44))
        self.add_line('e4', (37, 40), (37, 44))
        self.add_line('e5', (37, 40), (11, 40))
        self.add_line('e6', (8, 38), (8, 13))
        self.add_line('e7', (12, 10), (36, 10))
        self.add_line('e8', (40, 13), (40, 38))
        self.add_bezier('e9', (19, 5), ((19.56, 4.573), (19.95, 4.009), (20.78, 4.009)), ((20.85, 4.009), (20.93, 4), (21, 4)))
        self.add_bezier('e10', (28, 4), ((28.13, 4.091), (28.33, 4.091), (28.48, 4.182)), ((28.79, 4.382), (28.81, 4.755), (29, 5)))
        self.add_bezier('e11', (11, 40), ((9.73, 39.555), (8, 39.482), (8, 38)))
        self.add_bezier('e12', (8, 13), ((8.01, 12.964), (8.01, 13.027), (8.02, 12.991)), ((8.02, 11.509), (10.63, 10), (12, 10)))
        self.add_bezier('e13', (36, 10), ((37.63, 10), (40, 11.291), (40, 13)))
        self.add_bezier('e14', (40, 38), ((40, 39.409), (38.17, 39.5), (37, 40)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e11', 'e6', 'e12', 'e7', 'e13', 'e8', 'e14', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
