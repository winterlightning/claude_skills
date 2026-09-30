"""The rejected profile-selection mark lost its hair division. Restore a broad swept hairline within the open round head and keep the pointer lower right.
Symbol plan: Original profile hair and pointer; circular head and shared hair attachments.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '742a102d-2547-4878-9ea9-c64ad681d52b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-profile-selection-cursor-solo/20260929T122443Z-thuan-mac/reference/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'user-profile-selection-cursor-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('user', 'profile', 'selection', 'cursor', 'solo')

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

        path('head',(18,33),[('A',(6,19),14,14,True),('A',(34,19),14,13,True)])
        path('hair',(6,19),[('C',(20,14),(12,23),(16,20)),('C',(34,19),(25,19),(29,20))]);join('head','hair')
        poly('cursor',(28,27),(42,33),(35,35),(32,42),closed=True)
