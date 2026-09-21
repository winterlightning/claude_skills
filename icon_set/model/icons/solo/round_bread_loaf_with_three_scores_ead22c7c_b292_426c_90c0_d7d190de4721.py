"""Round Loaf of Bread.

Plan: Broad bread loaf and three scoring cuts; bounds4,10,44,38.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ead22c7c-b292-426c-90c0-d7d190de4721'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dough_ead22c7c-b292-426c-90c0-d7d190de4721.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-bread-loaf-with-three-scores'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('round', 'bread', 'loaf', 'with', 'three', 'scores')

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

        path('loaf',(4,28),[('C',(24,10),(4,16),(14,10)),('C',(44,28),(34,10),(44,16)),('C',(34,38),(44,37),(42,38)),('L',(14,38)),('C',(4,28),(6,38),(4,37))],True)
        for x in (14,24,34): line('score-'+str(x),(x,23),(x,27))
