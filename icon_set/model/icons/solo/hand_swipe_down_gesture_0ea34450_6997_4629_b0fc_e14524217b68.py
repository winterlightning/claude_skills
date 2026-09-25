"""Right-pointing rounded hand, smooth contact arc and complete downward arrow.
Omissions: None
Construction references: ['hand'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0ea34450-6997-4629-b0fc-e14524217b68'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-swipe-down-gesture/20260924T171046Z-thuan-mac/reference/gesture tap swipe down 1_0ea34450-6997-4629-b0fc-e14524217b68.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hand-swipe-down-gesture'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('gesture', 'tap', 'swipe', 'down', '1')

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
        self.path('hand',(4,28),[('L',(4,20)),('L',(17,14)),('C',(20,18),(22,12),(24,17)),('L',(28,18)),('A',(28,26),4,4,True),('L',(18,26)),('L',(16,28)),('L',(8,28)),('L',(4,28))],True)
        self.path('motion',(27,8),[('C',(44,23),(36,8),(44,14)),('C',(38,32),(44,27),(42,30))])
        self.add_polyline('arrow',(20,36),(24,40),(28,36));self.add_line('shaft',(24,35),(24,40));self.relate('connect','arrow','shaft')
