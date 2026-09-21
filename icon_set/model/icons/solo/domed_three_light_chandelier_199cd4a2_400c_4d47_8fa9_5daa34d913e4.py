'Domed Three Light Chandelier.\nSymbol plan: A domed ceiling fixture hangs from a short vertical stem. Three round lights descend below its flat lower edge, one on a straight central cord and two on curved side arms.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Side cords simplified to short stems; three circular lamps retained.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '199cd4a2-400c-4d47-8fa9-5daa34d913e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/ceiling lamp chandelier_199cd4a2-400c-4d47-8fa9-5daa34d913e4.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'domed-three-light-chandelier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('chandelier', 'lights', 'dome', 'ceiling', 'fixture', 'round', 'lighting')
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
        line('stem',(24,6),(24,14))
        arc('dome',(10,28),(38,28),14)
        line('rim',(38,28),(10,28));con('shade','dome','rim',closed=True)
        for i,x in enumerate((8,24,40)):
         circle('bulb'+str(i),x,40,2)
         line('cord'+str(i),(x,38),(10 if i==0 else 38 if i==2 else 24,28));self.relate('connect','cord'+str(i),'shade');self.relate('connect','cord'+str(i),'bulb'+str(i))
        self.relate('connect','cord1','shade');self.relate('connect','stem','shade')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
