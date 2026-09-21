"""Faceted Mineral Ore Rock.

Plan: Broad irregular rock with two strong seam branches; bounds6,6,42,42. Drop isolated tiny facet dash.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9fe232b-4dc9-433c-87f6-0acf2c03952b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ore_b9fe232b-4dc9-433c-87f6-0acf2c03952b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angular-faceted-ore-rock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('angular', 'faceted', 'ore', 'rock')

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

        poly('rock',(20,6),(36,10),(42,26),(34,38),(18,42),(6,28),(10,14),closed=True)
        poly('seam',(36,10),(21,23),(18,42));join('seam','rock')
        line('left-facet',(6,28),(21,23));join('left-facet','rock');join('left-facet','seam')
