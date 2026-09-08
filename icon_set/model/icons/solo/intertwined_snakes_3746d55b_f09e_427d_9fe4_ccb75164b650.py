"""Two serpents weave around each other. Extremes (2,2)-(46,46). No useful local Lucide match; single-stroke bodies and a shared central knot replace outline detail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3746d55b-f09e-427d-9fe4-ccb75164b650'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/snakes_3746d55b-f09e-427d-9fe4-ccb75164b650.svg'

class IntertwinedSnakes(Solo48):
    icon_id = 'intertwined-snakes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('snake', 'serpent', 'intertwined', 'caduceus', 'mythology', 'coil', 'reptile', 'symbol')

    def build(self) -> None:
        self.add_line('head-a-1', (18, 8), (20, 2))
        self.add_line('head-a-2', (20, 2), (14, 2))
        self.add_arc('upper-a-outer',(14,2),(2,12),radius_x=12,radius_y=10,sweep=False)
        self.add_arc('upper-a-inner',(2,12),(12,20),radius_x=10,radius_y=8,sweep=False)
        self.add_line('cross-a-upper',(12,20),(24,24))
        self.add_line('cross-a-lower',(24,24),(36,28))
        self.add_arc('lower-a-inner',(36,28),(46,36),radius_x=10,radius_y=8)
        self.add_arc('tail-a',(46,36),(34,46),radius_x=12,radius_y=10)
        self.add_contour('snake-a','head-a-1','head-a-2','upper-a-outer','upper-a-inner','cross-a-upper','cross-a-lower','lower-a-inner','tail-a')
        self.add_arc('tail-b',(34,2),(46,12),radius_x=12,radius_y=10)
        self.add_arc('upper-b-inner',(46,12),(36,20),radius_x=10,radius_y=8)
        self.add_line('cross-b-upper',(36,20),(24,24))
        self.add_line('cross-b-lower',(24,24),(12,28))
        self.add_arc('lower-b-inner',(12,28),(2,36),radius_x=10,radius_y=8,sweep=False)
        self.add_arc('lower-b-outer',(2,36),(14,46),radius_x=12,radius_y=10,sweep=False)
        self.add_line('head-b-1', (14, 46), (20, 46))
        self.add_line('head-b-2', (20, 46), (18, 40))
        self.add_contour('snake-b','tail-b','upper-b-inner','cross-b-upper','cross-b-lower','lower-b-inner','lower-b-outer','head-b-1','head-b-2')
        # The two bodies genuinely touch at the shared central knot (24,24).
        self.relate('connect','snake-a','snake-b')
