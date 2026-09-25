'Raised Peace Sign Hand.\nSymbol plan: A hand raises two long fingers into a wide V above a rounded palm. The other fingers curl inward beside a folded thumb, with a short palm crease beneath the crossing thumb.\nConstruction: Human reference: rounded hand silhouette; Lucide hand informs finger caps.\nReduction: Omit palm crease and separate curled fingertips.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd445cb84-69cc-4534-88ca-0620e15e15d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/peace sign_d445cb84-69cc-4534-88ca-0620e15e15d7.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'raised-peace-sign-hand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hand', 'peace', 'victory', 'fingers', 'gesture', 'palm')
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
        poly('finger-left',(18,28),(8,10));bez('left-cap',(8,10),((8,6),(8,4),(12,4)),((16,4),(18,6),(20,10)))
        poly('v',(20,10),(24,20),(30,8));arc('right-cap',(30,8),(38,8),4)
        line('right-finger',(38,8),(34,28));bez('palm',(34,28),((40,28),(40,32),(40,36)),((40,44),(32,44),(24,44)),((12,44),(8,38),(8,30)),((8,26),(14,26),(18,30)))
        line('thumb',(18,30),(28,32))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
