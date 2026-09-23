from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='41658dd2-6728-40b7-9a13-fdc34b4bb0ec'
SOURCE_PATH='icon_set/work/todo-references/rectangle person_41658dd2-6728-40b7-9a13-fdc34b4bb0ec.svg'
AUTHOR='gpt-6'
PLAN='Framed person with circular detached head and a smooth broad shoulder arch. Subject and frame share x=24.'
CONSTRUCTION_REFERENCES='Shared human-reference.md and human_ref/user.svg own proportions and detached gap; Lucide rectangle-ellipsis supplies the frame.'
OMISSIONS='Frame made taller to provide head/shoulder clearance.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='rectangle-person'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'person')

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
        self.box('panel',6,6,36,36,4)
        self.bust('person',24,18,3,8,4)

KEYSHAPE_REASON='The full composition uses centerline extremes (6,6)–(42,42).'
