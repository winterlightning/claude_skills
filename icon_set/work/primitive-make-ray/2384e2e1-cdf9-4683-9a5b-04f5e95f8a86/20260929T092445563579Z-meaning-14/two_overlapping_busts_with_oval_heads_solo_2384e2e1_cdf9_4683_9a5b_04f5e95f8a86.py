from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2384e2e1-cdf9-4683-9a5b-04f5e95f8a86'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-overlapping-busts-with-oval-heads-solo/20260929T091350Z-thuan-mac/reference/spouse_2384e2e1-cdf9-4683-9a5b-04f5e95f8a86.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Joined parallel busts read as an undifferentiated group with no overlap.
# Revision: Restore a front bust and visibly occluded rear bust with separate round heads.
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
    icon_id = 'two-overlapping-busts-with-oval-heads-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('spouse',)
    def build(self):
        # Two circular heads share radius six. Front bust occludes the left edge of the rear bust.
        circle(self,'front-head',15,12,6)
        circle(self,'rear-head',35,12,6)
        path(self,'front-body',(6,42),[('L',6,35),('A',15,26,9,9,True),('A',24,35,9,9,True),('L',24,42)])
        path(self,'rear-body',(31,27),[('A',35,26,9,9,True),('A',42,33,7,7,True),('L',42,42)])
