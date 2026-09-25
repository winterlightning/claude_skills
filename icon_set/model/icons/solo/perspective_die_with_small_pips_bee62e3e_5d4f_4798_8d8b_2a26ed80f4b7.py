"""Perspective Die with Small Pips
Plan: Perspective cube with joined face edges and one pip on each visible face.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide dice-3: restrained round pips.
Reduction: Source faint pips reduced to one per face."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bee62e3e-5d4f-4798-8d8b-2a26ed80f4b7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/board game dice 1_bee62e3e-5d4f-4798-8d8b-2a26ed80f4b7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'perspective-die-with-small-pips'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('die', 'dice', 'game', 'cube', 'pips', 'chance', 'tabletop')

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
        self.add_polyline('cube',(24,6),(42,15),(42,33),(24,42),(6,33),(6,15),closed=True)
        self.add_polyline('edges',(6,15),(24,24),(42,15));self.add_line('upright',(24,24),(24,42))
        for a,b in [('cube','edges'),('cube','upright'),('edges','upright')]:self.relate('connect',a,b)
        for i,p in enumerate([(14,28),(34,28)]):self.add_dot(f'pip-{i}',p)
