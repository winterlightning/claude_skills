from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='bd159874-c962-4129-9d84-72190444e5e0'
SOURCE_PATH='icon_set/work/todo-references/rectangle check_bd159874-c962-4129-9d84-72190444e5e0.svg'
AUTHOR='gpt-6'
PLAN='A wide rectangle contains a checkmark left of centre.'
OMISSIONS='No defining features omitted.'
LUCIDE_REFERENCE='check'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-check'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('rectangle', 'check')

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
        # A wide rectangle contains a checkmark left of centre.

        self.add_polyline('frame',(4,10),(44,10),(44,38),(4,38),closed=True)
        self.add_polyline('check',(13,24),(19,30),(30,18))

