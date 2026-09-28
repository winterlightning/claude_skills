'Right Facing Human Profile.\nSymbol plan: A human bust faces right with a rounded skull, small projecting nose and short flat chin. A long straight neck descends beside a single curved shoulder at the left.\nConstruction: human_ref/user.svg: smooth shoulder and circular skull vocabulary.\nReduction: Continuous neck, no detached head.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81b8e41d-b09d-4c1f-8f67-d8dbdac1f6ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/body skeleton_81b8e41d-b09d-4c1f-8f67-d8dbdac1f6ff.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'right-facing-human-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('person', 'profile', 'head', 'bust', 'human', 'portrait', 'face')
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
        arc('skull-left',(24,28),(24,4),12)
        arc('skull-top',(24,4),(36,16),12)
        poly('face',(36,16),(40,22),(34,24),(34,32),(28,32))
        line('neck',(24,28),(24,44))
        bez('shoulder',(8,44),((8,40),(14,38),(24,38)))
        con('profile','skull-left','skull-top',*['face-'+str(i) for i in range(1,5)])
        self.relate('connect','shoulder','neck')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
