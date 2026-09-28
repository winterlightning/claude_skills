# Final reduction: One open continuous spring with three broad alternating turns replaces overlapping closed coils.
'Open Spring with Three Broad Coils.\nSymbol plan: A vertical spring has three broad horizontal coils with rounded right ends. Slanting links connect successive coils down the left side, and the lowest link trails diagonally toward the lower edge.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f44ef841-7cdc-418d-b3f0-78940e56e0a8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-spring-with-three-broad-coils/20260927T165437Z-thuan-mac-1/reference/spring_f44ef841-7cdc-418d-b3f0-78940e56e0a8.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-spring-with-three-broad-coils'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('spring', 'coil', 'metal', 'mechanism', 'compression', 'spiral')
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
        # Three broad horizontal coils form one continuous open spring.
        line('top',(12,4),(36,4));arc('turn1',(36,4),(36,12),4)
        line('return1',(36,12),(12,12));arc('link1',(12,12),(12,20),4,s=False)
        line('coil2',(12,20),(36,20));arc('turn2',(36,20),(36,28),4)
        line('return2',(36,28),(12,28));arc('link2',(12,28),(12,36),4,s=False)
        line('coil3',(12,36),(36,36));arc('turn3',(36,36),(36,44),4)
        line('base',(36,44),(12,44))
        con('spring','top','turn1','return1','link1','coil2','turn2','return2','link2','coil3','turn3','base')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
