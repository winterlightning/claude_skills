'Plain Slotted Piggy Bank.\nSymbol plan: A round piggy bank faces right with a short square snout and pointed ear. Two stubby feet support the body, a curled tail extends left, and a horizontal coin slot crosses the back.\nConstruction: Lucide piggy-bank: flowing pig contour, square snout and feet.\nReduction: Omit the eye to keep the small face clear.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd9a8ecf-ec10-4cd5-8df9-6f2d1088bffa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/piggy bank_dd9a8ecf-ec10-4cd5-8df9-6f2d1088bffa.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'plain-slotted-piggy-bank-dd9a8ecf'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('piggybank', 'pig', 'savings', 'coin', 'slot', 'money')
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
        bez('back',(12,16),((16,10),(25,10),(30,12)))
        poly('ear',(30,12),(36,8),(36,20),(44,20),(44,28),(38,30),(36,40),(28,40),(28,34),(20,34),(20,40),(12,40),(10,30))
        bez('rump',(10,30),((6,28),(6,20),(12,16)))
        con('pig','back',*['ear-'+str(i) for i in range(1,13)],'rump',closed=True)
        line('slot',(20,22),(25,22))
        bez('tail',(10,30),((4,30),(4,25),(4,22)))
        self.relate('connect','tail','pig')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
