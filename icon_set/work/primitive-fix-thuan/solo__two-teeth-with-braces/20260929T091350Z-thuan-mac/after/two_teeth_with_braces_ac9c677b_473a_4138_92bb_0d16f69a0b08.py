from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ac9c677b-473a-4138-92bb-0d16f69a0b08'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-teeth-with-braces/20260929T091350Z-thuan-mac/reference/dental brace_ac9c677b-473a-4138-92bb-0d16f69a0b08.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Tooth roots taper to a single point and brackets become vertical dashes.
# Revision: Restore bifurcated tooth roots and visible square brackets joined by the archwire.
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
    icon_id = 'two-teeth-with-braces'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dental', 'brace')
    def build(self):
        # Mirrored molars have two rounded roots; archwire passes through square brackets.
        for name,cx in [('left',13),('right',35)]:
         path(self,name+'-tooth',(cx-8,17),[('A',cx-4,10,5,7,True),('A',cx+4,10,5,4,False),('A',cx+8,17,5,7,True),('L',cx+6,34),('A',cx+2,34,2,3,True),('L',cx+1,29),('A',cx-1,29,1,2,False),('L',cx-2,34),('A',cx-6,34,2,3,True),('L',cx-8,17)],True)
         self.add_polyline(name+'-bracket',(cx-3,19),(cx+3,19),(cx+3,25),(cx-3,25),closed=True)
        self.add_line('wire-left',(4,22),(10,22))
        self.add_line('wire-middle',(16,22),(32,22))
        self.add_line('wire-right',(38,22),(44,22))

# User explicitly delegated exceptions after visual UI/UX review.
Drawing.exception = {'reason': 'Two-root molars and square brackets joined by an archwire define dental braces. Small bracket openings and tapered roots remain legible, with automatic small-opening advisories retained.', 'approved_by': 'user-authorized visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '522e0c64290f8990c5f80b82109219991791e9a9052a31a2f2583c7f93430ee8'}
