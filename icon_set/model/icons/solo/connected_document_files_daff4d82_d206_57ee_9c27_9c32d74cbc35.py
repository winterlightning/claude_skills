"""Connected Document Files.
Plan: Two equal clipped-corner documents repeat vertically at a24-unit step; a broken left connector shares sheet-side junctions. Ink (6,2)-(42,46).
Reference construction: files; network.
Reduction: Omit the tiny interior fold line; the clipped corner carries the paper identity. Reduce the dashed connector to two bracket segments.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'daff4d82-d206-57ee-9c27-9c32d74cbc35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hierarchy files_daff4d82-d206-57ee-9c27-9c32d74cbc35.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'connected-document-files'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('connected', 'document', 'files')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,y in enumerate((4,28)):
         self.add_polyline(f'paper-{j}',(20,y),(32,y),(40,y+8),(40,y+16),(20,y+16),(20,y+8),closed=True)
         self.add_polyline(f'connector-{j}',(8,y+16 if j==0 else y),(8,y+8),(20,y+8))
         self.relate('connect',f'paper-{j}',f'connector-{j}')
