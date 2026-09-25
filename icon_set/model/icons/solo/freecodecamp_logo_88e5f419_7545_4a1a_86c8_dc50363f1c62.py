"""Matching smooth parentheses enclose a coherent asymmetric flame with a single inward tongue.
Omissions: Nested inner flame and small side tongue reduced to one coherent flame silhouette.
Construction references: ['flame'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='88e5f419-7545-4a1a-86c8-dc50363f1c62'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__freecodecamp-logo/20260924T171046Z-thuan-mac/reference/freecodecamp logo_88e5f419-7545-4a1a-86c8-dc50363f1c62.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='freecodecamp-logo'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('freecodecamp', 'logo')

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
        self.path('left',(7,10),[('C',(4,24),(5,13),(4,19)),('C',(7,38),(4,29),(5,35))])
        self.path('right',(41,10),[('C',(44,24),(43,13),(44,19)),('C',(41,38),(44,29),(43,35))])
        self.path('flame',(23,8),[('C',(30,22),(28,12),(30,17)),('C',(32,31),(31,25),(32,27)),('C',(24,40),(32,36),(29,40)),('C',(16,31),(19,40),(16,36)),('C',(23,8),(16,24),(26,19))],True)
