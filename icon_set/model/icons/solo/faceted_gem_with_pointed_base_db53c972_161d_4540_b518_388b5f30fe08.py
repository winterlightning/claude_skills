"""Facet Cut Diamond Gemstone.

Plan: Shared crown, girdle and lower tip. Bounds4,8,44,40. Two large triangular lower facets and wide central crown.
Construction reference: gem.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db53c972-161d-4540-b518-388b5f30fe08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/ruby_db53c972-161d-4540-b518-388b5f30fe08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'faceted-gem-with-pointed-base'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('faceted', 'gem', 'with', 'pointed', 'base')

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

        poly('gem',(4,20),(14,8),(34,8),(44,20),(24,40),closed=True)
        poly('girdle',(4,20),(16,20),(32,20),(44,20));join('gem','girdle')
        poly('left-facet',(14,8),(16,20),(24,40));poly('right-facet',(34,8),(32,20),(24,40))
        for n in ('left-facet','right-facet'):join(n,'gem');join(n,'girdle')
        join('left-facet','right-facet')
