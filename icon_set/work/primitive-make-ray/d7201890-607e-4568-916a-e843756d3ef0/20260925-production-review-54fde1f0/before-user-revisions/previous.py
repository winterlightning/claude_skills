"""Calendar uses matching radius-3 corners, equal bindings, a straight header and a long diagonal seven.
Omissions: None
Construction references: ['calendar'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d7201890-607e-4568-916a-e843756d3ef0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__calendar-number-seven/20260924T171046Z-thuan-mac/reference/calendar number seven_d7201890-607e-4568-916a-e843756d3ef0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='calendar-number-seven'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('calendar', 'number', 'seven')

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
        self.path('top',(8,17),[('L',(8,11)),('A',(11,8),3,3,True),('L',(16,8)),('L',(32,8)),('L',(37,8)),('A',(40,11),3,3,True),('L',(40,17))])
        self.path('body',(40,17),[('L',(40,41)),('A',(37,44),3,3,True),('L',(11,44)),('A',(8,41),3,3,True),('L',(8,17))])
        self.add_line('header',(8,17),(40,17))
        for a,b in [('top','body'),('header','top'),('header','body')]:self.relate('connect',a,b)
        for x in (16,32):
            self.add_line('binding-'+str(x),(x,4),(x,8));self.relate('connect','binding-'+str(x),'top')
        self.add_polyline('seven',(20,26),(31,26),(24,35))
