"""Simple House with Door and Window.

Plan: Gabled house and left door retained; the right window is enlarged to meet the outer jamb, avoiding a narrow wall strip. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide house: gabled shell and shared doorway, window retained as a broad opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9d1ebd7-328b-4326-8efc-3c4aca3bef77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/atelier_f9d1ebd7-328b-4326-8efc-3c4aca3bef77.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gabled-house-with-one-square-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('gabled', 'house', 'with', 'one', 'square', 'window')

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

        poly('roof',(6,18),(24,6),(42,18))
        poly('walls',(6,18),(6,42),(42,42),(42,18));join('roof','walls')
        poly('door',(14,42),(14,30),(22,30),(22,42));join('door','walls')
        poly('window',(42,22),(30,22),(30,30),(42,30));join('window','walls')
