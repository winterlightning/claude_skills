'Plain Narrow Front Underwear.\nSymbol plan: A plain undergarment has a wide horizontal waistband with rounded corners. Its sides curve sharply inward below the band before descending into a long rounded central front panel.\nConstruction: Lucide shirt: one flowing garment outline, mirrored about x=24.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36d1d30d-0608-4321-9df3-408bff2b783a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/codpiece_36d1d30d-0608-4321-9df3-408bff2b783a.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'plain-narrow-front-underwear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('underwear', 'briefs', 'waistband', 'clothing', 'garment', 'front', 'bottoms')
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
        poly('band',(6,14),(6,6),(42,6),(42,14))
        bez('right',(42,14),((28,14),(32,30),(30,36)),((28,44),(20,44),(18,36)),((16,30),(20,14),(6,14)))
        con('briefs','band-1','band-2','band-3','right',closed=True)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
