"""Diagonal Writing Pencil.
Plan: Broad diagonal barrel joins a rounded cap and an unmarked lower-left point. Ink (4,4)-(44,44).
Reference construction: pencil.
Reduction: Retain the cap seam and blank angular tip; regularize the source contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af6d609a-560f-4248-a671-cfb36522af0d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil_af6d609a-560f-4248-a671-cfb36522af0d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-writing-pencil-rounded-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('diagonal', 'writing', 'pencil')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('tip-left',(6,42),(10,28))
        self.add_line('barrel-left',(10,28),(26,12))
        self.add_line('cap-left',(26,12),(30,8))
        self.add_bezier('cap-top',(30,8),((32,6),(33,6),(34,6)))
        self.add_bezier('cap-turn',(34,6),((36,6),(42,12),(42,14)))
        self.add_bezier('cap-right',(42,14),((42,15),(42,16),(40,18)))
        self.add_line('cap-end',(40,18),(36,22))
        self.add_line('barrel-right',(36,22),(20,38))
        self.add_line('tip-right',(20,38),(6,42))
        self.add_contour('pencil','tip-left','barrel-left','cap-left','cap-top','cap-turn','cap-right','cap-end','barrel-right','tip-right',closed=True)
        self.add_line('cap-seam',(26,12),(36,22));self.relate('connect','cap-seam','pencil')
