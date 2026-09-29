from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '437cffd5-c767-5db6-a77e-e9e439fd74c2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-curved-blade-wind-turbine-on-tapered-mast/20260929T091350Z-thuan-mac/reference/renewable energy wind turbine_437cffd5-c767-5db6-a77e-e9e439fd74c2.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Rotor resembles a flower and mast is a single stalk.
# Revision: Restore swept blades around a distinct hub and a tapered mast.
# Construction references inspected: no useful turbine match; circle

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
    icon_id = 'three-curved-blade-wind-turbine-on-tapered-mast'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('renewable', 'energy', 'wind', 'turbine')
    def build(self):
        # Three swept rotor blades and a narrow tapered support; asymmetric blade directions are intentional.
        circle(self,'hub',24,19,3)
        path(self,'blade-up',(22,16),[('L',23,4),('A',29,13,9,9,True),('L',27,17)])
        path(self,'blade-left',(21,19),[('A',8,31,17,17,False),('L',19,25),('L',23,22)])
        path(self,'blade-right',(27,19),[('L',40,27),('A',27,25,12,12,True),('L',25,22)])
        self.add_polyline('mast',(22,27),(19,44),(29,44),(26,27))
        self.add_line('ground',(8,44),(40,44))
        self.relate('connect','mast','ground')
