'Three Overlapping Mozzarella Slices.\nSymbol plan: Three rounded mozzarella slices overlap in a diagonal stack, with the nearest slice lower and farther left. Their smooth blank faces and curved edges create a layered arrangement without interior marks.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '600abb76-55a0-48a0-9c01-0a94b6498aa6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mozzarella_600abb76-55a0-48a0-9c01-0a94b6498aa6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'three-overlapping-mozzarella-slices-600abb76'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('mozzarella', 'cheese', 'slices', 'food', 'dairy', 'round', 'stack')
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
        rect('slice-front',6,22,20,20,6)
        poly('middle-top',(14,22),(14,18));arc('middle-corner',(14,18),(18,14),4)
        line('middle-edge',(18,14),(30,14));arc('middle-round',(30,14),(34,18),4)
        poly('middle-side',(34,18),(34,30),(26,30))
        poly('back-top',(22,14),(22,10));arc('back-corner',(22,10),(26,6),4)
        line('back-edge',(26,6),(38,6));arc('back-round',(38,6),(42,10),4)
        poly('back-side',(42,10),(42,22),(34,22))
        self.relate('connect','slice-front','middle-top');self.relate('connect','slice-front','middle-side');self.relate('connect','back-top','middle-edge');self.relate('connect','back-side','middle-side')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
