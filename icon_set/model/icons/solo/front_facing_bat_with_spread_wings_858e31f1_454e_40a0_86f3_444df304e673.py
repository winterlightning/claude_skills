"""Flying Spooky Halloween Bat.

Plan: Bat silhouette with tall ears, wide wings and scalloped lower edge; bounds4,8,44,40. Drop tiny face marks.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '858e31f1-454e-40a0-86f3-444df304e673'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bat fly_858e31f1-454e-40a0-86f3-444df304e673.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-bat-with-spread-wings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('front', 'facing', 'bat', 'with', 'spread', 'wings')

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
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('bat',(4,10),[('C',(16,20),(8,18),(12,20)),('L',(18,8)),('L',(24,14)),('L',(30,8)),('L',(32,20)),('C',(44,10),(36,20),(40,18)),('C',(42,36),(44,20),(44,30)),('C',(32,34),(38,28),(34,28)),('C',(24,40),(28,30),(26,34)),('C',(16,34),(22,34),(20,30)),('C',(6,36),(14,28),(10,28)),('C',(4,10),(4,30),(4,20))],True)
