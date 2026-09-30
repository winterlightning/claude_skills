'Broadened the crown, flattened its dome slightly and retained a regular band and upturned brim.\nOriginal/current comparison: The rejected crown is too tall and narrow compared with the broad low bowler in the original.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; geometric arcs and smooth coherent contours.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9ffcaa3-d483-4e32-bc69-6209c65297b2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bowler-hat/20260929T104354Z-thuan-mac/reference/hat gentleman_f9ffcaa3-d483-4e32-bc69-6209c65297b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowler-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bowler', 'hat')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        path('crown',(8,22),[('A',(40,22),16,14,True),('L',(40,32)),('L',(40,40)),('L',(8,40)),('L',(8,32)),('L',(8,22))],True)
        line('band',(8,32),(40,32));join('band','crown')
        arc('brim-left',(4,36),(8,40),4,s=False);join('brim-left','crown')
        arc('brim-right',(40,40),(44,36),4,s=False);join('brim-right','crown')
