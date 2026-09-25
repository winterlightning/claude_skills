"Narrow Alley in Perspective.\nSymbol plan: Tall building faces frame a narrow street on the left and right, with smaller rear walls receding toward the center. A short slanted road mark reinforces the passage's depth.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit the smallest rear-wall edges to preserve the alley opening.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46)."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd5bb13bd-9b95-45b9-8d6f-dd703b261911'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/alley_d5bb13bd-9b95-45b9-8d6f-dd703b261911.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'narrow-alley-in-perspective-d5bb13bd'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('alley', 'street', 'buildings', 'perspective', 'urban', 'passage', 'city')
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
        poly('left',(8,4),(18,12),(18,32),(8,44),(8,4))
        poly('right',(40,4),(30,12),(30,32),(40,44),(40,4))
        line('rear',(18,24),(30,24))
        line('lane',(24,39),(22,44))
        self.relate('connect','left','rear');self.relate('connect','right','rear')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
