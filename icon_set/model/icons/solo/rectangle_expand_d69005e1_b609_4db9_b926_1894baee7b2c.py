from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='d69005e1-b609-4db9-b926-1894baee7b2c'
SOURCE_PATH='icon_set/work/todo-references/rectangle expand_d69005e1-b609-4db9-b926-1894baee7b2c.svg'
AUTHOR='gpt-6'
PLAN='A diagonal two-headed expand arrow inside a rectangular card.'
OMISSIONS='No defining features omitted.'
LUCIDE_REFERENCE='move-diagonal-2'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-expand'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('rectangle', 'expand')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def house(self,n,x,y,w,h):
        mid=x+w//2
        self.add_polyline(n,(x,y+8),(mid,y),(x+w,y+8),(x+w,y+h),(x,y+h),closed=True)

    def bust(self,n,x,y,r,shoulder_w,shoulder_h):
        self.circle(n+'-head',x,y,r)
        body_top=y+r+8
        self.add_arc(n+'-shoulders',(x-shoulder_w,body_top+shoulder_h),(x+shoulder_w,body_top+shoulder_h),radius_x=shoulder_w,radius_y=shoulder_h)
        # Exact detached gap: (y+r+8) - (y+r) = 8 centerline / 4 ink.

    def build(self):
        # A diagonal two-headed expand arrow inside a rectangular card.

        self.box('frame',4,8,40,32,4)
        self.add_line('diagonal',(14,18),(32,30))
        self.add_polyline('upper',(14,26),(14,18),(22,18));self.relate('connect','upper','diagonal')
        self.add_polyline('lower',(24,30),(32,30),(32,22));self.relate('connect','lower','diagonal')

