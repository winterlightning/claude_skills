from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cbac8cc4-cc0b-4abf-8acb-10218e3182b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-person-wearing-an-arm-sling/20260929T093049Z-thuan-mac/reference/bandage shoulder_cbac8cc4-cc0b-4abf-8acb-10218e3182b5.svg'
AUTHOR = 'gpt-6'
# Reference comparison: A thick zigzag replaces the sling and hides the supported forearm.
# Revision: Restore a diagonal shoulder strap, triangular sling opening and horizontal supported forearm within the torso.
# Construction references inspected: human_ref/user.svg; no useful direct Lucide sling match

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
    icon_id = 'standing-person-wearing-an-arm-sling'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('bandage', 'shoulder')
    def build(self):
        # Frontal person: circular head and smooth shoulders frame a real arm sling.
        # Head bottom 14; shoulder top 22 gives exactly 4 ink units of separation.
        circle(self,'head',24,9,5)
        path(self,'body-arm',(8,42),[('L',8,30),('A',16,22,8,8,True),('L',30,22),('L',32,22),('A',38,28,6,6,True),('L',40,33),('A',35,38,5,5,True),('L',20,38),('A',20,32,3,3,True),('L',30,32),('L',34,32)])
        self.add_polyline('sling-strap',(30,22),(20,32),(30,32),(30,22))
        self.add_polyline('left-torso',(20,38),(16,38),(16,44))
        self.relate('connect','body-arm','left-torso')
        self.add_line('right-torso',(32,38),(32,44))
        self.relate('connect','body-arm','sling-strap')
        self.relate('connect','body-arm','right-torso')
