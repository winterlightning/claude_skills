"""Simple Baby Carriage.

Plan: Raised hood, open cradle, curved handle and two detached wheels retained. The cradle is shallower to provide clear wheel spacing. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a79b7f1e-da1e-4ce2-8f22-1f2a0f3572eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby carriage_a79b7f1e-da1e-4ce2-8f22-1f2a0f3572eb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-baby-carriage-with-raised-hood'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('round', 'baby', 'carriage', 'with', 'raised', 'hood')

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

        path('cradle',(14,18),[('L',(28,18)),('L',(28,6)),('C',(42,18),(36,6),(42,10)),('C',(28,26),(42,23),(36,26)),('C',(14,18),(20,26),(14,23))],True)
        path('handle',(6,10),[('C',(14,18),(14,10),(14,10))]);join('handle','cradle')
        for x in [18,38]:circle(f'wheel{x}',x,38,4)
