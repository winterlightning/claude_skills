'Restored an outlined reservoir, a long high column and smoother bulb shoulders with two detached ticks.\nOriginal/current comparison: The rejected thermometer reservoir is a solid dot and the bulb has abrupt side flares.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide thermometer original and atomic-debug: continuous tube and rounded bulb; source high column and two ticks preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '26bf3af8-64f9-4d16-aa6c-a43c72408de7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__high-column-two-tick-thermometer/20260929T110700Z-thuan-mac/reference/temperature high_26bf3af8-64f9-4d16-aa6c-a43c72408de7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'high-column-two-tick-thermometer'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('high', 'column', 'two', 'tick', 'thermometer')

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

        path('outline',(11,24),[('L',(11,13)),('A',(29,13),9),('L',(29,24)),('C',(32,32),(29,27),(32,28)),('A',(8,32),12),('C',(11,24),(8,28),(11,27))],True)
        circle('reservoir',20,32,3)
        line('column',(20,14),(20,29));join('column','reservoir')
        for j,y in enumerate((14,24)):line(f'tick-{j}',(39,y),(40,y))
