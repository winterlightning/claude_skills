'Pearl in Open Oyster.\nSymbol plan: A broad open oyster shell has a scalloped upper edge and tapered lower sides. A large round pearl sits in its center, above a shallow curved lower shell lip at the base.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Broad scallops and a clear pearl replace tiny shell ridges.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6be5a48-0fa5-4a95-b514-e21e2dbc9e98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/oyster_d6be5a48-0fa5-4a95-b514-e21e2dbc9e98.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'pearl-open-oyster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('oyster', 'pearl', 'shell', 'seafood', 'marine', 'mollusk')
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
        bez('shell',(12,34),((12,28),(6,24),(6,20)),((6,15),(10,14),(10,14)),((10,8),(17,8),(18,8)),((22,5.333333333333333),(26,5.333333333333333),(30,8)),((38,8),(38,12),(38,14)),((42,14),(42,17),(42,20)),((42,24),(36,28),(36,34)))
        circle('pearl',24,24,5)
        bez('lip',(12,34),((6,38),(14,42),(24,42)),((34,42),(42,38),(36,34)))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
