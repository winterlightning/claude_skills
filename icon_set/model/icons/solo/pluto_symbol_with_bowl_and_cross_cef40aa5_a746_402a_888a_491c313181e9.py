"Pluto Astrology Symbol.\nSymbol plan: Astrological pictogram retained as a circle, bowl and cross; this is not letter/number typography.\nConstruction: Lucide original and atomic-debug: bath, truck, notebook, piano, orbit, sprout and pill-bottle; coherent arcs, shared joins and repeated dimensions.\nKeyshape VRECT_L: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cef40aa5-a746-402a-888a-491c313181e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astrology pluto_cef40aa5-a746-402a-888a-491c313181e9.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'pluto-symbol-with-bowl-and-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('pluto', 'astrology', 'symbol', 'circle', 'bowl', 'cross', 'celestial')
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
        circle('disk',24,11,7)
        arc('bowl-left',(8,12),(24,28),16,s=False);arc('bowl-right',(24,28),(40,12),16,s=False)
        line('stem',(24,28),(24,44));line('cross',(16,36),(32,36));self.relate('connect','stem','cross')

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
