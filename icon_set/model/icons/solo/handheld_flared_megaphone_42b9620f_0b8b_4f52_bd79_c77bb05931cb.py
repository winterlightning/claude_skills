# Final reduction: Omit small bell dome and doubled rim; retain flared horn, housing and lower handle.
'Handheld Flared Megaphone.\nSymbol plan: A megaphone points right with a wide flared horn and thick rounded front rim. A compact rear housing carries a downward handle, while a small dome projects beyond the bell.\nConstruction: Lucide megaphone: flared horn attached to a compact housing and lower grip.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42b9620f-0b8b-4f52-bd79-c77bb05931cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bullhorn_42b9620f-0b8b-4f52-bd79-c77bb05931cb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'handheld-flared-megaphone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('megaphone', 'horn', 'announcement', 'handle', 'sound', 'speaker', 'device')
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
        rect('rear',4,16,12,12,3)
        poly('horn',(16,16),(44,8),(44,32),(16,28))
        poly('grip',(6,28),(10,40),(20,40),(16,28))
        self.relate('connect','rear','horn');self.relate('connect','rear','grip')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
