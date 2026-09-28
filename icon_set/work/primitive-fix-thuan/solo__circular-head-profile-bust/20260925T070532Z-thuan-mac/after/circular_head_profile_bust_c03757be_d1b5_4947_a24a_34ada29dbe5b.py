"""Restore broad rounded shoulder block with circular detached head and exact 4px ink gap.
Plan: coherent named contours and repeated dimensions. VRECT_L natural subject envelope.
Construction reference: human_ref/user.svg: round head and broad smooth shoulders.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c03757be-d1b5-4947-a24a-34ada29dbe5b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__circular-head-profile-bust/20260925T070532Z-thuan-mac/reference/bob_c03757be-d1b5-4947-a24a-34ada29dbe5b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-head-profile-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('bob',)

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

        circle('head',24,12,8)
        path('body',(8,44),[('L',(8,38)),('A',(18,28),10,10,True),('L',(30,28)),('A',(40,38),10,10,True),('L',(40,44)),('L',(8,44))],True)
