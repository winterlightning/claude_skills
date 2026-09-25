"""Folded Document Download Arrow.
Plan: One continuous silhouette merges the clipped paper corner and broad downward arrow; the fold shares corner endpoints. Ink (6,2)-(42,46).
Reference construction: file-down.
Reduction: Enlarge the corner fold to a14-unit triangle so its opening passes the hole check; keep the fused document/arrow silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0261277-89ce-4117-bdab-3bf358c0f202'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation down 3_b0261277-89ce-4117-bdab-3bf358c0f202.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'folded-document-download-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('folded', 'document', 'download', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('document-arrow',(14,4),(22,4),(36,18),(36,28),(40,28),(24,44),(8,28),(14,28),closed=True)
        self.add_polyline('fold',(22,4),(22,18),(36,18));self.relate('connect','fold','document-arrow')
