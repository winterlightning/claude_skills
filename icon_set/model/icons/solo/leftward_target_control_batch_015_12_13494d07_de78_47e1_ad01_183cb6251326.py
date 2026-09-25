"""Smooth circular target boundary ending behind a circular node, with balanced left arrow.
Omissions: None
Construction references: ['arrow-left'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13494d07-de78-47e1-ad01-183cb6251326'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='leftward-target-control-batch-015-12'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    aliases=()
    keywords=('cursor', 'move', 'target', 'left')

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
        self.path('target',(10,18),[('C',(28,8),(14,11),(20,8)),('A',(44,24),16,16,True),('A',(28,40),16,16,True),('C',(10,30),(20,40),(14,37))])
        self.circle('node',10,24,6);self.relate('connect','target','node')
        self.add_polyline('head',(30,18),(24,24),(30,30));self.add_line('shaft',(24,24),(35,24));self.relate('connect','head','shaft')
