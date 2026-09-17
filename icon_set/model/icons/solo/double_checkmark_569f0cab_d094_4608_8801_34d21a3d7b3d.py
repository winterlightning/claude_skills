"""Double Checkmark.
Plan: Two checkmarks repeat with fourteen-unit vertical offset and matching diagonal angles. Ink (4,4)-(44,44).
Reference construction: check-check.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '569f0cab-d094-4608-8801-34d21a3d7b3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/check double_569f0cab-d094-4608-8801-34d21a3d7b3d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'double-checkmark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('double', 'checkmark')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('upper',(6,18),(16,28),(38,6))
        self.add_polyline('lower',(6,32),(16,42),(42,16))
