from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='4c602b7b-4759-408d-85ec-47eb4b50b541'
SOURCE_PATH='icon_set/work/todo-references/rearrange column_4c602b7b-4759-408d-85ec-47eb4b50b541.svg'
AUTHOR='gpt-6'
PLAN='Three segmented columns below a curved two-ended rearrangement arrow.'
OMISSIONS='Rows reduced to two per column.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rearrange-column'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rearrange', 'column')

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
        # Three segmented columns below a curved two-ended rearrangement arrow.

        for i,x in enumerate((4,20,36)):
            self.add_polyline('column'+str(i),(x,24),(x+8,24),(x+8,40),(x,40),closed=True)
            self.add_line('rule'+str(i),(x,32),(x+8,32));self.relate('connect','rule'+str(i),'column'+str(i))
        self.add_bezier('arrow',(8,15),((8,8),(14,8),(20,8)),((26,8),(40,8),(40,15)))
        self.add_polyline('left-tip',(4,11),(8,15),(12,11));self.relate('connect','left-tip','arrow')
        self.add_polyline('right-tip',(36,11),(40,15),(44,11));self.relate('connect','right-tip','arrow')

