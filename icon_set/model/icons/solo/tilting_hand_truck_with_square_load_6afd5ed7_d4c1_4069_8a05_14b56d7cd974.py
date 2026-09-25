"""Tilting hand truck with a round wheel, bent handle, and a square load derived from perpendicular integer vectors.
Omissions: Small trailing wheel omitted; primary wheel and tilting load retained.
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6afd5ed7-d4c1-4069-8a05-14b56d7cd974'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dolly_6afd5ed7-d4c1-4069-8a05-14b56d7cd974.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tilting-hand-truck-with-square-load'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('dolly',)

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
        self.path('handle',(6,6),[('L',(8,6)),('C',(11,10),(10,6),(11,8)),('L',(15,30))])
        self.circle('wheel',15,36,6);self.relate('connect','handle','wheel')
        self.add_polyline('load',(25,16),(38,12),(42,25),(29,29),closed=True)
        self.add_polyline('platform',(21,36),(29,29),(42,25))
        self.relate('connect','wheel','platform');self.relate('connect','load','platform')
