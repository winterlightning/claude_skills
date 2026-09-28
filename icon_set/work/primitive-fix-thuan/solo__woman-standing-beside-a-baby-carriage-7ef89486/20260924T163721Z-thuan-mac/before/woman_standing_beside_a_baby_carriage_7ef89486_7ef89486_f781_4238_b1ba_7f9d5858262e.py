'Woman Standing Beside a Baby Carriage.\nSymbol plan: A small standing figure with curved hair and a flared dress appears at left. A round-bodied baby carriage with an upright hood and two tiny wheels stands separately to her right.\nConstruction: human_ref/full_body_ref.png: circular head and flared dress; Lucide baby carriage construction.\nReduction: One leg and open hood silhouette simplify the small figure and carriage.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7ef89486-f781-4238-b1ba-7f9d5858262e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby trolley_7ef89486-f781-4238-b1ba-7f9d5858262e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'woman-standing-beside-a-baby-carriage-7ef89486'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('woman', 'carriage', 'baby', 'stroller', 'parent', 'person', 'scene')
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
        circle('head',11,10,4)
        bez('dress',(6,36),((6,28),(7,22),(11,22)),((15,22),(16,28),(16,36)))
        line('hem',(6,36),(16,36));line('leg',(11,36),(11,42))
        bez('carriage',(24,22),((24,30),(32,30),(34,30)),((42,30),(42,26),(42,22)))
        arc('hood',(32,12),(42,22),10)
        poly('hood-rim',(32,12),(32,22),(42,22))
        circle('wheel-a',27,40,2);circle('wheel-b',40,40,2)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
