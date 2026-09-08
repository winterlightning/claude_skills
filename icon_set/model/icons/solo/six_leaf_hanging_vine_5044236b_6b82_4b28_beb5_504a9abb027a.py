"""Six alternating pointed leaves on a hanging vertical vine; leaf veins omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5044236b-6b82-4b28-beb5-504a9abb027a'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 4_5044236b-6b82-4b28-beb5-504a9abb027a.svg'
AUTHOR = 'gpt-6'

class SixLeafHangingVine(Solo48):
    icon_id = 'six-leaf-hanging-vine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vine', 'hanging', 'leaves', 'stem', 'foliage', 'plant', 'botanical')

    def build(self) -> None:
        # VRECT_L: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_line('stem', (24, 2), (24, 46))
        self.add_arc('leaf-0a', (24, 7), (40, 7), radius_x=10, radius_y=9, sweep=True)
        self.add_arc('leaf-0b', (40, 7), (24, 7), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('leaf-0', 'leaf-0a', 'leaf-0b', closed=True)
        self.relate('connect', 'leaf-0', 'stem')
        self.add_arc('leaf-1a', (24, 14), (8, 14), radius_x=10, radius_y=9, sweep=True)
        self.add_arc('leaf-1b', (8, 14), (24, 14), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('leaf-1', 'leaf-1a', 'leaf-1b', closed=True)
        self.relate('connect', 'leaf-1', 'stem')
        self.add_arc('leaf-2a', (24, 21), (40, 21), radius_x=10, radius_y=9, sweep=True)
        self.add_arc('leaf-2b', (40, 21), (24, 21), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('leaf-2', 'leaf-2a', 'leaf-2b', closed=True)
        self.relate('connect', 'leaf-2', 'stem')
        self.add_arc('leaf-3a', (24, 28), (8, 28), radius_x=10, radius_y=9, sweep=True)
        self.add_arc('leaf-3b', (8, 28), (24, 28), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('leaf-3', 'leaf-3a', 'leaf-3b', closed=True)
        self.relate('connect', 'leaf-3', 'stem')
        self.add_arc('leaf-4a', (24, 35), (40, 35), radius_x=10, radius_y=9, sweep=True)
        self.add_arc('leaf-4b', (40, 35), (24, 35), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('leaf-4', 'leaf-4a', 'leaf-4b', closed=True)
        self.relate('connect', 'leaf-4', 'stem')
        self.add_arc('leaf-5a', (24, 42), (8, 42), radius_x=10, radius_y=9, sweep=True)
        self.add_arc('leaf-5b', (8, 42), (24, 42), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('leaf-5', 'leaf-5a', 'leaf-5b', closed=True)
        self.relate('connect', 'leaf-5', 'stem')
