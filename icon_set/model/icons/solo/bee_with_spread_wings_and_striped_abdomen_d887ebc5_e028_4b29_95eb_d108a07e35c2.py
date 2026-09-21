"""Flying Honey Bee.

Plan: Bee with spread wings, antennae, body bands and pointed abdomen. Bounds6,6,42,42. Omit tiny legs.
Construction reference: bug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd887ebc5-e028-4b29-95eb-d108a07e35c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sting_d887ebc5-e028-4b29-95eb-d108a07e35c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bee-with-spread-wings-and-striped-abdomen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bee', 'with', 'spread', 'wings', 'and', 'striped', 'abdomen')

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

        path('body',(18,16),[('A',(24,10),6,6,True),('A',(30,16),6,6,True),('L',(30,30)),('L',(24,42)),('L',(18,30)),('L',(18,16))],True)
        line('band',(18,26),(30,26));join('band','body')
        line('antenna-left',(18,16),(14,6));line('antenna-right',(30,16),(34,6));join('antenna-left','body');join('antenna-right','body')
        path('wing-left',(18,16),[('C',(6,20),(8,12),(6,14)),('C',(18,26),(6,30),(12,30))]);join('wing-left','body')
        path('wing-right',(30,16),[('C',(42,20),(40,12),(42,14)),('C',(30,26),(42,30),(36,30))]);join('wing-right','body')
