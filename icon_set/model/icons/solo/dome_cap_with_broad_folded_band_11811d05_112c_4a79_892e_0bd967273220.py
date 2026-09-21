"""Simple Beanie Hat.

Plan: Rounded dome and broad folded band retained as shared contours. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11811d05-112c-4a79-892e-0bd967273220'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/skullcap_11811d05-112c-4a79-892e-0bd967273220.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dome-cap-with-broad-folded-band'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('dome', 'cap', 'with', 'broad', 'folded', 'band')

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

        path('dome',(4,28),[('A',(24,8),20,20,True),('A',(44,28),20,20,True)])
        path('band',(4,28),[('L',(44,28)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28))],True);join('dome','band')
