'Single Eyed Rounded Creature Head.\nSymbol plan: A rounded upright creature head has a domed top, straight sides, and small semicircular ears. One large almond shaped eye with a round pupil sits centrally across the otherwise blank face.\nConstruction: Lucide eye: centered pupil and broad eye opening.\nReduction: Retain a single circular eye; omit its small pupil.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1996e073-b2d3-410a-8ad7-171410fe3cdd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/cyclops_1996e073-b2d3-410a-8ad7-171410fe3cdd.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'single-eyed-rounded-creature-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('cyclops', 'creature', 'eye', 'head', 'ears', 'monster', 'face')
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
        arc('crown',(10,20),(38,20),14)
        arc('ear-right',(38,20),(38,28),4)
        line('right',(38,28),(38,30));arc('jaw',(38,30),(10,30),14,12)
        line('left',(10,30),(10,28));arc('ear-left',(10,28),(10,20),4)
        con('head','crown','ear-right','right','jaw','left','ear-left',closed=True)
        circle('eye',24,24,5)
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
