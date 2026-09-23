from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='a9eae52c-5fba-4c26-8ab9-e955eeea7260'
SOURCE_PATH='icon_set/work/todo-references/real estate market house increase_a9eae52c-5fba-4c26-8ab9-e955eeea7260.svg'
AUTHOR='gpt-6'
PLAN='Three ascending market bars under an upward diagonal arrow.'
OMISSIONS='No house added: the supplied reference contains only chart bars and arrow.'
LUCIDE_REFERENCE='chart-no-axes-column-increasing'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='real-estate-market-house-increase'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('real', 'estate', 'market', 'house', 'increase')

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
        # Three ascending market bars under an upward diagonal arrow.

        for i,(x,top) in enumerate(((4,32),(20,24),(36,8))):
            self.add_polyline('bar'+str(i),(x,40),(x,top),(x+8,top),(x+8,40),closed=True)
        self.add_line('trend',(4,20),(28,8))
        self.add_polyline('tip',(20,8),(28,8),(28,16));self.relate('connect','trend','tip')

