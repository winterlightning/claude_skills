'Moon on a Dashed Earth Orbit.\nSymbol plan: An Earth globe with an irregular continent outline sits within a larger dashed orbit. A small round moon interrupts the orbit at the upper right, separated from the globe itself.\nConstruction: Lucide orbit: clear central globe and offset satellite.\nReduction: Four broad orbit dashes replace the fine dashed ring.\nKeyshape CIRCLE: ink extremes (2, 2, 46, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87fce6c8-26b1-411d-877c-3b43d5067f7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy earth rotation_87fce6c8-26b1-411d-877c-3b43d5067f7d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'moon-on-a-dashed-earth-orbit-87fce6c8'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('earth', 'moon', 'orbit', 'globe', 'continent', 'astronomy', 'space')
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
        circle('earth',24,24,8)
        line('continent',(24,16),(24,20))
        self.relate('connect','continent','earth')
        circle('moon',39,9,3)
        arc('orbit-a',(6,24),(24,6),18)
        arc('orbit-b',(42,24),(24,42),18)
        arc('orbit-c',(16,40),(8,32),18)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
