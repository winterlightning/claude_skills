"""Guitar: rejected waist is pinched, neck blocky and soundhole a solid dot. Restore smooth body transitions and visible soundhole. Widen the waist around a visible soundhole, and smooth the body and headstock.
Symbol plan: Lucide guitar original/atoms: smooth waist curves, round soundhole and rounded headstock; strings and bridge omitted for spacing.
Keyshape VRECT_M: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '39f10ef4-8250-4acb-b0ce-eaee10f3b757'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-acoustic-guitar/20260929T115456Z-thuan-mac/reference/guitars_39f10ef4-8250-4acb-b0ce-eaee10f3b757.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'upright-acoustic-guitar'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'acoustic', 'guitar')

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

        path('outline',(20,8),[('A',(24,4),4,4,True),('A',(28,8),4,4,True),('L',(28,18)),('C',(36,24),(32,18),(36,20)),('C',(35,30),(36,27),(35,28)),('C',(38,37),(35,32),(38,33)),('A',(31,44),7,7,True),('L',(17,44)),('A',(10,37),7,7,True),('C',(13,30),(10,33),(13,32)),('C',(12,24),(13,28),(12,27)),('C',(20,18),(12,20),(16,18)),('L',(20,8))],True)
        circle('soundhole',24,32,3)
