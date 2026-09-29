from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0291328f-6b9e-4cc3-80d5-84c234b92ad3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-buildings-beneath-cloud/20260929T091350Z-thuan-mac/reference/building cloudy_0291328f-6b9e-4cc3-80d5-84c234b92ad3.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Cloud is a cramped puff; buildings have no window cues.
# Revision: Enlarge cloud lobes and add sparse windows to three distinct roofs.
# Construction references inspected: cloud

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
    icon_id = 'three-buildings-beneath-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('building', 'cloudy')
    def build(self):
        # Root owns one large cloud and three joined, differently roofed buildings.
        path(self,'cloud',(10,19),[('A',10,11,4,4,True),('A',24,11,7,7,True),('A',24,19,4,4,True),('L',10,19)],True)
        self.add_polyline('low-building',(6,42),(6,33),(16,33),(16,42))
        self.add_polyline('house',(16,42),(16,28),(24,22),(32,28),(32,42))
        self.add_polyline('tower',(32,42),(32,6),(42,6),(42,42),(6,42))
        for y in (16,26): self.add_dot(f'window-{y}',(37,y))
        self.add_line('house-window',(24,32),(24,35))
        self.relate('connect','low-building','house')
        self.relate('connect','house','tower')
        self.relate('connect','low-building','tower')
