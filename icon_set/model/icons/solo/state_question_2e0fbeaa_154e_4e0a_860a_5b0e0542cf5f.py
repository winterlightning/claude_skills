"""Question mark has a smooth round hook, short vertical return and distinct dot centered within a true circle.
Omissions: None
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2e0fbeaa-154e-4e0a-860a-5b0e0542cf5f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__state-question/20260924T172356Z-thuan-mac/reference/state question_2e0fbeaa-154e-4e0a-860a-5b0e0542cf5f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='state-question'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('state', 'question')

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
        self.circle('ring',24,24,20)
        self.path('question',(18,19),[('A',(30,19),6,6,True),('C',(24,27),(30,23),(24,23))])
        self.add_dot('dot',(24,35))
