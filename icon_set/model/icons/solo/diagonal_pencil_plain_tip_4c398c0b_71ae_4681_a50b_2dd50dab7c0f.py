"""Diagonal Pencil.
Plan: Diagonal barrel has a14-unit cross-section and a rounded cap; the pointed tip anchors lower-left. Ink (4,4)-(44,44).
Reference construction: pencil.
Reduction: Retain the cap seam. Keep the tip blank as in the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c398c0b-71ae-4681-a50b-2dd50dab7c0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil_4c398c0b-71ae-4681-a50b-2dd50dab7c0f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-pencil-plain-tip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('diagonal', 'pencil')
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
