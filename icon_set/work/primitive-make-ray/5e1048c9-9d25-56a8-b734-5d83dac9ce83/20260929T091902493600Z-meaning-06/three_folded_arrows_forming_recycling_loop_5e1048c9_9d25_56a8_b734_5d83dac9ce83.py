from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5e1048c9-9d25-56a8-b734-5d83dac9ce83'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-folded-arrows-forming-recycling-loop/20260929T091350Z-thuan-mac/reference/recycling sign_5e1048c9-9d25-56a8-b734-5d83dac9ce83.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Single-stroke arrows omit the broad folded ribbon construction.
# Revision: Restore three broad closed ribbon arrows in a triangular cycle.
# Construction references inspected: recycle

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
    icon_id = 'three-folded-arrows-forming-recycling-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('recycling', 'sign')
    def build(self):
        # Three broad ribbon arrows form a clockwise triangular loop; arrow polygons own their directional points.
        self.add_polyline('top-arrow',(14,6),(25,6),(34,19),(39,16),(35,28),(23,25),(27,22),(19,12),(11,12),closed=True)
        self.add_polyline('bottom-arrow',(42,30),(35,42),(20,42),(20,46),(9,38),(20,30),(20,35),(31,35),(35,28),closed=True)
        self.add_polyline('left-arrow',(10,33),(4,24),(12,12),(8,9),(21,8),(23,20),(18,17),(11,26),(15,33),closed=True)
