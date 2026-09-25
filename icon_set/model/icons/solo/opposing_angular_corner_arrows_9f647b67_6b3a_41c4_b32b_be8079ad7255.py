"""AMD Brand Arrow Symbol.

Plan: Two opposed angular corner shapes, one large upper-right and smaller lower-left. Envelope 6,6–42,42.
Construction reference: plane (local original and atomic-debug inspected).
Simplification: Sharp stepped corners retained as identity features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f647b67-6b3a-41c4-b32b-be8079ad7255'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amd logo_9f647b67-6b3a-41c4-b32b-be8079ad7255.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'opposing-angular-corner-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('amd', 'brand', 'arrow', 'symbol')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'; members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        self.add_polyline('upper',(6,6),(42,6),(42,42),(32,32),(32,16),(16,16),closed=True)
        self.add_polyline('lower',(6,33),(14,25),(14,34),(24,34),(16,42),(6,42),closed=True)
