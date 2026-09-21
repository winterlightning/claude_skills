"""Search Magnifying Glass.

Plan: Retained the circular lens and long lower-right handle. Preserved this separate source UUID even though its concept matches the neighboring reference.
Construction reference: Lucide search: true circular lens and one connected diagonal handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd77748e7-f42b-400a-a0ae-6bd2d336ef2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/magnifying glass_d77748e7-f42b-400a-a0ae-6bd2d336ef2b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'magnifying-glass-with-long-diagonal-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('magnifying', 'glass', 'with', 'long', 'diagonal', 'handle')

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

        path('lens',(6,21),[('A',(21,6),15,15,True),('A',(30,33),15,15,True),('A',(6,21),15,15,True)],True)
        line('handle',(30,33),(42,42));join('handle','lens')
