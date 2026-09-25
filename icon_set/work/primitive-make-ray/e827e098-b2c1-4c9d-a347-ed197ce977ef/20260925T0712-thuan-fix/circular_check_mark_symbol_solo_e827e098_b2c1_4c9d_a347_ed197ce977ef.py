"""Extend the open circular ring and balance a crisp check inside it.
Plan: coherent named contours and repeated dimensions. CIRCLE natural subject envelope.
Construction reference: Lucide circle-check-big: open ring and independent check.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e827e098-b2c1-4c9d-a347-ed197ce977ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__circular-check-mark-symbol-solo/20260925T070532Z-thuan-mac/reference/circle check 1_e827e098-b2c1-4c9d-a347-ed197ce977ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-check-mark-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('circle', 'check', '1')

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

        path('ring',(44,24),[('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True),('C',(32,6),(27,4),(29,5))])
        poly('check',(16,23),(24,31),(40,12))
