'Mushroom Explosion Cloud.\nSymbol plan: A large lobed cloud cap spreads above a narrow vertical column with gently curved sides. The column widens toward a low rounded base, forming a tall mushroom-shaped explosion silhouette.\nConstruction: Lucide cloud: broad continuous lobes, extended into a mushroom stem.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2dea1540-2eee-4f44-b49e-7aaa9f6d42a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nuke_2dea1540-2eee-4f44-b49e-7aaa9f6d42a6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'mushroom-explosion-cloud-2dea1540'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('explosion', 'mushroom', 'cloud', 'nuclear', 'smoke', 'blast')
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
        bez('cap',(16,28),((6,28),(6,24),(6,20)),((6,16),(10,14),(12,14)),((12,6),(18,6),(24,6)),((30,6),(36,6),(36,14)),((38,14),(42,16),(42,20)),((42,24),(42,28),(32,28)))
        bez('stem-right',(32,28),((29,35),(29,38),(36,42)))
        line('base',(36,42),(12,42))
        bez('stem-left',(12,42),((19,38),(19,35),(16,28)))
        con('cloud','cap','stem-right','base','stem-left',closed=True)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
