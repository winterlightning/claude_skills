from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '86b37e1a-0047-497f-8897-cc61b8ea2db2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-tower-suspension-bridge/20260929T091350Z-thuan-mac/reference/bridge golden gate_86b37e1a-0047-497f-8897-cc61b8ea2db2.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Thick arch silhouette and wavy deck lose suspended cable construction.
# Revision: Use slim towers, sagging cables, vertical suspenders, a straight deck and water below.
# Construction references inspected: no useful bridge match

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
    icon_id = 'two-tower-suspension-bridge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('bridge', 'golden', 'gate')
    def build(self):
        # Two towers support a broad sagging central cable and a straight deck. Quarter ellipses meet tangentially at the sag.
        for x in (12,36): self.add_line(f'tower-{x}',(x,6),(x,36))
        path(self,'cable',(4,26),[('A',12,10,22,22,False),('A',24,24,12,14,False),('A',36,10,12,14,False),('A',44,26,22,22,False)])
        self.add_line('deck',(4,28),(44,28))
        self.add_line('central-suspender',(24,24),(24,28))
        self.relate('connect','central-suspender','cable')
        self.relate('connect','central-suspender','deck')
        path(self,'water',(4,42),[('A',14,42,7,4,False),('A',24,42,7,4,True),('A',34,42,7,4,False),('A',44,42,7,4,True)])
