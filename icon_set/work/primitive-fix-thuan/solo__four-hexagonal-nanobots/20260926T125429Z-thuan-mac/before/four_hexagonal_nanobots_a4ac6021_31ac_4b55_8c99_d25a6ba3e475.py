"""Set of Hexagonal Nanobots.

Plan: Retained all four hexagonal nanobots in a two-by-two arrangement and their side appendages. Removed tiny center circles and shortened the bottom appendages to the body points.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4ac6021-31ac-4b55-8c99-d25a6ba3e475'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nanobots 1_a4ac6021-31ac-4b55-8c99-d25a6ba3e475.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-hexagonal-nanobots'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'science'
    categories = ('science', 'primitive', 'primitives')
    aliases = ()
    keywords = ('four', 'hexagonal', 'nanobots')

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

        for i,(x,y) in enumerate([(12,12),(36,12),(12,34),(36,34)]):
         name='bot-'+str(i)
         poly(name,(x,y-6),(x+6,y-3),(x+6,y+3),(x,y+6),(x-6,y+3),(x-6,y-3),(x,y-6),closed=True)
         for suffix,a,b in [('left',(x-6,y+3),(x-6,y+8)),('right',(x+6,y+3),(x+6,y+8)),('foot',(x,y+6),(x,y+6))]:
          line(name+suffix,a,b);join(name+suffix,name)
