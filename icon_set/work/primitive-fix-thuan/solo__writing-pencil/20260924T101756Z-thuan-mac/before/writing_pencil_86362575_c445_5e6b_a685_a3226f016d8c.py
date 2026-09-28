"""Writing Pencil.

Symbol plan: Diagonal barrel with a circular rounded end, shared tip seam. Centerline extremes (6,6)-(42,42); deliberate down-left direction.
References: original SOURCE_PATH; Lucide pencil/gavel/hat-glasses for coherent
outlines and shared attachment nodes; human_ref/user.svg for circular heads
and rounded shoulders. Omit tiny decorative face, emblem and robe marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86362575-c445-5e6b-a685-a3226f016d8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/content pen_86362575-c445-5e6b-a685-a3226f016d8c.svg'
AUTHOR = 'gpt-6'

class WritingPencil(Solo48):
    icon_id = 'writing-pencil'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/content"
    aliases = ()
    keywords = ('writing', 'pencil')

    def build(self):
        self.add_line('barrel-left',(10,20),(26,8))
        self.add_arc('cap',(26,8),(38,24),radius_x=10)
        self.add_line('barrel-right',(38,24),(22,36))
        self.add_line('tip-right',(22,36),(6,42))
        self.add_line('tip-left',(6,42),(10,20))
        self.add_contour('outline','barrel-left','cap','barrel-right','tip-right','tip-left',closed=True)
        self.add_line('tip-seam',(10,20),(22,36))
        self.relate('connect','outline','tip-seam')
