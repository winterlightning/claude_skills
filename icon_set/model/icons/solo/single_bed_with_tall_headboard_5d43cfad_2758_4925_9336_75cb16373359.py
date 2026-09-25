"""Single Bed with Tall Headboard
Plan: Tall headboard, raised pillow, mattress and foot support.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: Lucide bed: connected open structural lines.
Reduction: Headboard thickness simplified to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d43cfad-2758-4925-9336-75cb16373359'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crib_5d43cfad-2758-4925-9336-75cb16373359.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-bed-with-tall-headboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bed', 'single', 'pillow', 'headboard', 'bedroom', 'sleep', 'furniture')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        self.add_line('headboard',(4,8),(4,40))
        path('mattress',(4,23),[('L',(40,23)),('A',(44,27),4,4,True),('L',(44,40))])
        self.add_line('bed-base',(4,32),(44,32))
        path('pillow',(4,14),[('L',(14,14)),('A',(18,18),4,4,True),('L',(18,23))])
        for a,b in [('headboard','mattress'),('headboard','bed-base'),('headboard','pillow'),('mattress','pillow'),('mattress','bed-base')]:self.relate('connect',a,b)
