"""Rounded envelope corners and gently rounded flap tip restore the source construction.
Plan: coherent named contours and repeated dimensions. HRECT_M natural subject envelope.
Construction reference: Lucide mail: soft enclosure corners and continuous flap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '36431152-eb7f-4823-8544-b6247731eddd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-envelope-batch-020-12/20260925T070532Z-thuan-mac/reference/mail_36431152-eb7f-4823-8544-b6247731eddd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-envelope-batch-020-12'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mail',)

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

        box('envelope',4,10,44,38,3)
        path('flap',(4,13),[('L',(21,25)),('C',(27,25),(23,27),(25,27)),('L',(44,13))])
        join('flap','envelope')
