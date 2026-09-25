'Paper Sheet with Fold Guides.\nSymbol plan: An upright sheet has rounded lower corners and a diagonally clipped upper right corner. A dashed horizontal fold guide crosses its middle, meeting a shorter dashed vertical guide descending from the top.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Use broad separated fold dashes.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ff94890-14ba-4521-b4c3-5283d40ef0d6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paper sizes folding dash_0ff94890-14ba-4521-b4c3-5283d40ef0d6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'paper-sheet-fold-guides-0ff94890'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('paper', 'sheet', 'fold', 'guides', 'dashed', 'document')
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
        poly('page',(8,4),(30,4),(40,14),(40,40),(36,44),(12,44),(8,40),(8,4))
        for i,(a,b) in enumerate([((8,28),(16,28)),((24,28),(32,28)),((24,12),(24,18))]):line('guide'+str(i),a,b)
        self.relate('connect','page','guide0')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
