"""Polished Diamond Gemstone.

Plan: Broad-crown diamond bounds4,8,44,40. Restore complete pointed bottom from imperfect source; retain triangular crown.
Construction reference: Lucide gem: symmetric polygon and shared facet nodes
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'baab004f-5043-4b98-8464-4a3953727534'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sketch logo_baab004f-5043-4b98-8464-4a3953727534.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'faceted-diamond-with-broad-crown'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('faceted', 'diamond', 'with', 'broad', 'crown')

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

        poly('outline',(12,8),(24,8),(36,8),(44,20),(24,40),(4,20),closed=True)
        poly('belt',(4,20),(16,20),(32,20),(44,20))
        poly('facets',(24,8),(16,20),(24,40),(32,20),(24,8))
        join('outline','belt');join('outline','facets');join('belt','facets')
