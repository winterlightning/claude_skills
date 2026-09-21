"""Sparkle-Eyed Face with Uneven Smile
Plan: Circular face with two four-point sparkle eyes and curved smile.
Keyshape: CIRCLE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Sparkles budgeted as paired repeated shapes; their openings require strict validation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd25557be-d198-406c-ac40-686ab3f61c2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/smiley bright_d25557be-d198-406c-ac40-686ab3f61c2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sparkle-eyed-face-with-uneven-smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('face', 'smile', 'sparkle', 'eyes', 'expression', 'happy')

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
        circle('face',24,24,20)
        for x in (16,32):
         path(f'eye-{x}',(x,15),[('C',(x+3,18),(x,15),(x+2,17)),('C',(x,21),(x+2,17),(x,19)),('C',(x-3,18),(x,19),(x-2,17)),('C',(x,15),(x-2,17),(x,15))],True)
        path('smile',(15,31),[('C',(33,31),(19,35),(29,35))])
