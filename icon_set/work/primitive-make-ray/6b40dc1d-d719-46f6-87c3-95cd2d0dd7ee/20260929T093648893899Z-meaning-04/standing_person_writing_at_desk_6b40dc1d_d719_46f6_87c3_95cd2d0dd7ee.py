from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6b40dc1d-d719-46f6-87c3-95cd2d0dd7ee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-person-writing-at-desk/20260929T093049Z-thuan-mac/reference/desk document base work standing user_6b40dc1d-d719-46f6-87c3-95cd2d0dd7ee.svg'
AUTHOR = 'gpt-6'
# Reference comparison: The person appears to walk beside a box, with floating bars and no clear writing surface.
# Revision: Restore a stationary standing body, bent writing arm, pen, paper and open-legged desk.
# Construction references inspected: human_ref/full_body_ref.png; Lucide file-pen-line

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
    icon_id = 'standing-person-writing-at-desk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('desk', 'document', 'base', 'work', 'standing', 'user')
    def build(self):
        # Side-view writer with a continuous upright leg and a hand resting at the desk.
        # Circular head bottom 12 and shoulder top 20 are exactly 8 apart on centerlines.
        circle(self,'head',36,8,4)
        path(self,'writer',(36,20),[('A',42,26,6,6,True),('L',42,41),('A',36,41,3,3,True),('L',36,29),('L',32,32),('L',24,32),('A',24,26,3,3,True),('L',30,26),('L',36,20)],True)
        self.add_polyline('desk',(4,44),(4,32),(24,32),(28,32),(28,44))
        self.add_line('paper',(9,28),(19,28))
        self.add_line('pen',(21,28),(25,18))
        self.relate('connect','writer','desk')
