from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b16280dc-c5f8-496c-99d7-eaecc0358b57'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__starfruit-with-star-cross-section/20260929T093049Z-thuan-mac/reference/starfruit_b16280dc-c5f8-496c-99d7-eaecc0358b57.svg'
AUTHOR = 'gpt-6'
# Reference comparison: The whole fruit is a featureless bean and the slice is a sharp generic star.
# Revision: Restore an elongated whole fruit with its diagonal longitudinal ridge and a softer five-lobed star-shaped slice.
# Construction references inspected: Lucide star; no useful whole-fruit match

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
    icon_id = 'starfruit-with-star-cross-section'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('starfruit',)
    def build(self):
        # A ridged elongated whole fruit sits behind its five-lobed cross-section.
        # Star points use coherent shallow arcs instead of a generic sharp badge.
        path(self,'whole-fruit',(15,36),[('A',8,34,10,8,True),('A',32,6,25,25,True),('A',35,17,13,13,True)])
        self.add_line('ridge',(8,34),(32,6))
        self.relate('connect','whole-fruit','ridge')
        path(self,'slice',(30,18),[('A',35,26,15,15,True),('A',44,28,17,17,True),('A',38,34,18,18,True),('A',39,44,19,19,True),('A',30,40,17,17,True),('A',21,44,17,17,True),('A',22,34,19,19,True),('A',16,28,18,18,True),('A',25,26,17,17,True),('A',30,18,15,15,True)],True)
        self.add_dot('seed-core',(30,33))
