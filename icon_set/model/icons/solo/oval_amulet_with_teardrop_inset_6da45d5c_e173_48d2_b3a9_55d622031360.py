"Oval Amulet with Teardrop Inset.\nSymbol plan: An upright oval pendant hangs beneath a small round suspension loop. A pointed teardrop-shaped inset occupies the center, with its rounded base following the outer pendant's lower curve.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape VRECT_L."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6da45d5c-e173-48d2-b3a9-55d622031360'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amulet_6da45d5c-e173-48d2-b3a9-55d622031360.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'oval-amulet-with-teardrop-inset'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('amulet', 'pendant', 'jewelry', 'teardrop', 'oval', 'loop', 'necklace')
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
        circle('loop',24,6,2)
        line('link',(24,8),(24,18))
        arc('outer-a',(8,31),(40,31),16,13);arc('outer-b',(40,31),(8,31),16,13);con('pendant','outer-a','outer-b',closed=True)
        bez('drop',(24,27),((34,33),(29,35),(24,35)),((19,35),(14,33),(24,27)))
        self.relate('connect','loop','link');self.relate('connect','link','pendant')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
