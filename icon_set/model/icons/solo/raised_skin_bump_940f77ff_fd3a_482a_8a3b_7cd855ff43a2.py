"Pimple on Skin Layer.\nSymbol plan: Skin bump and spot retained as two clear elements.\nConstruction: Lucide original and atomic-debug: bath, truck, notebook, piano, orbit, sprout and pill-bottle; coherent arcs, shared joins and repeated dimensions.\nKeyshape HRECT_M: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '940f77ff-fd3a-482a-8a3b-7cd855ff43a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pimple_940f77ff-fd3a-482a-8a3b-7cd855ff43a2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'raised-skin-bump'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('pimple', 'skin', 'bump', 'spot', 'anatomy', 'dermatology')
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
        bez('skin',(4,38),((12,38),(12,10),(24,10)),((36,10),(36,38),(44,38)))
        circle('spot',24,28,4)

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
