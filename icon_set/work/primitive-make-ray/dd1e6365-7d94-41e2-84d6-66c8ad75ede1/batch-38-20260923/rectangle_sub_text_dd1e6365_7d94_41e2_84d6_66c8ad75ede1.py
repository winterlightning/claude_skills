from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='dd1e6365-7d94-41e2-84d6-66c8ad75ede1'
SOURCE_PATH='icon_set/work/todo-references/rectangle sub text_dd1e6365-7d94-41e2-84d6-66c8ad75ede1.svg'
AUTHOR='gpt-6'
PLAN='Rounded panel containing the full uppercase text SUB. Each glyph is authored as a coherent stroke or connected bowls.'
CONSTRUCTION_REFERENCES='Lucide rectangle-ellipsis: outer panel; letters hand-authored from supplied source.'
OMISSIONS='None; all three letters retained.'
KEYSHAPE_INK_BOUNDS=(2, 6, 46, 42)

class Drawing(Solo48):
    icon_id='rectangle-sub-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'sub', 'text')

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
        self.box('panel',4,8,40,32,4)
        self.add_bezier('s',(18,17),((15,13),(9,15),(10,20)),((11,23),(17,23),(18,27)),((19,32),(12,34),(10,30)))
        self.add_line('u-left',(23,16),(23,28))
        self.add_arc('u-base',(23,28),(29,28),radius_x=3,sweep=False)
        self.add_line('u-right',(29,28),(29,16));self.add_contour('u','u-left','u-base','u-right')
        self.add_polyline('b-stem',(34,32),(34,24),(34,16),(36,16))
        self.add_arc('b-upper',(36,16),(36,24),radius_x=4)
        self.add_arc('b-lower',(36,24),(36,32),radius_x=4)
        self.add_line('b-bottom',(36,32),(34,32));self.add_line('b-mid',(34,24),(36,24))
        for a,b in [('b-stem','b-upper'),('b-upper','b-lower'),('b-lower','b-bottom'),('b-bottom','b-stem'),('b-mid','b-stem'),('b-mid','b-upper'),('b-mid','b-lower')]:self.relate('connect',a,b)

KEYSHAPE_REASON='The wide composition uses centerline extremes (4,8)–(44,40).'
