"""Fairy Tale Castle with Flags.

Plan: Three roofed towers with central pennant, stepped wall and doorway; bounds6,6,42,42. Retain one broad flag instead of three tiny flags.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3c19f77-a991-4b79-b14f-5d47ca735c7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amusement park castle_f3c19f77-a991-4b79-b14f-5d47ca735c7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-tower-castle-with-flags'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'tower', 'castle', 'with', 'flags')

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

        poly('walls',(6,26),(6,42),(18,42),(18,34),(30,34),(30,42),(42,42),(42,26),(30,26),(30,18),(18,18),(18,26),closed=True)
        poly('roof-left',(6,26),(12,16),(18,26));join('roof-left','walls')
        poly('roof-right',(30,26),(36,16),(42,26));join('roof-right','walls')
        poly('roof-mid',(18,18),(24,8),(30,18));join('roof-mid','walls')
        poly('flag',(24,8),(24,6),(32,6)) ;join('flag','roof-mid')
