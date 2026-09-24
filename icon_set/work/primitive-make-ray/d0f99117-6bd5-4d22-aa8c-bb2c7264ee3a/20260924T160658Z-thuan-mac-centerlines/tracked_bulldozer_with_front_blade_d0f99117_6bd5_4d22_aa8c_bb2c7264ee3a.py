'Tracked bulldozer with sloping cab roof front, continuous engine body, capsule track and curved blade. Bounds (4,8)-(44,40).\nConstruction: Lucide car: unified vehicle outline and round track ends.\nOmissions: Track rollers and inset cab window omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd0f99117-6bd5-4d22-aa8c-bb2c7264ee3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tracked-bulldozer-with-front-blade/20260924T160658Z-thuan-mac/reference/bulldozer_d0f99117-6bd5-4d22-aa8c-bb2c7264ee3a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tracked-bulldozer-with-front-blade'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('tracked', 'bulldozer', 'with', 'front', 'blade')

    def build(self):

        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        path('track',(9,30),[('L',(10,30)),('L',(25,30)),('A',(30,35),5,5,True),('A',(25,40),5,5,True),('L',(9,40)),('A',(4,35),5,5,True),('A',(9,30),5,5,True)],True)
        poly('cab',(10,30),(10,20),(14,20),(14,8),(24,8),(29,20),(30,20),(30,30),(25,30));join('cab','track')
        line('arm',(30,30),(40,30));join('arm','cab')
        path('blade',(42,18),[('C',(40,30),(41,22),(40,26)),('C',(44,40),(40,35),(42,38)),('L',(38,40)),('L',(38,20)),('L',(42,18))],True);join('blade','arm')
