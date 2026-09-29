from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4c828b75-2ce2-5271-b9ae-3111238b215a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stationary-bike-rider/20260929T093049Z-thuan-mac/reference/sport gym cycling_4c828b75-2ce2-5271-b9ae-3111238b215a.svg'
AUTHOR = 'gpt-6'
# Reference comparison: The rider has no convincing torso or bent pedaling leg and the equipment resembles a scooter.
# Revision: Restore an aligned head and leaning torso, bent pedaling leg, handlebar support and broad stationary-bike housing.
# Construction references inspected: human_ref/full_body_ref.png; Lucide bike

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
    icon_id = 'stationary-bike-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('sport', 'gym', 'cycling')
    def build(self):
        # Leaning rider and stationary exercise-bike housing. Torso points toward the head via a 5-12-13 triangle.
        # Head radius 5 and center-to-neck distance 13 prove exact 8 centerline / 4 ink clearance.
        circle(self,'head',27,8,5)
        self.add_line('torso',(22,20),(17,32))
        self.add_polyline('arms',(22,20),(30,26),(40,24))
        self.add_polyline('pedaling-leg',(17,32),(25,35),(21,41),(25,41))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','pedaling-leg')
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
        self.add_polyline('handle-support',(40,24),(43,23),(36,38))
        path(self,'housing',(11,32),[('A',7,38,7,7,False),('A',13,44,6,6,False),('L',40,44),('A',42,40,3,3,False),('L',32,37)])
        self.add_line('saddle',(12,31),(18,31))
        self.add_line('crank',(25,41),(29,38))
        self.relate('connect','crank','pedaling-leg')
