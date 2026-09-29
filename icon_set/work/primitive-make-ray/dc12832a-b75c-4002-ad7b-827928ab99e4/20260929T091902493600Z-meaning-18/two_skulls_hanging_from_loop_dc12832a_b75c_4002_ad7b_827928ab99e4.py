from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dc12832a-b75c-4002-ad7b-827928ab99e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-skulls-hanging-from-loop/20260929T091350Z-thuan-mac/reference/fantasy medieval bounty hunter 1_dc12832a-b75c-4002-ad7b-827928ab99e4.svg'
AUTHOR = 'gpt-6'
# Reference comparison: Skulls look like bags; suspension ropes and cranial details are unclear.
# Revision: Restore a centered hanging loop, two cords and two rounded skulls with paired sockets and teeth.
# Construction references inspected: skull

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
    icon_id = 'two-skulls-hanging-from-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('fantasy', 'medieval', 'bounty', 'hunter', '1')
    def build(self):
        # Centered ring suspends two skulls. Each skull owns its dome, squared jaw, paired eyes and tooth notch.
        circle(self,'loop',24,7,3)
        self.add_line('left-cord',(22,10),(15,18))
        self.add_line('right-cord',(26,10),(34,18))
        for name,cx,cy in [('left',14,27),('right',35,29)]:
         path(self,name+'-skull',(cx-8,cy),[('A',cx+8,cy,8,9,True),('L',cx+8,cy+5),('L',cx+5,cy+7),('L',cx+5,cy+13),('L',cx-5,cy+13),('L',cx-5,cy+7),('L',cx-8,cy+5),('L',cx-8,cy)],True)
         for dx in (-3,3): self.add_dot(name+f'-eye-{dx}',(cx+dx,cy+1))
         self.add_line(name+'-teeth',(cx,cy+10),(cx,cy+13))
         self.relate('connect',name+'-skull',name+'-teeth')
