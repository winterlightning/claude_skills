"""Continuous left-facing profile and neck within integrated scan boundary; deliberate asymmetry follows face direction. Bounds (6,6)-(42,42).
Construction reference: ear; shared human_ref/user.svg (anatomical vocabulary; continuous profile has no detached head).
Reduction: Ear omitted to preserve clearance within the scanned head silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b97885e6-dbf9-5160-931c-e559629ea220'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg'
SAVED_BRIEF_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/artificial-intelligence/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'human-head-side-profile-scan-batch-001-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/anatomy'
    aliases = ()
    keywords = ('human', 'head', 'side', 'profile', 'scan')
    def build(self):
        self.add_polyline('scan',(24,6),(10,6),(6,6),(6,42),(22,42))
        self.add_arc('crown',(24,6),(42,24),radius_x=18)
        self.add_polyline('neck',(42,24),(36,34),(38,42))
        self.relate('connect','scan','crown'); self.relate('connect','crown','neck')
        self.add_arc('forehead',(28,14),(16,26),radius_x=12,sweep=False)
        self.add_polyline('face',(16,26),(12,32),(20,32),(20,36),(22,42))
        self.relate('connect','forehead','face'); self.relate('connect','face','scan')

    def rect(self, name, l, t, r, b, radius=4, top=(), bottom=()):
        # One rounded rectangle owns matching corner radii and attachment nodes.
        pts=[(l+radius,t),*[(x,t) for x in sorted(top)],(r-radius,t),(r,t+radius),(r,b-radius),(r-radius,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for j,(p,q) in enumerate(zip(pts,pts[1:]+pts[:1])):
            n=f'{name}-{j}'; members.append(n)
            if p[0]!=q[0] and p[1]!=q[1]: self.add_arc(n,p,q,radius_x=radius)
            else: self.add_line(n,p,q)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

