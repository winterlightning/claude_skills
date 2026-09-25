"""Wavy banknote with coherent smooth boundaries and a clean dollar sign. Taller square envelope provides room for the currency strokes.
Omissions: None
Construction references: ['banknote'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f112a16f-0b5c-4192-abdc-173f55e6a032'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wavy-dollar-bill/20260924T172356Z-thuan-mac/reference/money bill wave_f112a16f-0b5c-4192-abdc-173f55e6a032.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wavy-dollar-bill'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('money', 'bill', 'wave')

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
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('bill',(6,8),[('C',(15,6),(9,6),(12,6)),('C',(33,8),(21,6),(27,8)),('C',(42,6),(37,8),(39,7)),('L',(42,40)),('C',(33,42),(39,42),(36,42)),('C',(15,40),(27,42),(21,40)),('C',(6,42),(11,40),(9,41)),('L',(6,8))],True)
        self.path('dollar',(28,18),[('C',(24,17),(27,17),(25,17)),('C',(24,24),(17,17),(17,23)),('C',(24,31),(31,25),(31,31)),('C',(20,30),(22,31),(21,31))])
        for n,a,b in [('top',(24,16),(24,17)),('bottom',(24,31),(24,32))]:
            self.add_line(n,a,b);self.relate('connect',n,'dollar')
