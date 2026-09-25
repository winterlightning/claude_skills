"Person Seated at a Straight Desk.\nSymbol plan: A round-headed person sits behind a long horizontal tabletop with one bent arm resting on it. A curved seated thigh and downward-bent lower leg are visible between the table's two straight legs.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance.\nReduction: One bent leg and resting forearm preserve the seated desk scene.\nKeyshape SQUARE."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ad53d4fb-d2b8-4581-825c-e6a0af28bebb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bandage rehab_ad53d4fb-d2b8-4581-825c-e6a0af28bebb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-seated-at-a-straight-desk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('person', 'desk', 'seated', 'table', 'work', 'chair', 'posture')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        circle('head',20,10,4);line('torso',(20,22),(20,38));poly('arm',(20,22),(34,22),(34,30));poly('leg',(20,38),(30,38),(28,42))
        poly('desk',(6,42),(6,30),(42,30),(42,42));self.relate('connect','arm','desk');self.relate('connect','torso','desk');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
