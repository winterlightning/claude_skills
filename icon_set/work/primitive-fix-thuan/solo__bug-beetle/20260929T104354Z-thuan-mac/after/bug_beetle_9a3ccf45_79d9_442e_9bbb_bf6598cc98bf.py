'Rebuilt a rounded symmetrical body, centered the dividing line and attached three equally balanced leg pairs.\nOriginal/current comparison: The rejected beetle has crowded shoulder joints and a top divider; the original has a round body crossed at its middle.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide bug original and atomic-debug: paired attachments and continuous rounded body; source horizontal body division restored.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9a3ccf45-79d9-442e-9bbb-bf6598cc98bf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bug-beetle/20260929T104354Z-thuan-mac/reference/bug_9a3ccf45-79d9-442e-9bbb-bf6598cc98bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bug-beetle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bug', 'beetle')

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

        path('body',(16,14),[('C',(24,10),(18,11),(20,10)),('C',(32,14),(28,10),(30,11)),('C',(36,24),(35,17),(36,20)),('C',(32,34),(36,28),(35,31)),('C',(24,38),(30,37),(28,38)),('C',(16,34),(20,38),(18,37)),('C',(12,24),(13,31),(12,28)),('C',(16,14),(12,20),(13,17))],True)
        line('middle',(12,24),(36,24));join('middle','body')
        for side,s in [('left',-1),('right',1)]:
            for name,a,b in [('upper',(24+s*8,14),(24+s*16,6)),('middle',(24+s*12,24),(24+s*18,24)),('lower',(24+s*8,34),(24+s*16,42))]:
                n=name+'-'+side;line(n,a,b);join(n,'body')
                if name=='middle':join(n,'middle')
