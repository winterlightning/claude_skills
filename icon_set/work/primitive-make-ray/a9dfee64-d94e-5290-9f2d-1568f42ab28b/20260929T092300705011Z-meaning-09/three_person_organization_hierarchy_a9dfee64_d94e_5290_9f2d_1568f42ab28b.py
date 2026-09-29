from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a9dfee64-d94e-5290-9f2d-1568f42ab28b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-person-organization-hierarchy/20260929T091350Z-thuan-mac/reference/workflow teamwork hierarchy_a9dfee64-d94e-5290-9f2d-1568f42ab28b.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Merged head/body outlines and diagonal lines obscure the organization chart.
# Revision: Use separate circular heads, open bust shoulders and orthogonal hierarchy connectors.
# Construction references inspected: network; human_ref/user.svg

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
    icon_id = 'three-person-organization-hierarchy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('workflow', 'teamwork', 'hierarchy')
    def build(self):
        # Source uses genuine continuous necks, not detached heads. Three identical portrait outlines sit on an orthogonal chart.
        for name,cx,cy in [('leader',24,8),('left',12,32),('right',36,32)]:
         path(self,name,(cx-3,cy+4),[('A',cx-4,cy,4,4,True),('A',cx+4,cy,4,4,True),('A',cx+3,cy+4,4,4,True),('L',cx+7,cy+8),('L',cx+7,cy+12),('L',cx-7,cy+12),('L',cx-7,cy+8),('L',cx-3,cy+4)],True)
        self.add_line('trunk',(24,20),(24,24))
        self.add_polyline('branch',(12,27),(12,24),(24,24),(36,24),(36,27))
        self.relate('connect','trunk','branch')
        self.relate('connect','trunk','leader')
