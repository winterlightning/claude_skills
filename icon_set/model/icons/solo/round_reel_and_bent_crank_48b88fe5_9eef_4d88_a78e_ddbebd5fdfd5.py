'Round Reel and Bent Crank.\nSymbol plan: A circular reel surrounds a smaller circular opening, with a short vertical grip beneath it. A horizontal crank projects rightward and bends up into a rounded end, with a thin line dropping from the bend.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Crank end reduced to an open bent grip; no separate thin fishing line.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48b88fe5-9eef-4d88-a78e-ddbebd5fdfd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/reel_48b88fe5-9eef-4d88-a78e-ddbebd5fdfd5.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'round-reel-and-bent-crank'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('reel', 'spool', 'fishing', 'crank', 'handle', 'tackle')
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
        circle('reel',20,20,14);circle('hole',20,20,5)
        poly('grip',(16,34),(16,42),(24,42),(24,34))
        poly('crank',(34,26),(42,26),(42,18))
        self.relate('connect','reel','grip');self.relate('connect','reel','crank')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
