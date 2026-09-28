"""Smaller circular hinge and longer splayed compass legs; deliberate diagonal posture.
Plan: coherent named contours and repeated dimensions. SQUARE natural subject envelope.
Construction reference: Lucide drafting-compass: circular hinge and braced legs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f18957c4-d496-4dcc-baef-4934631bc063'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__circinus-state/20260925T070532Z-thuan-mac/reference/circinus_f18957c4-d496-4dcc-baef-4934631bc063.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circinus-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('circinus',)

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('hinge',(35,10),[('A',(37,14),5,5,True),('A',(32,19),5,5,True),('A',(28,17),5,5,True),('A',(27,14),5,5,True),('A',(32,9),5,5,True),('A',(35,10),5,5,True)],True)
        line('grip',(35,10),(42,6));join('grip','hinge')
        poly('left-leg',(28,17),(17,25),(6,33));join('left-leg','hinge')
        poly('right-leg',(32,19),(29,28),(24,42));join('right-leg','hinge')
        line('brace',(17,25),(29,28));join('brace','left-leg');join('brace','right-leg')
