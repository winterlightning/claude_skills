"""Diagonal Double Headed Arrow.
Plan: Single diagonal shaft joins opposing right-angle heads at exact endpoints. Ink (4,4)-(44,44).
Reference construction: move-diagonal.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1949af7-d5b2-49c0-837f-e872db7e64d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand diagonal_a1949af7-d5b2-49c0-837f-e872db7e64d5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-double-headed-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('diagonal', 'double', 'headed', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('shaft',(6,42),(42,6))
        self.add_polyline('upper',(28,6),(42,6),(42,20))
        self.add_polyline('lower',(6,28),(6,42),(20,42))
        self.relate('connect','shaft','upper');self.relate('connect','shaft','lower')
