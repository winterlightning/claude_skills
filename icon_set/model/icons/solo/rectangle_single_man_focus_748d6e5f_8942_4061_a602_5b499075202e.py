from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='748d6e5f-8942-4061-a602-5b499075202e'
SOURCE_PATH='icon_set/work/todo-references/rectangle single man focus_748d6e5f-8942-4061-a602-5b499075202e.svg'
AUTHOR='gpt-6'
PLAN='Portrait panel with four focus brackets around a head-and-shoulders silhouette. Bracket pairs mirror about x=24.'
CONSTRUCTION_REFERENCES='Shared human-reference.md/user.svg: circular head and shoulders; Lucide scan-face: corner focus brackets.'
OMISSIONS='Hair and neck contour reduced to the shared detached-head vocabulary; all brackets retained.'
KEYSHAPE_INK_BOUNDS=(6, 2, 42, 46)

class Drawing(Solo48):
    icon_id='rectangle-single-man-focus'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'single', 'man', 'focus')

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
        for name,points in [('tl',((14,18),(14,12),(18,12))),('tr',((30,12),(34,12),(34,18))),('bl',((14,30),(14,36),(18,36))),('br',((30,36),(34,36),(34,30)))]:self.add_polyline('focus-'+name,*points)
        self.bust('person',24,20,3,6,3)

KEYSHAPE_REASON='The upright panel uses centerline extremes (8,4)–(40,44).'
