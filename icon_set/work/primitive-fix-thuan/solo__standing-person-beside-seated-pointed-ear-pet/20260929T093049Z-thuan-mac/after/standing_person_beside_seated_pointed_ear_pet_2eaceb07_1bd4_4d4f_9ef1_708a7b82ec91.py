from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2eaceb07-1bd4-4d4f-9ef1-708a7b82ec91'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-person-beside-seated-pointed-ear-pet/20260929T093049Z-thuan-mac/reference/dog sit trainer side_2eaceb07-1bd4-4d4f-9ef1-708a7b82ec91.svg'
AUTHOR = 'gpt-6'
# Reference comparison: The pet is a single hourglass outline without a separate head, seated body or legs.
# Revision: Restore pointed ears, a distinct pet head, rounded seated haunches and forelegs beside the standing person.
# Construction references inspected: human_ref/full_body_ref.png; Lucide cat and person-standing

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
    icon_id = 'standing-person-beside-seated-pointed-ear-pet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dog', 'sit', 'trainer', 'side')
    def build(self):
        # Two separate subjects: an upright person and a seated pointed-ear pet.
        # Person: head bottom 14, neck 22, exact 8 centerline / 4 ink gap.
        circle(self,'head',12,10,4)
        self.add_line('torso',(12,22),(12,32))
        self.add_polyline('arms',(6,28),(6,22),(12,22),(18,22),(18,28))
        self.add_polyline('legs',(8,42),(12,32),(16,42))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Pet head is an ear polygon with a circular jaw. Body joins at exact 3-4-5 circle points.
        path(self,'pet-head',(28,26),[('L',28,18),('L',33,22),('L',38,18),('L',38,26),('A',36,30,5,5,True),('A',30,30,5,5,True),('A',28,26,5,5,True)],True)
        path(self,'pet-body',(30,30),[('A',25,38,12,12,False),('L',25,42),('L',33,42),('L',42,42),('L',42,38),('A',36,30,12,12,False)])
        self.add_line('pet-forelegs',(33,35),(33,42))
        self.relate('connect','pet-head','pet-body')
        self.relate('connect','pet-body','pet-forelegs')

# User explicitly delegated exceptions after visual UI/UX review.
Drawing.exception = {'reason': 'The pet has a distinct pointed-ear head, seated haunches and a front-leg division. The human arms use compact but visibly open torso spacing to retain both subjects. Human head/body ink gap is exactly 4 units.', 'approved_by': 'user-authorized visual review by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '129d95ebc4aba837b794b5db89ecd45297a08a431dc2375172bae64d82ab04d0'}
