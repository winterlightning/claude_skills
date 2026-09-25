"""Simple Ashram Building.

Plan: Gabled roof, projecting eaves and centered arched doorway retained. Omitted the extra ground-line extension and roof baseline to keep the small facade open. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide house: centered doorway and mirrored shell; eaves retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bf54c99-5c2d-4ba6-8a92-8e2924d208d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/ashram_6bf54c99-5c2d-4ba6-8a92-8e2924d208d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-gabled-building-with-an-arch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('small', 'gabled', 'building', 'with', 'an', 'arch')

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

        poly('roof',(6,22),(24,6),(42,22))
        path('walls',(10,18),[('L',(10,38)),('A',(14,42),4,4,False),('L',(34,42)),('A',(38,38),4,4,False),('L',(38,18))])
        join('roof','walls')
        path('door',(20,42),[('L',(20,32)),('A',(24,28),4,4,True),('A',(28,32),4,4,True),('L',(28,42))]);join('door','walls')
