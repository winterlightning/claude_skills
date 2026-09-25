from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='e23fb9d7-ed54-45f6-9142-77054c14c7bc'
SOURCE_PATH='icon_set/work/todo-references/rectangle ad text_e23fb9d7-ed54-45f6-9142-77054c14c7bc.svg'
AUTHOR='gpt-6'
PLAN='The letters AD inside a rectangular advertising panel.'
OMISSIONS='No letters omitted; outlines squared to preserve spacing.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-ad-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('rectangle', 'ad', 'text')

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
        # The letters AD inside a rectangular advertising panel.

        self.add_polyline('frame',(4,8),(44,8),(44,40),(4,40),closed=True)
        self.add_polyline('a',(12,31),(15,16),(18,31))
        self.add_line('a-bar',(13,26),(17,26));self.relate('connect','a','a-bar')
        self.add_line('d-stem',(27,31),(27,17));self.add_arc('d-bowl',(27,17),(27,31),radius_x=8,radius_y=7);self.add_contour('d','d-stem','d-bowl',closed=True)

