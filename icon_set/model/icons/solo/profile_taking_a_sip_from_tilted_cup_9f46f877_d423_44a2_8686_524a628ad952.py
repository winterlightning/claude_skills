"Profile Taking a Sip from Tilted Cup.\nSymbol plan: A person's head and upper torso face right, with a small tilted cup positioned just in front of the mouth. The nose, chin, neck and sloping shoulder form a continuous plain profile.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Profile head has a continuous neck rather than a detached stick head.\nReduction: Keep the profile and a broad open cup; omit the cup’s narrow tilted rim.\nKeyshape SQUARE."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9f46f877-d423-44a2-8686-524a628ad952'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sip_9f46f877-d423-44a2-8686-524a628ad952.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'profile-taking-a-sip-from-tilted-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('sip', 'drink', 'cup', 'person', 'profile', 'mouth')
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
        bez('back',(6,42),((6,30),(14,30),(12,24)),((2,6),(14,6),(18,6)),((28,6),(28,14),(24,18)))
        poly('face',(24,18),(26,24),(22,24),(22,30),(18,30),(22,34),(26,42))
        poly('cup',(34,24),(34,36),(42,36),(42,24))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
