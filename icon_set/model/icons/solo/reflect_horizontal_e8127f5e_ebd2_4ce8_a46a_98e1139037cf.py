from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e8127f5e-ebd2-4ce8-a46a-98e1139037cf'
SOURCE_PATH='icon_set/work/todo-references/reflect horizontal_e8127f5e-ebd2-4ce8-a46a-98e1139037cf.svg'
AUTHOR='gpt-6'
PLAN='Two horizontal outlined bars with an upward sloping stroke attached to the lower bar. Shared width and eight-unit bar height.'
CONSTRUCTION_REFERENCES='No useful exact Lucide match; paired rectangles and diagonal stroke are reconstructed directly.'
OMISSIONS='None.'
KEYSHAPE_INK_BOUNDS=(2, 6, 46, 42)

class Drawing(Solo48):
    icon_id='reflect-horizontal'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('reflect', 'horizontal')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def bust(self,name,cx,cy,r,shoulder_half_width,shoulder_height):
        # Shared human reference: body apex exactly 8 below head outline.
        self.circle(name+'-head',cx,cy,r)
        apex=cy+r+8;end_y=apex+shoulder_height
        self.add_arc(name+'-shoulders',(cx-shoulder_half_width,end_y),(cx+shoulder_half_width,end_y),radius_x=shoulder_half_width,radius_y=shoulder_height)

    def cross(self,name,cx,cy,half):
        self.add_polyline(name+'-a',(cx-half,cy-half),(cx,cy),(cx+half,cy+half))
        self.add_polyline(name+'-b',(cx+half,cy-half),(cx,cy),(cx-half,cy+half))
        self.relate('connect',name+'-a',name+'-b')

    def reflection(self,direction):
        # Triangles mirror around the axis; only arrowhead direction changes.
        self.add_line('axis',(24,18),(24,42))
        for name,x,tip in (('left',6,16),('right',42,32)):
            self.add_polyline(name,(x,20),(tip,31),(x,42),closed=True)
        self.add_arc('arrow-arc',(14,16),(34,16),radius_x=10)
        x=14 if direction=='left' else 34
        self.add_polyline('arrowhead',(x-4,12),(x,16),(x+4,12))
        self.relate('connect','arrow-arc','arrowhead')

    def build(self):
        self.add_polyline('top-bar',(4,8),(44,8),(44,16),(4,16),closed=True)
        self.add_polyline('bottom-bar',(4,32),(20,32),(44,32),(44,40),(4,40),closed=True)
        self.add_line('slope',(20,32),(28,24));self.relate('connect','bottom-bar','slope')

KEYSHAPE_REASON='The wide composition uses centerline extremes (4,8)–(44,40).'
