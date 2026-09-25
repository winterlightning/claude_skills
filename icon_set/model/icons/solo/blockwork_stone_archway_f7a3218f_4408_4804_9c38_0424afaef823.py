"""Blockwork Stone Archway
Plan: Masonry outer wall, open central arch, courses and centered upper block joint.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Reduced staggered joints to avoid crowding."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7a3218f-4408-4804-9c38-0424afaef823'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/patina_f7a3218f-4408-4804-9c38-0424afaef823.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blockwork-stone-archway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('archway', 'arch', 'stone', 'blocks', 'wall', 'entrance')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        poly('wall',(6,42),(6,32),(6,15),(6,6),(24,6),(42,6),(42,15),(42,32),(42,42),(32,42),(32,32),(32,31));path('arch',(32,31),[('A',(16,31),8,8,False),('L',(16,32)),('L',(16,42)),('L',(6,42))]);join('wall','arch')
        line('course-top',(6,15),(42,15));join('course-top','wall')
        for x in (6,32):
         line(f'course-{x}',(x,32),(x+10,32));join(f'course-{x}','wall');join(f'course-{x}','arch' if x==6 else 'wall')
        line('joint',(24,6),(24,15));join('joint','wall');join('joint','course-top')
