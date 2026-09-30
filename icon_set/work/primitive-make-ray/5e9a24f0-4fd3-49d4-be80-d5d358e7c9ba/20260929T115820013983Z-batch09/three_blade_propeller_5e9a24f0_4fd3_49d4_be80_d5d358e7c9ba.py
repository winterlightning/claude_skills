"""Propeller: rejected lower blades are angular and hub oversized. Use round blade ends and balanced blade lengths. Round all three tips and use a smaller hub with long smoothly widening blades.
Symbol plan: Lucide fan original and atoms: few coherent rounded blade contours around a central hub; three blades per source.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5e9a24f0-4fd3-49d4-be80-d5d358e7c9ba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-blade-propeller/20260929T115456Z-thuan-mac/reference/propeller_5e9a24f0-4fd3-49d4-be80-d5d358e7c9ba.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'three-blade-propeller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'blade', 'propeller')

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

        circle('hub',24,25,6)
        path('top-blade',(19,22),[('L',(18,12)),('A',(30,12),6,6,True),('L',(29,22))]);join('top-blade','hub')
        path('left-blade',(18,25),[('L',(8,33)),('A',(14,42),6,6,False),('L',(23,31))]);join('left-blade','hub')
        path('right-blade',(30,25),[('L',(40,33)),('A',(34,42),6,6,True),('L',(25,31))]);join('right-blade','hub')
