# Final reduction: One centered stethoscope tube and chestpiece replace cramped paired tubing. Circular head ends y=18; shoulders top y=26: exact 4-unit ink gap.
'Doctor Bust with a Stethoscope.\nSymbol plan: An oval head floats above broad shoulders and a V-shaped neckline. A stethoscope hangs around the neck, ending in paired earpiece tubing on the left and a circular chestpiece on the right.\nConstruction: human_ref/user.svg: circular head and broad shoulders.\nReduction: Circular head bottom y=18, shoulders top y=26: exact 4-unit ink gap. Omit neckline and earpiece fork to retain stethoscope.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b100d26-07ec-44b1-9174-2936180175ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/allergist_7b100d26-07ec-44b1-9174-2936180175ea.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'doctor-bust-with-a-stethoscope'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('doctor', 'stethoscope', 'medical', 'portrait', 'health', 'physician', 'bust')
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
        circle('head',24,11,7)
        bez('shoulders',(8,44),((8,31),(12,26),(24,26)),((36,26),(40,31),(40,44)))
        line('tube',(24,26),(24,35));circle('chestpiece',24,38,3)
        self.relate('connect','shoulders','tube');self.relate('connect','tube','chestpiece')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
