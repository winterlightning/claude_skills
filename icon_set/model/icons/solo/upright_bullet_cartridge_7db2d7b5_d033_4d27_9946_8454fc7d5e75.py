"""Upright Bullet Cartridge
Plan: Symmetric projectile, casing and broad rim.
Keyshape: VRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7db2d7b5-d033-4d27-9946-8454fc7d5e75'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/ammunition_7db2d7b5-d033-4d27-9946-8454fc7d5e75.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-bullet-cartridge'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bullet', 'cartridge', 'ammunition', 'casing', 'projectile', 'round', 'rim')

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
        path('bullet',(12,18),[('C',(24,4),(12,11),(19,4)),('C',(36,18),(29,4),(36,11)),('L',(36,36)),('L',(38,36)),('L',(38,44)),('L',(10,44)),('L',(10,36)),('L',(12,36)),('L',(12,18))],True)
        self.add_line('projectile-seam',(12,18),(36,18));self.add_line('base-seam',(12,36),(36,36))
        self.relate('connect','bullet','projectile-seam');self.relate('connect','bullet','base-seam')
