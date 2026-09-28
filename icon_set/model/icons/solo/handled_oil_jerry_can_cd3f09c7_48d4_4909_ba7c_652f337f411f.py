'Handled Oil Jerry Can.\nSymbol plan: A tall jerry can has rounded corners, a small raised cap at the upper left, and a sloping upper shoulder. A triangular rounded handle opening occupies the upper right portion of the body.\nConstruction: Lucide fuel: rounded vessel and integrated handle opening.\nReduction: Broaden the handle into a rounded opening; retain the cap and sloping shoulder.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd3f09c7-48d4-4909-ba7c-652f337f411f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/oleo_cd3f09c7-48d4-4909-ba7c-652f337f411f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'handled-oil-jerry-can'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('jerrycan', 'oil', 'can', 'handle', 'container', 'fuel')
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
        poly('cap',(12,12),(12,4),(20,4),(20,12))
        bez('top',(8,20),((8,12),(12,12),(20,12)),((24,12),(24,8),(30,8)),((40,8),(40,12),(40,18)))
        line('right',(40,18),(40,38));arc('br',(40,38),(34,44),6)
        line('base',(34,44),(14,44));arc('bl',(14,44),(8,38),6)
        line('left',(8,38),(8,20));con('can','top','right','br','base','bl','left',closed=True)
        rect('handle',17,21,14,12,4)
        self.relate('connect','cap','can')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
