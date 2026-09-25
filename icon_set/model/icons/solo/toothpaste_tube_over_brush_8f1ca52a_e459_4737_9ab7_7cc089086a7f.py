"""A diagonal toothpaste tube over a horizontal toothbrush; matching nozzle and brush curves.
Omissions: Detached toothpaste dollop and fine bristle subdivisions omitted due to clearance.
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8f1ca52a-e459-4737-9ab7-7cc089086a7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brush toothpaste 2_8f1ca52a-e459-4737-9ab7-7cc089086a7f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='toothpaste-tube-over-brush'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('brush', 'toothpaste', '2')

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
        self.add_polyline('tube',(26,6),(42,18),(28,30),(20,24),closed=True)
        self.add_line('nozzle',(20,24),(18,27));self.relate('connect','tube','nozzle')
        self.path('brush',(6,42),[('L',(14,42)),('L',(24,42)),('C',(34,38),(29,42),(29,38)),('L',(42,38))])
        for x in (6,14):
            self.add_line('bristle-'+str(x),(x,34),(x,42));self.relate('connect','bristle-'+str(x),'brush')
