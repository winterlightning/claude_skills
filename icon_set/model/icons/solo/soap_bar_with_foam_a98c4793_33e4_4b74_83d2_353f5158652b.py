'Perspective soap bar behind a broad foam outline. Straight box edges and circular lather lobes. Bounds (6,6)-(42,42).\nConstruction: Lucide cloud: coherent rounded foam lobes.\nOmissions: Lower soap edges hidden behind foam.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a98c4793-33e4-4b74-83d2-353f5158652b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/sponge soap_a98c4793-33e4-4b74-83d2-353f5158652b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soap-bar-with-foam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('soap', 'bar', 'with', 'foam')

    def build(self):

        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        poly('bar',(6,30),(6,16),(22,6),(42,6),(42,28),(36,32))
        poly('top',(6,16),(28,16),(42,6));join('top','bar')
        line('edge',(28,16),(28,28));join('edge','top')
        path('foam',(6,30),[('A',(14,22),8,8,True),('A',(22,30),8,8,True),('A',(28,28),6,6,True),('A',(36,32),8,6,True),('A',(42,37),6,5,True),('A',(24,42),18,5,True),('A',(6,37),18,5,True),('L',(6,30))],True)
        join('foam','bar');join('foam','edge')
