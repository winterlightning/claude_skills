from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '56b4e71f-75e4-4a89-a34d-2644a8cfe823'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__turnover-pastry/20260929T091350Z-thuan-mac/reference/turnover_56b4e71f-75e4-4a89-a34d-2644a8cfe823.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Upright arch reads as a tunnel, not a folded pastry.
# Revision: Restore a diagonal turnover edge, rounded pastry crescent and short crimp marks.
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
    icon_id = 'turnover-pastry'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('turnover',)
    def build(self):
        # A semicircular pastry shell is cut by a sloping sealed edge; crimp marks follow that edge.
        path(self,'pastry',(6,40),[('A',42,31,19,27,True),('L',6,40)],True)
        path(self,'filling-ridge',(15,30),[('A',33,28,10,8,True)])
        for i,(x,y) in enumerate(((15,38),(24,36),(33,34))):
         self.add_line(f'crimp-{i}',(x,y),(x-1,y-3))

# User explicitly delegated exceptions after visual UI/UX review.
Drawing.exception = {'reason': 'The tilted pastry shell, inner ridge and crimped edge distinguish a turnover from a tunnel. The natural pastry aspect uses a shorter envelope and compact ridge spacing.', 'approved_by': 'user-authorized visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6e2d471e3bd1549f65e7bbb93cc865ee181ce27e6b61c9bba233ddc0686be493'}
