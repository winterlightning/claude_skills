"""Hryvnia: smooth reversed S with horizontal extrema and two exactly parallel currency bars.
Omissions: None
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5afaf6ee-841d-4918-940a-7de550ac7754'
SOURCE_PATH = 'pictographic-primitives/symbol/hryvnia sign_5afaf6ee-841d-4918-940a-7de550ac7754.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hryvnia-sign'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('hryvnia', 'sign')

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
        self.path('currency',(14,6),[('C',(24,4),(17,4),(20,4)),('C',(34,12),(30,4),(34,7)),('C',(27,20),(34,15),(30,18)),('C',(21,28),(24,22),(24,26)),('C',(14,36),(18,30),(14,33)),('C',(24,44),(14,41),(18,44)),('C',(34,42),(28,44),(31,44))])
        self.add_polyline('upper',(8,20),(27,20),(40,20));self.add_polyline('lower',(8,28),(21,28),(40,28))
        self.relate('connect','currency','upper');self.relate('connect','currency','lower')
