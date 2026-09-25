"Overlapping Square and Circle.\nSymbol plan: A rounded square sits above and to the left of a larger circle. Their complete outlines overlap across the square's lower right corner, leaving both interiors empty.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape SQUARE."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '501a1af2-eada-4b51-ab88-42eb6c350817'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/byte logo_501a1af2-eada-4b51-ab88-42eb6c350817.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'overlapping-square-and-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('square', 'circle', 'overlap', 'geometry', 'shapes', 'outline', 'pair')
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
        rect('square',6,6,24,24,3)
        circle('circle',28,28,14)
        self.relate('connect','circle','square')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
