from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7f241b41-a40e-5d93-877e-90934b0259e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-overlapping-folders/20260929T091350Z-thuan-mac/reference/duplicate folder_7f241b41-a40e-5d93-877e-90934b0259e9.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Rear folder is an incomplete rail and front tab is exaggerated.
# Revision: Restore two clearly overlapping folder bodies with modest tabs.
# Construction references inspected: folder

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
    icon_id = 'two-overlapping-folders'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('duplicate', 'folder')
    def build(self):
        # Back folder has a visible left side and top tab; front folder occludes its lower-right portion.
        path(self,'rear',(6,33),[('L',6,8),('A',8,6,2,2,True),('L',17,6),('L',22,11),('L',35,11),('A',37,13,2,2,True),('L',37,16)])
        path(self,'front',(17,42),[('A',15,40,2,2,True),('L',15,22),('A',17,20,2,2,True),('L',24,20),('L',29,25),('L',40,25),('A',42,27,2,2,True),('L',42,40),('A',40,42,2,2,True),('L',17,42)],True)
