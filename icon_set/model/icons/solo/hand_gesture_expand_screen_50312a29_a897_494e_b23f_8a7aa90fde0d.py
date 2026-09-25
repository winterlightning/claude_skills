"""Rounded pointing finger and thumb between three identical outward arrows and bottom-right corner.
Omissions: Small folded-finger separations omitted.
Construction references: ['hand', 'move-diagonal'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='50312a29-a897-494e-b23f-8a7aa90fde0d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-gesture-expand-screen/20260924T171046Z-thuan-mac/reference/hand gesture control expand_50312a29-a897-494e-b23f-8a7aa90fde0d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hand-gesture-expand-screen'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('hand', 'gesture', 'control', 'expand')

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
        self.path('hand',(20,34),[('L',(16,27)),('C',(22,25),(14,22),(19,21)),('L',(22,18)),('A',(30,18),4,4,True),('L',(30,25)),('C',(34,27),(32,24),(34,25)),('L',(34,30)),('A',(30,34),4,4,True),('L',(20,34))],True)
        for n,p in [('tl',[(13,6),(6,6),(6,13),(12,12)]),('tr',[(35,6),(42,6),(42,13),(37,11)]),('bl',[(6,35),(6,42),(13,42),(11,37)])]:
            self.add_polyline(n,*p[:3]);self.add_line(n+'-stem',p[1],p[3]);self.relate('connect',n,n+'-stem')
        self.add_polyline('corner',(42,36),(42,42),(36,42))
