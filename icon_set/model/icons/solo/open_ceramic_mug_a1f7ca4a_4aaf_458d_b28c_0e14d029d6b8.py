"""Simple Ceramic Coffee Mug.

Plan: Open oval rim, rounded mug body and broad attached handle retained. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide coffee: rounded cup and attached handle; source elliptical rim retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1f7ca4a-4aaf-458d-b28c-0e14d029d6b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mug_a1f7ca4a-4aaf-458d-b28c-0e14d029d6b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-ceramic-mug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'ceramic', 'mug')

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

        path('rim',(6,12),[('C',(19,6),(6,8),(12,6)),('C',(32,12),(26,6),(32,8)),('C',(19,18),(32,16),(26,18)),('C',(6,12),(12,18),(6,16))],True)
        path('body',(6,12),[('L',(6,34)),('A',(14,42),8,8,False),('L',(24,42)),('A',(32,34),8,8,False),('L',(32,12))]);join('body','rim')
        path('handle',(32,20),[('L',(38,20)),('A',(42,24),4,4,True),('L',(42,28)),('A',(38,32),4,4,True),('L',(32,32))]);join('handle','body')
