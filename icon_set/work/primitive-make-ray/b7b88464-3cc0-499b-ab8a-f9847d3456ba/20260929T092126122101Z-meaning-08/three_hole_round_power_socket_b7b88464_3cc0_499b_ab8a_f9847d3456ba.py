from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b7b88464-3cc0-499b-ab8a-f9847d3456ba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-hole-round-power-socket/20260929T091350Z-thuan-mac/reference/power outlet type k_b7b88464-3cc0-499b-ab8a-f9847d3456ba.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Missing square faceplate makes the outlet read as a face.
# Revision: Restore the square faceplate, circular socket and type-K grounding slot.
# Construction references inspected: circle

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
    icon_id = 'three-hole-round-power-socket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'k')
    def build(self):
        # Square faceplate contains a round recess; two pin holes and flat-topped earth aperture identify type K.
        rect(self,'faceplate',4,4,40,40,5)
        circle(self,'socket',24,24,13)
        for x in (19,29): self.add_dot(f'pin-{x}',(x,19))
        path(self,'earth',(20,27),[('L',28,27),('A',20,27,4,4,True)],True)
