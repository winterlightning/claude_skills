"""Passport cover and globe: a mirrored meridian pair, equator and circular rim. Rounded enclosure uses the Lucide id-card corner construction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f180a84-a846-4671-b767-dbb6041f800a'
SOURCE_PATH = 'pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg'
AUTHOR = 'gpt-6'
PLAN = 'Passport cover and globe: a mirrored meridian pair, equator and circular rim. Rounded enclosure uses the Lucide id-card corner construction.'
OMISSIONS = ['Rear-cover reveal omitted to give the globe a full cover interior.']
class Drawing(Solo48):
    icon_id = 'passport'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('passport',)
    def build(self):
        self.add_polyline('cover',(6,6),(42,6),(42,42),(6,42),closed=True)
        x,y,r=24,24,10
        self.circle('globe',x,y,r)
        self.add_arc('meridian-left',(x,y-r),(x,y+r),radius_x=5,radius_y=r,sweep=False)
        self.add_arc('meridian-right',(x,y-r),(x,y+r),radius_x=5,radius_y=r)
        self.add_polyline('equator',(x-r,y),(x,y),(x+r,y))
        for a,b in [('globe','meridian-left'),('globe','meridian-right'),('globe','equator'),('meridian-left','meridian-right'),('meridian-left','equator'),('meridian-right','equator')]:self.relate('connect',a,b)


    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; p=n+str(i)
            if i%2:self.add_arc(p,a,z,radius_x=rad)
            else:self.add_line(p,a,z)
            members.append(p)
        self.add_contour(n,*members,closed=True)
