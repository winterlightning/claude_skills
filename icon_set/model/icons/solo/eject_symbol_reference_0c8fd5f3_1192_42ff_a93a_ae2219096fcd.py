"""Eject Symbol.
Plan: An upward triangle sits eight units above a full-width rectangular eject bar. Ink (4,4)-(44,44).
Reference construction: eject.
Reduction: Regularize the triangle and bar while retaining both outlined forms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0c8fd5f3-1192-42ff-a93a-ae2219096fcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/keyboard eject_0c8fd5f3-1192-42ff-a93a-ae2219096fcd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'eject-symbol-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('eject', 'symbol')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('triangle',(24,6),(40,26),(8,26),closed=True)
        self.add_polyline('bar',(6,34),(42,34),(42,42),(6,42),closed=True)
