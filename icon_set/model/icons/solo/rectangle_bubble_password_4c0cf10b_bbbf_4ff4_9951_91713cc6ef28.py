from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='4c0cf10b-bbbf-4ff4-9951-91713cc6ef28'
SOURCE_PATH='icon_set/work/todo-references/rectangle bubble password_4c0cf10b-bbbf-4ff4-9951-91713cc6ef28.svg'
AUTHOR='gpt-6'
PLAN='A long rounded password field containing two X masking marks.'
OMISSIONS='No masking marks omitted.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-bubble-password'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'bubble', 'password')

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
        # A long rounded password field containing two X masking marks.

        self.box('field',4,10,40,28,10)
        for i,x in enumerate((17,31)):
            self.add_line('x'+str(i)+'a',(x-3,21),(x+3,27));self.add_line('x'+str(i)+'b',(x+3,21),(x-3,27));self.relate('connect','x'+str(i)+'a','x'+str(i)+'b')

