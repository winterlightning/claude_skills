"""The rejected profile-selection icon lost the hair, leaving a generic broken circle and cursor. Restore a swept hair division and an unmistakable selection pointer.
Symbol plan: Original head/cursor; Lucide user supporting round head construction; hair retained to identify a profile.
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

        path('head',(21,32),[('A',(6,19),15,13,True),('A',(34,19),14,13,True)])
        path('hair',(7,14),[('C',(21,9),(12,17),(18,14)),('C',(32,14),(24,14),(28,15))]);join('hair','head')
        poly('cursor',(27,26),(42,33),(35,35),(32,42),closed=True)
