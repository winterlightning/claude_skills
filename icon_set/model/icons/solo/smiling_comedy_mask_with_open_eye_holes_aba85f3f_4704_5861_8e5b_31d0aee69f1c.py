"""Smiling Theater Comedy Mask.
Plan: A dipped mask rim owns two circular open eye holes and a smile; mirror on x=24. Centerline extremes (6,6)-(42,42).
Reference: No useful Lucide mask match; circular construction and mirrored facial layout.
Reduction: Domed eyes reduced to circular open holes for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba85f3f-4704-5861-8e5b-31d0aee69f1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/funny mask_aba85f3f-4704-5861-8e5b-31d0aee69f1c.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'smiling-comedy-mask-with-open-eye-holes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/entertainment"
    aliases = ()
    keywords = ('smiling', 'theater', 'comedy', 'mask')

    def build(self):

        self.add_arc('rim',(6,6),(42,6),radius_x=30,radius_y=8,sweep=False)
        self.add_line('right',(42,6),(42,24))
        self.add_arc('chin',(42,24),(6,24),radius_x=18,sweep=True)
        self.add_line('left',(6,24),(6,6))
        for a,b in (('rim','right'),('right','chin'),('chin','left'),('left','rim')):
            self.relate('connect',a,b)
        for i,x in enumerate((17,31)):
            self.add_arc(f'eye-{i}-a',(x-3,19),(x+3,19),radius_x=3)
            self.add_arc(f'eye-{i}-b',(x+3,19),(x-3,19),radius_x=3)
            self.add_contour(f'eye-{i}',f'eye-{i}-a',f'eye-{i}-b',closed=True)
        self.add_arc('smile',(17,31),(31,31),radius_x=9,radius_y=3,sweep=False)
