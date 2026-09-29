from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2230e8dc-ec40-46aa-97fe-c7a3278e68e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-pregnant-person/20260929T093049Z-thuan-mac/reference/disability pregant_2230e8dc-ec40-46aa-97fe-c7a3278e68e9.svg'
AUTHOR = 'gpt-6'
# Reference comparison: The body is missing; the bent line and large arc do not convey pregnancy.
# Revision: Restore a complete side-facing body with a prominent rounded belly, dress hem, leg and bent arm.
# Construction references inspected: human_ref/full_body_ref.png; no useful direct Lucide pregnancy match

def path(icon, name, start, commands, closed=False):
    members=[]
    p=start
    for i,command in enumerate(commands):
        tag=f"{name}-{i}"
        q=(command[1],command[2])
        if command[0]=='L': icon.add_line(tag,p,q)
        else: icon.add_arc(tag,p,q,radius_x=command[3],radius_y=command[4],sweep=command[5])
        members.append(tag)
        p=q
    if closed and p != start:
        tag=f"{name}-close"
        icon.add_line(tag,p,start)
        members.append(tag)
    icon.add_contour(name,*members,closed=closed)

def circle(icon,name,cx,cy,r):
    path(icon,name,(cx-r,cy),[('A',cx+r,cy,r,r,True),('A',cx-r,cy,r,r,True)],True)

def rect(icon,name,x,y,w,h,r=2):
    path(icon,name,(x+r,y),[('L',x+w-r,y),('A',x+w,y+r,r,r,True),('L',x+w,y+h-r),('A',x+w-r,y+h,r,r,True),('L',x+r,y+h),('A',x,y+h-r,r,r,True),('L',x,y+r),('A',x+r,y,r,r,True)],True)

def bust(icon,name,cx,cy,r,half,base):
    # Detached circular head; shoulders start exactly 8 centerline units below its lower extent.
    circle(icon,name+'-head',cx,cy,r)
    top=cy+r+8
    path(icon,name+'-body',(cx-half,base),[('L',cx-half,top+half),('A',cx,top,half,half,True),('A',cx+half,top+half,half,half,True),('L',cx+half,base)])

class Drawing(Solo48):
    icon_id = 'standing-pregnant-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('disability', 'pregant')
    def build(self):
        # Side-facing pregnant silhouette: belly projects left, one bent arm rests to the right.
        # Head bottom 12; upper shoulder at y20 leaves exactly 4 ink units.
        circle(self,'head',24,8,4)
        path(self,'body',(24,20),[('L',22,20),('A',18,24,4,4,False),('L',18,27),('A',10,38,8,11,False),('L',18,38),('L',18,41),('A',26,41,4,4,False),('L',26,38),('L',31,38),('L',28,25),('L',24,20)],True)
        self.add_polyline('arm',(24,20),(38,26),(34,34))
        self.relate('connect','body','arm')
