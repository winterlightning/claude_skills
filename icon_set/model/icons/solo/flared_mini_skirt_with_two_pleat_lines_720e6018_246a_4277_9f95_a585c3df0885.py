"""A-Line Mini Skirt.

Plan: Mirrored flared skirt, waistband and two hem-connected pleats; envelope 4,8–44,40.
Construction reference: shirt (local original and atomic-debug inspected).
Simplification: Hem curvature simplified to a straight hem; two pleats retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '720e6018-246a-4277-9f95-a585c3df0885'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mini skirt_720e6018-246a-4277-9f95-a585c3df0885.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'flared-mini-skirt-with-two-pleat-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('a-line', 'mini', 'skirt')

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

        axis=24
        self.add_polyline('outline',(14,8),(34,8),(36,16),(44,40),(32,40),(16,40),(4,40),(12,16),closed=True)
        self.add_line('waistband',(12,16),(36,16))
        self.relate('connect','outline','waistband')
        for side in (-1,1):
            self.add_line(f'pleat-{side}',(axis+side*6,26),(axis+side*8,40))
            self.relate('connect','outline',f'pleat-{side}')
