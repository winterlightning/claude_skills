"""Rocket Launch Over Globe.

Plan: Diagonal rocket over partial globe; bounds6,6,42,42. One exhaust stroke and one continent seam.
Construction reference: Lucide rocket diagonal nose and fin construction
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '316bef96-1836-4fb8-b6a2-7483304127ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rocket attack global_316bef96-1836-4fb8-b6a2-7483304127ec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rocket-passing-above-a-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rocket', 'passing', 'above', 'a', 'globe')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('rocket',(18,20),(30,8),(42,6),(40,18),(28,30),closed=True)
        line('fin',(18,20),(8,20));join('fin','rocket')
        line('exhaust',(6,32),(10,28))
        path('globe',(16,34),[('C',(30,42),(18,40),(24,42)),('C',(42,30),(38,42),(42,36))])
