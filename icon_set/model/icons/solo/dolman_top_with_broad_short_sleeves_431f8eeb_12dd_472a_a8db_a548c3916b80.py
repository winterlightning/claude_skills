"""Short Sleeve Dolman Top.

Plan: Retained the broad dolman sleeves, rounded neckline and curved hem. Simplified the short inner sleeve seams.
Construction reference: Lucide shirt: one connected garment silhouette and rounded neck opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '431f8eeb-12dd-472a-a8db-a548c3916b80'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dolman_431f8eeb-12dd-472a-a8db-a548c3916b80.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dolman-top-with-broad-short-sleeves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('dolman', 'top', 'with', 'broad', 'short', 'sleeves')

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

        path('shirt',(18,8),[('C',(30,8),(20,14),(28,14)),('C',(38,14),(34,8),(36,10)),('L',(44,22)),('L',(34,28)),('L',(36,38)),('C',(24,40),(32,40),(28,40)),('C',(12,38),(20,40),(16,40)),('L',(14,28)),('L',(4,22)),('L',(10,14)),('C',(18,8),(12,10),(14,8))],True)
