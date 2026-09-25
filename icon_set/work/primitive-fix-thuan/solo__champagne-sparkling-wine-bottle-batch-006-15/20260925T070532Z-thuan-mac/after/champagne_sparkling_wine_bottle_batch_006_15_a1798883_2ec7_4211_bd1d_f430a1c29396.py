"""Slender champagne neck with rounded cap, flowing shoulders and rounded bottle base.
Plan: coherent named contours and repeated dimensions. VRECT_M natural subject envelope.
Construction reference: Lucide bottle-wine: narrow neck and flowing shoulders.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a1798883-2ec7-4211-bd1d-f430a1c29396'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__champagne-sparkling-wine-bottle-batch-006-15/20260925T070532Z-thuan-mac/reference/champagne bottle_a1798883-2ec7-4211-bd1d-f430a1c29396.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'champagne-sparkling-wine-bottle-batch-006-15'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('champagne', 'bottle')

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

        path('bottle',(19,13),[('L',(19,9)),('A',(29,9),5,5,True),('L',(29,13)),('C',(38,29),(29,21),(38,22)),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,29)),('C',(19,13),(10,22),(19,21))],True)
        line('cap-seam',(19,13),(29,13));join('cap-seam','bottle')
        line('base-seam',(10,35),(38,35))
