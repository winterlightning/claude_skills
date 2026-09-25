'Ring Hub with Three Spokes.\nSymbol plan: A large circular hub with a smaller concentric opening sits on the right. Three straight spokes extend leftward at different angles, each ending in a small circular node.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd0f6df7c-0039-4ae0-af51-2226c8c2154d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon web service internet of thing event_d0f6df7c-0039-4ae0-af51-2226c8c2154d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'ring-hub-with-three-spokes-d0f6df7c'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('hub', 'network', 'spokes', 'nodes', 'connections', 'ring', 'topology')
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
        circle('hub',30,24,12);circle('hole',30,24,3)
        circle('upper-node',8,8,2);circle('middle-node',8,24,2);circle('lower-node',8,40,2)
        line('spoke-a',(10,9),(22,15));line('spoke-b',(10,24),(18,24));line('spoke-c',(10,39),(22,33))
        for n in ('a','b','c'):self.relate('connect','spoke-'+n,'hub')
        self.relate('connect','spoke-a','upper-node');self.relate('connect','spoke-b','middle-node');self.relate('connect','spoke-c','lower-node')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
