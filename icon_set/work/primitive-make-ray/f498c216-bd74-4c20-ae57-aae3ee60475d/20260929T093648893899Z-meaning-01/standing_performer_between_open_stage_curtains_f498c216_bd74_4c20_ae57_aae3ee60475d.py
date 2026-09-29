from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f498c216-bd74-4c20-ae57-aae3ee60475d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-performer-between-open-stage-curtains/20260929T093049Z-thuan-mac/reference/show person_f498c216-bd74-4c20-ae57-aae3ee60475d.svg'
AUTHOR = 'gpt-6'
# Reference comparison: The rejected performer is only a head above a tiny forked mark; the curtains have harsh angular inner edges.
# Revision: Restore a full standing performer, curved tied-back curtains and the stage opening.
# Construction references inspected: human_ref/full_body_ref.png; Lucide theater and person-standing

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
    icon_id = 'standing-performer-between-open-stage-curtains'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('show', 'person')
    def build(self):
        # Stage root owns mirrored drapes and a complete central standing figure.
        # Curtain arcs meet the frame at true shared tie-back points.
        self.add_polyline('frame',(14,42),(6,42),(6,26),(6,6),(16,6),(32,6),(42,6),(42,26),(42,42),(34,42))
        path(self,'left-drape',(16,6),[('A',6,26,10,20,True),('A',14,42,8,16,True)])
        path(self,'right-drape',(32,6),[('A',42,26,10,20,False),('A',34,42,8,16,False)])
        self.relate('connect','frame','left-drape')
        self.relate('connect','frame','right-drape')
        circle(self,'head',24,16,4)
        self.add_line('torso',(24,28),(24,35))
        self.add_polyline('arms',(18,32),(24,28),(30,32))
        self.add_polyline('legs',(20,42),(24,35),(28,42))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','legs')
        self.mark_human_figure('performer',head='head',torso='torso',torso_junction='start')
