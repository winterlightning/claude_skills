"Person with Steering Wheel.\nSymbol plan: Broad curved torso with touching circular head; steering wheel keeps a single wide spoke, omitting hub and lower spoke.\nConstruction: human_ref/full_body_ref.png: circular heads and coherent limbs; Lucide object construction where relevant.\nKeyshape VRECT_L: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ebabdd4-e0a0-4c38-a81f-00e33ec2cc64'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/driver_9ebabdd4-e0a0-4c38-a81f-00e33ec2cc64.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'driver-bust-behind-circular-steering-wheel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('driver', 'person', 'steering', 'wheel', 'car', 'driving', 'bust')
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
        circle('head',24,10,6)
        arc('shoulder-left',(8,32),(16,20),8,12)
        line('shoulder-top',(16,20),(32,20))
        arc('shoulder-right',(32,20),(40,32),8,12)
        line('left',(8,44),(8,32));line('right',(40,32),(40,44))
        con('body','left','shoulder-left','shoulder-top','shoulder-right','right')
        self.relate('connect','head','body')
        circle('wheel',24,37,7)
        line('spoke',(17,37),(31,37));self.relate('connect','wheel','spoke')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
