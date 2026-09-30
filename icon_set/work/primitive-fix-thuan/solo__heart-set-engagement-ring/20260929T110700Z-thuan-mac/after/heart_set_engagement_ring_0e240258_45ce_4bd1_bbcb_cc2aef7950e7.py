'Deepened the heart and smoothed its lower sides, with an open rounded ring band beneath it.\nOriginal/current comparison: The rejected heart is flat and triangular, whereas the original has a taller rounded jewel above a circular band.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide heart original and atomic-debug: matched lobes and flowing sides; supplied source retains heart above an open band.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0e240258-45ce-4bd1-bbcb-cc2aef7950e7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-set-engagement-ring/20260929T110700Z-thuan-mac/reference/lgbt engagement ring_0e240258-45ce-4bd1-bbcb-cc2aef7950e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-set-engagement-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('heart', 'set', 'engagement', 'ring')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
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

        path('heart',(24,12),[('A',(16,4),8,8,False),('A',(8,12),8,8,False),('C',(24,26),(8,17),(18,23)),('C',(40,12),(30,23),(40,17)),('A',(32,4),8,8,False),('A',(24,12),8,8,False)],True)
        path('band',(10,30),[('A',(24,44),14,14,False),('A',(38,30),14,14,False)])
