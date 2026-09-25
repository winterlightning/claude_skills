"""Two circular arcs and equal right-angle arrowheads related by 180-degree rotation.
Omissions: None
Construction references: ['refresh-cw'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e63cb3c3-10bb-4fb1-a675-1e6b119047a5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__circular-rotating-arrows/20260924T171046Z-thuan-mac/reference/arrows spin_e63cb3c3-10bb-4fb1-a675-1e6b119047a5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='circular-rotating-arrows'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('arrows', 'spin')

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
        for name,flip in [('upper',False),('lower',True)]:
            def p(x,y):return (48-x,48-y) if flip else (x,y)
            self.path(name,p(6,21),[('C',p(24,6),p(6,13),p(14,6)),('C',p(42,18),p(32,6),p(38,12))])
            self.add_polyline(name+'-head',p(32,18),p(42,18),p(42,6))
            self.relate('connect',name,name+'-head')
