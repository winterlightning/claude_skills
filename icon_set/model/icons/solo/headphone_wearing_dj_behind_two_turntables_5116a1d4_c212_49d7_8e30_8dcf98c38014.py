"""Circular head with attached headphone band and ear strokes; broad shoulders meet deck; two separated platter marks.
Keyshape VRECT_L. Shared human user.svg and full_body_ref.png for round head and shoulders; Lucide headphones for attached ear strokes. Head bottom16 to shoulder top24 gives exact 4-unit ink gap.
Omissions: Platters reduced to short marks to retain shoulders and console."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5116a1d4-c212-49d7-8e30-8dcf98c38014'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/concert dj_5116a1d4-c212-49d7-8e30-8dcf98c38014.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'headphone-wearing-dj-behind-two-turntables'
    keyshape = Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "entertainment"
    aliases=()
    keywords=('headphone', 'wearing', 'dj', 'behind', 'two', 'turntables')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('head',24,10,6)
        for side in (-1,1):
         x=24+side*6; z=24+side*14
         path(f'headphone-{side}',(x,10),[('L',(z,10)),('L',(z,16))]);join(f'headphone-{side}','head')
        path('shoulders',(14,28),[('A',(24,24),10,4,True),('A',(34,28),10,4,True)])
        poly('deck',(10,28),(14,28),(34,28),(38,28),(40,44),(8,44),closed=True);join('deck','shoulders')
        for x in (18,30):self.add_dot(f'platter-{x}',(x,36))

