from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5af5ae7c-c36a-44e3-b9a3-a6d9683548ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-fanned-playing-cards/20260929T091350Z-thuan-mac/reference/card game cards_5af5ae7c-c36a-44e3-b9a3-a6d9683548ab.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Cards are axis-aligned stacked rectangles rather than fanned playing cards.
# Revision: Restore three angularly fanned cards and a clear diamond suit.
# Construction references inspected: layers, diamond

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
    icon_id = 'three-fanned-playing-cards'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('card', 'game', 'cards')
    def build(self):
        # Three cards fan about the lower area; front card owns the diamond suit.
        self.add_polyline('back-card',(16,12),(4,17),(12,39),(17,37))
        self.add_polyline('middle-card',(16,29),(16,8),(33,8),(33,12))
        self.add_polyline('front-card',(27,13),(44,20),(35,40),(18,33),closed=True)
        self.add_polyline('diamond',(31,23),(34,28),(29,31),(26,26),closed=True)
