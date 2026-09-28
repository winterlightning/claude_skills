'Six-Window Apartment Building.\nSymbol plan: A flat-fronted rectangular building has six square windows arranged in two rows of three. A central doorway opens at ground level, and a small rectangular rooftop block rises above the left side.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Six windows become a clear six-dot grid; doorway retained.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8600fbaf-53f0-4953-a198-299f02e70c9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/apartment_8600fbaf-53f0-4953-a198-299f02e70c9e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'six-window-apartment-building-8600fbaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('apartment', 'building', 'windows', 'door', 'architecture', 'residential', 'city')
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
        rect('building',6,14,36,28)
        poly('roof',(10,14),(10,6),(20,6),(20,14))
        for j,y in enumerate((22,30)):
         for i,x in enumerate((14,24,34)):self.add_dot('window'+str(j)+str(i),(x,y))
        line('door',(24,42),(24,38))
        self.relate('connect','building','roof');self.relate('connect','building','door')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
