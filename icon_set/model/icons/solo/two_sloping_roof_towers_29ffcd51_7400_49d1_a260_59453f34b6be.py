'Two Sloping Roof Towers.\nSymbol plan: Two narrow towers stand side by side with rooflines sloping in opposite directions. Short horizontal window bands and small ground level doors mark each building, with a mast on the taller one.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit tiny door openings and mast to retain two separate sloping towers.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '29ffcd51-7400-49d1-a260-59453f34b6be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/buildings modern_29ffcd51-7400-49d1-a260-59453f34b6be.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'two-sloping-roof-towers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('towers', 'buildings', 'city', 'architecture', 'skyscrapers', 'windows', 'urban')
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
        poly('left',(6,42),(6,14),(22,6),(22,42),(6,42))
        poly('right',(30,42),(30,18),(42,24),(42,42),(30,42))
        line('window-left',(14,22),(22,22));line('window-right',(30,32),(42,32))
        self.relate('connect','left','window-left');self.relate('connect','right','window-right')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
