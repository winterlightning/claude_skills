"""The rejected winged lion resembled a rabbit with angular ears. Restore curved outspread wings above a rounded mane and central muzzle.
Symbol plan: Original winged lion; mirrored swept wings and rounded mane, no useful exact Lucide match.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '31adb801-c03d-4489-a2fa-3ecf7a57b89b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-lion-head/20260929T124732Z-thuan-mac/reference/winged lion_31adb801-c03d-4489-a2fa-3ecf7a57b89b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'winged-lion-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('winged', 'lion', 'head')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('mane',(12,30),[('A',(36,30),12,8,True),('A',(12,30),12,12,True)],True)
        poly('nose',(22,32),(24,33),(26,32))
        path('wing-left',(20,14),[('C',(6,6),(20,10),(12,8)),('C',(14,14),(6,11),(9,14))])
        path('wing-right',(28,14),[('C',(42,6),(28,10),(36,8)),('C',(34,14),(42,11),(39,14))])
