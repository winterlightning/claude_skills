from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ea71018-0faa-5fbf-aeb4-02467c816835'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-flame-stove-burner/20260929T091350Z-thuan-mac/reference/stove gas_8ea71018-0faa-5fbf-aeb4-02467c816835.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Flames read as drops and the burner has no support legs.
# Revision: Restore pointed flame shapes, rounded burner body and two legs.
# Construction references inspected: flame

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
    icon_id = 'three-flame-stove-burner'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('stove', 'gas')
    def build(self):
        # Flame instances share a teardrop construction; the central flame rises two units higher.
        for i,cx in enumerate((10,24,38)):
            top=6 if i==1 else 8
            path(self,f'flame-{i}',(cx,top),[('L',cx+3,top+5),('A',cx-3,top+5,3,4,True),('L',cx,top)],True)
        rect(self,'burner',6,25,36,10,3)
        for x in (14,34):
            self.add_line(f'leg-{x}',(x,35),(x,42))
            self.relate('connect','burner',f'leg-{x}')
        self.add_line('ground',(6,42),(42,42))
        for x in (14,34): self.relate('connect',f'leg-{x}','ground')
