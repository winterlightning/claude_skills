"""Courier with rear parcel, circular head and equal wheels. Torso turns smoothly into seated thigh; neck y20 minus head bottom y12 equals 8 centerline / 4 ink.
Construction: human_ref/full_body_ref.png: outlined round heads and continuous limbs; Lucide bike original/atomic-debug: two-wheel scene.
Omissions: Scooter panels, headlamp and wheel hubs omitted; parcel, seated leg and cap distinction retained.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '54079a5b-25ea-4346-8fc4-d2b5f8239da0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='capped-delivery-rider-on-scooter'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('capped', 'delivery', 'rider', 'on', 'scooter')
    def build(self):
        self.circle('head',24,9,3)
        for n,x in [('rear-wheel',9),('front-wheel',39)]:self.circle(n,x,39,3)
        self.box('parcel',6,16,14,24,2)
        self.line('torso',(24,20),(24,25))
        self.path('seated-leg',(24,25),[('A',(27,28),3,3,False),('A',(30,31),3,3,True)])
        self.line('arm',(24,20),(38,20))
        self.path('fork',(38,20),[('C',(39,36),(39,24),(39,30))])
        self.line('frame',(12,39),(36,39))
        for a,b in [('torso','seated-leg'),('torso','arm'),('arm','fork'),('fork','front-wheel'),('frame','front-wheel'),('frame','rear-wheel')]:self.join(a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.line('visor',(27,9),(32,9));self.join('visor','head')

    def path(self,n,p,steps,closed=False):
        ids=[]
        for j,step in enumerate(steps):
            k,q,*v=step; uid=f'{n}-{j}'
            if k=='L': self.add_line(uid,p,q)
            elif k=='A': self.add_arc(uid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif k=='C': self.add_bezier(uid,p,(v[0],v[1],q))
            ids.append(uid);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=2):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def line(self,n,a,b): self.add_line(n,a,b)
    def poly(self,n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
    def join(self,a,b): self.relate('connect',a,b)
