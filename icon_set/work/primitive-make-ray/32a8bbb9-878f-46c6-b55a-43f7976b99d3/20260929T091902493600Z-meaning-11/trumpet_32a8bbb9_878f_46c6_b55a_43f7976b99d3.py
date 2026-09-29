from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '32a8bbb9-878f-46c6-b55a-43f7976b99d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__trumpet/20260929T091350Z-thuan-mac/reference/trumpet_32a8bbb9-878f-46c6-b55a-43f7976b99d3.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Blunt bell and valve pins make an abstract symbol rather than a trumpet.
# Revision: Restore a flared bell, narrow mouthpiece, looped tubing and capped valves.
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
    icon_id = 'trumpet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('trumpet',)
    def build(self):
        # Mouthpiece feeds upper tube and flared bell; three capped valve stems intersect the tubing loop.
        self.add_line('mouthpiece',(4,20),(11,20))
        self.add_line('mouthpiece-rim',(4,17),(4,23))
        self.add_line('lead-pipe',(11,20),(32,20))
        self.add_polyline('bell',(32,20),(44,8),(44,32),(32,20))
        path(self,'tubing',(31,23),[('A',24,38,8,8,True),('L',16,38),('A',16,22,8,8,True),('L',31,22)])
        for x in (16,23,30):
         self.add_line(f'valve-{x}',(x,15),(x,31))
         self.add_line(f'cap-{x}',(x-2,15),(x+2,15))
         self.relate('connect',f'valve-{x}',f'cap-{x}')
        self.relate('connect','mouthpiece','mouthpiece-rim')
        self.relate('connect','mouthpiece','lead-pipe')
        self.relate('connect','lead-pipe','bell')
