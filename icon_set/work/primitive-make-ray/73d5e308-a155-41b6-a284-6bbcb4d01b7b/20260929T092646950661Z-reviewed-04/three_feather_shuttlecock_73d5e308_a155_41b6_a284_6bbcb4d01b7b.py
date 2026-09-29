from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '73d5e308-a155-41b6-a284-6bbcb4d01b7b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-feather-shuttlecock/20260929T091350Z-thuan-mac/reference/badminton_73d5e308-a155-41b6-a284-6bbcb4d01b7b.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Flat triangular fan loses the three rounded feathers and diagonal sporting silhouette.
# Revision: Use three rounded feather tips, converging ribs and a domed cork.
# Construction references inspected: no useful subject match

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
    icon_id = 'three-feather-shuttlecock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('badminton',)
    def build(self):
        # Three equal visual feather widths converge to a cork band; rounded tips replace the rejected straight rim.
        path(self,'left-feather',(17,32),[('L',8,12),('A',18,10,6,6,True),('L',21,32)])
        path(self,'middle-feather',(18,10),[('A',30,10,6,6,True),('L',27,32)])
        path(self,'right-feather',(30,10),[('A',40,12,6,6,True),('L',31,32)])
        path(self,'cork',(17,32),[('L',31,32),('L',31,37),('A',17,37,7,7,True),('L',17,32)],True)
        for a,b in [('left-feather','middle-feather'),('middle-feather','right-feather'),('left-feather','cork'),('middle-feather','cork'),('right-feather','cork')]: self.relate('connect',a,b)

# User explicitly delegated exceptions after visual UI/UX review.
Drawing.exception = {'reason': 'Three rounded feather tips, converging ribs and the cork define the shuttlecock. Internal taper advisories are intentional feather convergence, reviewed at 48px.', 'approved_by': 'user-authorized visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '1db4705fc2ec9adf901c9f90ab80dc3bb0654c554e1d70774b16f3634d51ef12'}
