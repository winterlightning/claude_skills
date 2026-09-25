"""Fist is rounded into a long forearm; the lower arm has a horizontal bottom tangent; muscle has one smooth inner curve.
Omissions: Small fist creases and the closed inner muscle lens reduced to one curve.
Construction references: ['biceps-flexed'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f4100bb0-e557-5776-84f3-12d5a0ad1a62'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/massage muscle_f4100bb0-e557-5776-84f3-12d5a0ad1a62.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='flexed-arm-with-inner-muscle-shape-batch-012-14'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "health"
    aliases=()
    keywords=('massage', 'muscle')

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('arm',(44,24),[('C',(24,27),(38,20),(29,22)),('C',(21,17),(23,24),(21,20)),('C',(25,14),(24,16),(25,15)),('C',(21,8),(25,10),(24,8)),('C',(13,12),(17,8),(15,10)),('C',(4,33),(9,19),(4,28)),('C',(24,40),(4,40),(14,40)),('C',(44,36),(32,40),(39,38))])
        self.path('muscle',(24,27),[('C',(37,27),(28,30),(33,30))])
        self.relate('connect','arm','muscle')
