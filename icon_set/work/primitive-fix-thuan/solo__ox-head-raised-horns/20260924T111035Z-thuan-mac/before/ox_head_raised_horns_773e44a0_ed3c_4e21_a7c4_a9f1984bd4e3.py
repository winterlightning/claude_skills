'Ox Head with Raised Horns.\nSymbol plan: An ox head faces forward with a long tapered face and broad rounded muzzle. Two large horns curve outward and upward above small side ears, leaving the central face blank.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit small side ears; preserve the raised horns and broad muzzle.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '773e44a0-ed3c-4e21-a7c4-a9f1984bd4e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ox_773e44a0-ed3c-4e21-a7c4-a9f1984bd4e3.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'ox-head-raised-horns'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('ox', 'cattle', 'head', 'horns', 'animal', 'livestock')
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
        bez('face',(16,18),((16,30),(18,34),(20,34)))
        bez('face-right',(28,34),((30,34),(32,30),(32,18)))
        line('forehead',(16,18),(32,18))
        rect('muzzle',16,32,16,8,4)
        bez('horn-left',(16,18),((8,18),(4,14),(4,8)),((4,23),(10,26),(16,26)))
        bez('horn-right',(32,18),((40,18),(44,14),(44,8)),((44,23),(38,26),(32,26)))
        self.relate('connect','muzzle','face');self.relate('connect','muzzle','face-right');self.relate('connect','horn-left','face');self.relate('connect','horn-right','face-right')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
