"""Simple Farm Chicken Hen.

Plan: Right-facing hen, small beak, raised left tail and one foot retained. Small crest/wattle details simplified into the head silhouette. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8d6f09a-0963-413b-9f3e-2fdf85be5892'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/capon_a8d6f09a-0963-413b-9f3e-2fdf85be5892.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-hen-with-raised-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('standing', 'hen', 'with', 'raised', 'tail')

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

        path('hen',(36,8),[('C',(28,15),(30,8),(28,10)),('C',(19,22),(28,20),(24,22)),('C',(4,12),(12,22),(7,12)),('L',(6,26)),('C',(23,32),(6,31),(14,32)),('C',(40,24),(35,32),(40,30)),('L',(40,20)),('L',(44,17)),('L',(40,14)),('C',(36,8),(42,10),(40,8))],True)
        poly('foot',(23,32),(23,40),(30,40));join('foot','hen')
