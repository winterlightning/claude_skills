"""bareheaded-delivery-rider-on-scooter. Reconstructed clean centerlines from the original reference.
Construction reference: bike and human_ref/full_body_ref.png. Keyshape SQUARE chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9046ec78-1a6b-4029-a2e9-be0d10843436'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bareheaded-delivery-rider-on-scooter/20260925T034142Z-thuan-mac/reference/delivery person motorcycle 1_9046ec78-1a6b-4029-a2e9-be0d10843436.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bareheaded-delivery-rider-on-scooter'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('bareheaded', 'delivery', 'rider', 'on', 'scooter')
    def build(self):
        # Equal wheel circles, circular head, right-angle parcel, smooth seated hip.
        # Shared human reference full_body_ref.png. Neck20-headBottom12=8 CL /4 ink.
        self.circle('head',24,9,3)
        self.circle('rear-wheel',9,39,3);self.circle('front-wheel',39,39,3)
        self.add_polyline('parcel',(6,16),(14,16),(14,24),(6,24),closed=True)
        self.add_line('torso',(24,20),(24,25))
        self.path('leg',(24,25),[('A',(27,28),3,3,False),('A',(30,31),3,3,True)])
        self.add_line('arm',(24,20),(38,20))
        self.add_line('fork',(38,20),(39,36))
        self.add_line('frame',(12,39),(36,39))
        for a,b in [('torso','leg'),('torso','arm'),('arm','fork'),('fork','front-wheel'),('frame','front-wheel'),('frame','rear-wheel')]:self.join(a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

    def path(self,n,p,ops,closed=False):
        members=[]
        for i,(kind,q,*v) in enumerate(ops):
            eid=f'{n}-{i}'
            if kind=='L': self.add_line(eid,p,q)
            elif kind=='A': self.add_arc(eid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C': self.add_bezier(eid,p,(v[0],v[1],q))
            members.append(eid);p=q
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def join(self,a,b): self.relate('connect',a,b)
