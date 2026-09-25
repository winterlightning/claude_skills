"""Restore recognizable land detail within the tilted desk globe and a rounded pedestal.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: VRECT_L for the subject's natural orientation.
Construction: Lucide earth: simplified continent boundary inside a circle; globe provides circular construction.
Reduction: Fine coastline detail reduced to one broad continuous land boundary.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd7db4bca-68d7-4e3b-b134-1375e3f3d159'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__desk-globe-stand/20260925T083122Z-thuan-mac/reference/earth model_d7db4bca-68d7-4e3b-b134-1375e3f3d159.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'desk-globe-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'model')

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


        path('globe',(17,7),[('A',(26,4),15,15,True),('A',(41,19),15,15,True),('A',(35,31),15,15,True),('A',(26,34),15,15,True),('A',(11,19),15,15,True),('A',(17,7),15,15,True)],True)
        path('support',(13,4),[('C',(4,19),(7,8),(4,12)),('C',(26,40),(4,31),(14,40)),('C',(40,35),(32,40),(37,38))])
        line('axis-top',(13,4),(17,7));join('axis-top','globe');join('axis-top','support')
        line('axis-bottom',(35,31),(40,35));join('axis-bottom','globe');join('axis-bottom','support')
        path('land',(26,4),[('C',(21,10),(26,9),(21,6)),('L',(21,13)),('L',(27,13)),('C',(31,18),(30,13),(31,15)),('C',(26,28),(31,22),(28,27)),('C',(22,22),(23,29),(22,26)),('L',(22,20)),('C',(11,19),(20,17),(15,20))]);join('land','globe')
        line('post',(26,40),(26,45));join('post','support')
        poly('foot',(14,45),(26,45),(38,45));join('post','foot')
