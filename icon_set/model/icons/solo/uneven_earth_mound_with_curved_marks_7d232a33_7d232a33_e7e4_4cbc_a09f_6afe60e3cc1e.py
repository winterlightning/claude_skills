'Uneven Earth Mound with Curved Marks.\nSymbol plan: A mound of earth has a tall rounded central peak and two lower shoulders above a flat base. Short curved marks trace smaller bumps across the otherwise blank front surface.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One interior soil curve replaces multiple small marks.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d232a33-e7e4-4cbc-a09f-6afe60e3cc1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dump_7d232a33-e7e4-4cbc-a09f-6afe60e3cc1e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'uneven-earth-mound-with-curved-marks-7d232a33'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('earth', 'mound', 'soil', 'pile', 'dirt', 'ground', 'landscape')
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
        bez('mound',(4,40),((4,28),(8,23),(14,24)),((14,12),(21,8),(26,8)),((35,8),(36,22),(36,22)),((42,20),(44,29),(44,40)))
        line('base',(44,40),(4,40))
        bez('mark',(22,29),((24,24),(28,24),(30,29)))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
