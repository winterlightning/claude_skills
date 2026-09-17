"""Arrows toward Horizontal Divider.
Plan: Two arrows reflected across y24 stop 8 units from the divider; ink (4,4)-(44,44).
Reference construction: move.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f5c496b-ab35-40d2-bfdd-dcb1ed4f047d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/shrink vertical_6f5c496b-ab35-40d2-bfdd-dcb1ed4f047d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'arrows-toward-horizontal-divider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('arrows', 'toward', 'horizontal', 'divider')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('divider',(6,24),(42,24))
        for label,sgn in [('upper',-1),('lower',1)]:
            tip=(24,24+sgn*8)
            self.add_line(label+'-shaft',(24,24+sgn*18),tip)
            self.add_polyline(label+'-head',(18,24+sgn*14),tip,(30,24+sgn*14))
            self.relate('connect',label+'-shaft',label+'-head')
