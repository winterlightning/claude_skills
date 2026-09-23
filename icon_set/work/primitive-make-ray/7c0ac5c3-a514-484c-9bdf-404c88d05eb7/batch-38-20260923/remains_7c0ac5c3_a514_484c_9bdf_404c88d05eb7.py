from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7c0ac5c3-a514-484c-9bdf-404c88d05eb7'
SOURCE_PATH='icon_set/work/todo-references/remains_7c0ac5c3-a514-484c-9bdf-404c88d05eb7.svg'
AUTHOR='gpt-6'
PLAN='Diagonal bone beside a pointed leaf with a vein continuing into a stem. Preserve the organic asymmetry.'
CONSTRUCTION_REFERENCES='Lucide bone: paired rounded lobes and narrow shaft; leaf: curved pointed outline with stem.'
OMISSIONS='None.'
KEYSHAPE_INK_BOUNDS=(2, 8, 46, 40)

class Drawing(Solo48):
    icon_id='remains'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('remains',)

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
        # Paired radius-four lobes; a diagonal shaft connects the two ends.
        self.add_line('shaft-upper',(12,14),(20,22))
        self.add_arc('end-upper',(20,22),(20,30),radius_x=4)
        self.add_arc('end-lower',(20,30),(16,34),radius_x=4,large_arc=True)
        self.add_line('shaft-lower',(16,34),(12,22))
        self.add_arc('start-lower',(12,22),(8,18),radius_x=4,large_arc=True)
        self.add_arc('start-upper',(8,18),(12,14),radius_x=4,large_arc=True)
        self.add_contour('bone','shaft-upper','end-upper','end-lower','shaft-lower','start-lower','start-upper',closed=True)
        self.add_bezier('leaf',(44,12),((44,24),(43,31),(36,33)),((32,33),(32,18),(44,12)))
        self.add_polyline('vein',(34,38),(36,33),(40,23));self.relate('connect','leaf','vein')

KEYSHAPE_REASON='The shallow wide composition uses centerline extremes (4,10)–(44,38).'
FINAL_REDUCTIONS='No objects omitted. Bone angle made steeper and leaf narrowed to separate both subjects.'
