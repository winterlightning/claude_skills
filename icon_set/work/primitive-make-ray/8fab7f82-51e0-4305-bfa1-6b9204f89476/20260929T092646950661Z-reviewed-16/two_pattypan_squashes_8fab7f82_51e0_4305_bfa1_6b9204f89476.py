from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8fab7f82-51e0-4305-bfa1-6b9204f89476'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-pattypan-squashes/20260929T091350Z-thuan-mac/reference/patty pan squashes_8fab7f82-51e0-4305-bfa1-6b9204f89476.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Small cloud-like blobs lose the broad scalloped squash bodies and lobes.
# Revision: Restore two offset scalloped squashes, stalks and sparse curved rib marks.
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
    icon_id = 'two-pattypan-squashes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('patty', 'pan', 'squashes')
    def build(self):
        # Each pattypan has a scalloped saucer silhouette and short stalk; foreground overlaps the rear fruit.
        path(self,'rear',(20,23),[('L',19,17),('A',23,10,6,5,True),('A',31,9,7,4,True),('A',39,13,6,4,True),('A',42,21,5,5,True),('A',32,26,11,5,True)])
        self.add_polyline('rear-stem',(31,9),(34,4),(37,5))
        path(self,'front',(6,30),[('A',12,24,8,6,True),('A',20,24,6,4,True),('A',28,28,7,4,True),('A',31,35,5,5,True),('A',22,42,12,7,True),('A',10,38,12,7,True),('A',6,30,6,6,True)],True)
        self.add_polyline('front-stem',(13,23),(14,18),(17,17))
        path(self,'front-rib',(23,30),[('A',20,37,12,12,True)])
        path(self,'rear-rib',(34,14),[('A',33,19,9,9,True)])

# User explicitly delegated exceptions after visual UI/UX review.
Drawing.exception = {'reason': 'Two scalloped squash bodies, stems and curved rib cues need compact occlusion and detail clearances. The organic silhouette deliberately differs from the rectangular envelope.', 'approved_by': 'user-authorized visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd274510192b00fad9c16b4a861125177244f1021356c11e99c18ccd153d6383c'}
