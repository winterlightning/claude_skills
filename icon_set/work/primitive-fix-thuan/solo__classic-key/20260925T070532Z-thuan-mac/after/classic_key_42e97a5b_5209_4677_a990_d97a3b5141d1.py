"""Larger circular key bow, full length terminal tooth and balanced inner tooth.
Plan: coherent named contours and repeated dimensions. SQUARE natural subject envelope.
Construction reference: Lucide key: round bow joined to a single shaft.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '42e97a5b-5209-4677-a990-d97a3b5141d1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__classic-key/20260925T070532Z-thuan-mac/reference/key 1_42e97a5b-5209-4677-a990-d97a3b5141d1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'classic-key'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('key', '1')

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

        path('bow',(22,24),[('A',(26,32),10,10,True),('A',(16,42),10,10,True),('A',(6,32),10,10,True),('A',(16,22),10,10,True),('A',(22,24),10,10,True)],True)
        poly('shaft',(22,24),(28,18),(38,6),(42,10))
        line('inner-tooth',(28,18),(33,23));join('bow','shaft');join('shaft','inner-tooth')
