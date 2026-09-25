# Final reduction: Flat hull baseline replaces wave detail. Turret reduced to gun stem.
'Warship with Deck Gun on Waves.\nSymbol plan: A warship faces right with a long stepped hull resting on a wavy waterline. A central deckhouse supports a short mast, and a small forward turret carries an angled gun barrel.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Use flat waterline and reduce turret housing to a deck gun.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '34b9e30c-830f-44aa-b0a0-6458ea79ac3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/destroyer_34b9e30c-830f-44aa-b0a0-6458ea79ac3b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'warship-with-deck-gun'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('warship', 'ship', 'destroyer', 'gun', 'navy', 'vessel', 'water')
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
        poly('hull',(4,28),(44,28),(36,40),(12,40),closed=True)
        poly('deck',(12,28),(16,20),(26,20),(26,28))
        line('mast',(20,8),(20,20));poly('gun',(34,28),(34,20),(44,16))
        self.relate('connect','hull','deck');self.relate('connect','deck','mast');self.relate('connect','hull','gun')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
