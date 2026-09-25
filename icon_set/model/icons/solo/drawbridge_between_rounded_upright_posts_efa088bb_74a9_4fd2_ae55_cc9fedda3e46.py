"Drawbridge Between Rounded Upright Posts.\nSymbol plan: Two tall rounded posts flank a narrow horizontal bridge deck. A single diagonal support line climbs from the deck's left end toward the upper part of the right post.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape SQUARE."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'efa088bb-74a9-4fd2-ae55-cc9fedda3e46'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/drawbridge_efa088bb-74a9-4fd2-ae55-cc9fedda3e46.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'drawbridge-between-rounded-upright-posts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('drawbridge', 'bridge', 'posts', 'deck', 'support', 'structure', 'crossing')
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
        rect('left',6,6,8,36,4);rect('right',34,6,8,36,4)
        line('deck-top',(14,30),(34,30));line('deck-bottom',(14,38),(34,38));line('cable',(14,30),(34,14))
        for a in ('deck-top','deck-bottom','cable'):
         self.relate('connect',a,'left');self.relate('connect',a,'right')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
