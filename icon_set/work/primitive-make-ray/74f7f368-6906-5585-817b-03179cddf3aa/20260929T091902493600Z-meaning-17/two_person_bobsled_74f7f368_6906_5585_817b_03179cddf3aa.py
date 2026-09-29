from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '74f7f368-6906-5585-817b-03179cddf3aa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-person-bobsled/20260929T091350Z-thuan-mac/reference/skiing bobsled_74f7f368-6906-5585-817b-03179cddf3aa.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Detached dots above an empty capsule omit both riders.
# Revision: Restore two heads with seated shoulder silhouettes above a shaped bobsled shell and runner.
# Construction references inspected: human_ref/user.svg; human_ref/full_body_ref.png

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
    icon_id = 'two-person-bobsled'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('skiing', 'bobsled')
    def build(self):
        # Two equal riders share circular heads and seated shoulders; shell has a rounded nose and lower runner.
        for i,cx in enumerate((14,29)):
         circle(self,f'rider-{i}-head',cx,10,4)
         path(self,f'rider-{i}-body',(cx-5,26),[('A',cx,22,5,4,True),('A',cx+5,26,5,4,True)])
        path(self,'shell',(6,27),[('L',32,27),('A',44,35,12,8,True),('A',38,38,6,3,True),('L',13,38),('A',6,27,7,11,True)],True)
        self.add_polyline('runner',(4,44),(38,44),(44,41))
        for x in (15,33): self.add_line(f'strut-{x}',(x,38),(x,44))
