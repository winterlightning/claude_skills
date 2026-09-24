from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='922ba268-0492-4ece-8f41-54253b52949a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/refugee immigration war 2_922ba268-0492-4ece-8f41-54253b52949a.svg'
AUTHOR = 'gpt-6'
PLAN='Explosion with a diagonal capsule inside, beside a small house with an arched door. Preserve the full war/displacement scene.'
CONSTRUCTION_REFERENCES='No useful exact Lucide match; starburst and house contours reconstructed from source.'
OMISSIONS='Two short peripheral impact rays omitted to reduce nonessential clutter.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='refugee-immigration-war-2'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('refugee', 'immigration', 'war', '2')

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
        # Four broad blast points replace the tightly serrated burst. The damaged
        # roof starts at the blast's lower-right notch; the left wall is interrupted.
        self.add_polyline('explosion',(18,6),(24,12),(30,18),(24,24),(18,30),(12,24),(6,18),(12,12),closed=True)
        self.add_dot('impact',(18,18))
        self.add_line('roof',(24,24),(42,34))
        self.add_polyline('house',(26,36),(26,42),(42,42),(42,34))
        self.relate('connect','explosion','roof')
        self.relate('connect','roof','house')
