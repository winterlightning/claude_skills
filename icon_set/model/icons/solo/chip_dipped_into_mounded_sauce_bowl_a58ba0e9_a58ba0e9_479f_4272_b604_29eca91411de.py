'Chip Dipped into Mounded Sauce Bowl.\nSymbol plan: A broad bowl contains a rounded mound of dip rising above its straight rim. A single tilted chip enters from the upper right, with its lower corner touching the dip near the rim.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a58ba0e9-479f-4272-b604-29eca91411de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dip_a58ba0e9-479f-4272-b604-29eca91411de.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'chip-dipped-into-mounded-sauce-bowl-a58ba0e9'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('dip', 'chip', 'bowl', 'sauce', 'nacho', 'food', 'snack')
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
        line('rim',(4,26),(44,26))
        bez('bowl',(44,26),((40,40),(35,40),(24,40)),((13,40),(8,40),(4,26)))
        bez('dip',(6,26),((8,16),(17,15),(26,18)))
        poly('chip',(24,26),(30,8),(42,12),(38,26))
        self.relate('connect','dip','rim');self.relate('connect','dip','chip');self.relate('connect','chip','rim')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
