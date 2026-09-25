'Seder Plate beside Matzah.\nSymbol plan: A large round plate with several small circular food portions sits behind a square piece of matzah. Short broken horizontal lines cross the matzah, which overlaps the plate at the lower right.\nConstruction: Reference-specific coherent contours; no useful exact Lucide match.\nReduction: Three food portions and a central perforation mark retain the plate and matzah.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b4fe5f3-6380-4a59-98dc-f653a3972764'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pesach passover 1_5b4fe5f3-6380-4a59-98dc-f653a3972764.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'seder-plate-matzah'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('seder', 'matzah', 'plate', 'passover', 'food', 'meal')
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
        arc('plate-top',(6,24),(42,24),18);arc('plate-left',(24,42),(6,24),18)
        rect('matzah',24,24,18,18)
        for n,x,y in [('a',18,18),('b',29,16),('c',16,29)]:self.add_dot(n,(x,y))
        self.add_dot('holes',(33,33))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
