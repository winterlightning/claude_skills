"""Longer pointed pepper with flowing belly and clean curved stalk.
Plan: coherent named contours and repeated dimensions. HRECT_L natural subject envelope.
Construction reference: No useful exact Lucide match; smooth organic silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8658def3-7931-4cec-bff9-b70a989154e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chilli/20260925T070532Z-thuan-mac/reference/chilli_8658def3-7931-4cec-bff9-b70a989154e1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chilli'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('chilli',)

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

        path('pepper',(4,26),[('C',(31,18),(17,29),(24,24)),('C',(41,21),(36,13),(41,16)),('C',(23,40),(41,31),(32,40)),('C',(4,26),(13,40),(6,33))],True)
        path('stem',(41,21),[('C',(44,12),(43,19),(44,15)),('C',(40,8),(44,10),(43,8))])
        join('stem','pepper')
