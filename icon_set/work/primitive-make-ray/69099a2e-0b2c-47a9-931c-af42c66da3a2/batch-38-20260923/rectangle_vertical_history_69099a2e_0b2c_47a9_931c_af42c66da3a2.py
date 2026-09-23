from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='69099a2e-0b2c-47a9-931c-af42c66da3a2'
SOURCE_PATH='icon_set/work/todo-references/rectangle vertical history_69099a2e-0b2c-47a9-931c-af42c66da3a2.svg'
AUTHOR='gpt-6'
PLAN='Portrait history panel enclosing a three-quarter circular return arrow and clock hands.'
CONSTRUCTION_REFERENCES='No local Lucide history original found; circular arc and attached arrow are constructed directly.'
OMISSIONS='Minute ticks absent in source; no additions.'
KEYSHAPE_INK_BOUNDS=(6, 2, 42, 46)

class Drawing(Solo48):
    icon_id='rectangle-vertical-history'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'vertical', 'history')

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
        self.box('panel',8,4,32,40,4)
        self.add_arc('history',(24,34),(34,24),radius_x=10,large_arc=True)
        self.add_polyline('arrow',(30,20),(34,24),(34,18));self.relate('connect','history','arrow')
        self.add_polyline('hands',(24,18),(24,24),(28,28))

KEYSHAPE_REASON='The upright panel uses centerline extremes (8,4)–(40,44).'
