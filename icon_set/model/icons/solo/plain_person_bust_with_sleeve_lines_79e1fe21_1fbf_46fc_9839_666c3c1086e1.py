"Person User Avatar.\nSymbol plan: Open base and omitted short sleeve seams keep the broad reference shoulders clear. Touching head/body ink.\nConstruction: human_ref/user.svg and Lucide user-round original/atomic-debug: circular head, rounded shoulders, open base.\nKeyshape VRECT_L: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79e1fe21-1fbf-46fc-9839-666c3c1086e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/servant_79e1fe21-1fbf-46fc-9839-666c3c1086e1.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'plain-person-bust-with-sleeve-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "objects/reference"
    aliases = ()
    keywords = ('person', 'bust', 'torso', 'head', 'figure', 'portrait')
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
        circle('head',24,13,9)
        arc('shoulders',(8,42),(40,42),16)
        line('side-left',(8,44),(8,42));line('side-right',(40,42),(40,44))
        con('body','side-left','shoulders','side-right')
        self.relate('connect','head','body')

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
