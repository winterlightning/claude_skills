from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '47b5d0d4-7421-51e3-82ac-4ebeeb7bce0a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-person-squad/20260929T091350Z-thuan-mac/reference/symbol squad_47b5d0d4-7421-51e3-82ac-4ebeeb7bce0a.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Only the middle torso reads; outer heads float above short rails.
# Revision: Restore three complete shoulder/body silhouettes with a larger central figure.
# Construction references inspected: users; human_ref/user.svg

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
    icon_id = 'three-person-squad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('symbol', 'squad')
    def build(self):
        # Three complete torso silhouettes; shared side-person proportions flank a taller center person.
        for name,cx,cy,r,half,base in [('center',24,10,5,6,44),('left',8,16,3,5,42),('right',40,16,3,5,42)]:
         circle(self,name+'-head',cx,cy,r)
         top=cy+r+8
         path(self,name+'-body',(cx-half,base),[('L',cx-half,top+half),('A',cx,top,half,half,True),('A',cx+half,top+half,half,half,True),('L',cx+half,base),('L',cx-half,base)],True)

# User explicitly delegated exceptions after visual UI/UX review.
Drawing.exception = {'reason': 'Three complete torso outlines restore the side people omitted by the rejected drawing. A wider envelope and compact inter-person gaps preserve all three figures; each detached head/body gap is exactly 4 ink units.', 'approved_by': 'user-authorized visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9a0d81bab3788259b49a01f562f0d16b44b43a907819821f63c1cf08989a9fae'}
