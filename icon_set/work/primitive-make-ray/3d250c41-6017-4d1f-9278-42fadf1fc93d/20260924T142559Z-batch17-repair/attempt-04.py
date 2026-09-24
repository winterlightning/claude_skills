from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3d250c41-6017-4d1f-9278-42fadf1fc93d'
SOURCE_PATH='icon_set/work/todo-references/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg'
AUTHOR='gpt-6'
PLAN='LIKE lettering inside a rectangular social button.'
OMISSIONS='All four letters retained; hand-built centerline glyphs.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-like-text'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'like', 'text')

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
        self.box('frame',6,6,36,36,3)
        self.add_polyline('l',(10,16),(10,32),(14,32))
        self.add_line('i',(20,16),(20,32))
        self.add_polyline('k-stem',(26,16),(26,24),(26,32))
        self.add_polyline('k-arms',(31,16),(26,24),(31,32))
        self.relate('connect','k-stem','k-arms')
        self.add_polyline('e',(39,16),(35,16),(35,24),(35,32),(39,32))
        self.add_line('e-middle',(35,24),(39,24))
        self.relate('connect','e','e-middle')
