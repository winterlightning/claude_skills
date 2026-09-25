"""pen-4d7410cc: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d7410cc-8df1-40ed-b2e1-f198d65f3a13'
SOURCE_PATH = 'pictographic-primitives/design/pen_4d7410cc-8df1-40ed-b2e1-f198d65f3a13.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Pen4d7410cc(Solo48):
    icon_id = 'pen-4d7410cc'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        # Plan: SQUARE (6,6)-(42,42); tangent rounded cap, parallel diagonal barrel and seam ending exactly on its sides.
        # Reference: Lucide pencil: coherent rounded cap and one shared seam.
        # The cap and the barrel mirror across the diagonal x+y=48.
        self.add_line('upper-barrel',(12,28),(30,10))
        self.add_bezier('cap-upper',(30,10),((32,8),(33,6),(36,6)))
        self.add_arc('cap-round',(36,6),(42,12),radius_x=6)
        self.add_bezier('cap-lower',(42,12),((42,15),(40,16),(38,18)))
        self.add_line('lower-barrel',(38,18),(20,36))
        self.add_line('tip-lower',(20,36),(6,42))
        self.add_line('tip-upper',(6,42),(12,28))
        self.add_contour('outline','upper-barrel','cap-upper','cap-round','cap-lower','lower-barrel','tip-lower','tip-upper',closed=True)
        self.add_line('cap-seam',(26,14),(34,22))
        self.relate('connect','cap-seam','outline')
