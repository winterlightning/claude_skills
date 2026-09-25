from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1f180a84-a846-4671-b767-dbb6041f800a'
SOURCE_PATH='pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg'
AUTHOR='gpt-6'
PLAN='Passport changed from SQUARE to VRECT_L, with a taller cover and globe radius11 instead of10. Both curved meridians and equator are restored. Cover/globe spacing is retained as an approved exception.'
CONSTRUCTION_REFERENCES='Lucide globe and rectangle-ellipsis originals and atomic-debug: circular graticule and consistent rounded corners.'
OMISSIONS=['Rear-cover reveal omitted.']
class Drawing(Solo48):
    icon_id='travel-passport-with-globe'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('passport',)

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Taller passport envelope with a larger round globe and full curved graticule.
        self.box('cover',8,4,40,44,4)
        self.circle('globe',24,25,11)
        self.path('meridian-left',(24,14),[('A',(20,25),4,11,False),('A',(24,36),4,11,False)])
        self.path('meridian-right',(24,14),[('A',(28,25),4,11,True),('A',(24,36),4,11,True)])
        self.add_polyline('equator',(13,25),(20,25),(28,25),(35,25))
        for a,b in [('globe','meridian-left'),('globe','meridian-right'),('globe','equator'),('meridian-left','meridian-right'),('meridian-left','equator'),('meridian-right','equator')]:self.relate('connect',a,b)

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'Passport changed from SQUARE to VRECT_L, with a taller cover and globe radius11 instead of10. Both curved meridians and equator are restored. Cover/globe spacing is retained as an approved exception.', 'scope': ['globe/cover clearance'], 'svg_sha256': 'e2d42cd2fa2a15b1a60f97c8c23a776defd7ae55df9c7b1a7d8fdf7587e0df44', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}
