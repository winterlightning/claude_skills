"""The rejected doll omitted the pin and made the head very flat. Restore a visible pin entering the left head edge and a rounder sewn head with two clear cross eyes. Keep an upright layout to retain both eyes at 48px; simplify the original diagonal pose.
Symbol plan: Original sewn doll and pin; smooth curve construction, upright reduction for readable crossed eyes.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41a210db-2c37-42ef-baba-2adfb456a545'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__voodoo-doll-with-cross-eyes/20260929T122443Z-thuan-mac/reference/voodoo doll_41a210db-2c37-42ef-baba-2adfb456a545.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'voodoo-doll-with-cross-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('voodoo', 'doll', 'with', 'cross', 'eyes')

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

        path('doll',(6,20),[('C',(10,12),(6,16),(8,14)),('C',(24,8),(14,8),(18,8)),('C',(42,20),(35,8),(42,12)),('C',(34,28),(42,25),(37,28)),('L',(36,28)),('A',(40,32),4,4,True),('A',(36,36),4,4,True),('L',(36,38)),('A',(32,42),4,4,True),('L',(24,34)),('L',(16,42)),('A',(12,38),4,4,True),('L',(12,36)),('A',(8,32),4,4,True),('A',(12,28),4,4,True),('L',(14,28)),('C',(6,20),(11,28),(6,25))],True)
        for x in (18,30):
         line(f'eye-{x}-a',(x-1,18),(x+1,20));line(f'eye-{x}-b',(x-1,20),(x+1,18));join(f'eye-{x}-a',f'eye-{x}-b')
        line('pin',(6,6),(10,12));join('pin','doll')
