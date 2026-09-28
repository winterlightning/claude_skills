"""pen-50e47373: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50e47373-cb10-491f-a428-767a767f9cef'
SOURCE_PATH = 'pictographic-primitives/design/pen_50e47373-cb10-491f-a428-767a767f9cef.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Pen50e47373(Solo48):
    icon_id = 'pen-50e47373'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'state')
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        # Plan: SQUARE; diagonal symmetry, smooth rounded cap, parallel barrel, shared nib seam.
        # Reference: Lucide pencil: cap flow and exact seam contacts.
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
        self.add_line('nib-seam',(12,28),(20,36))
        self.relate('connect','nib-seam','outline')
