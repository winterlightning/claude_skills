"""Bitten Chip Cookie
Plan: Round cookie with two connected bite scallops at upper-right; three separated chocolate chips.
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: Lucide cookie: circular envelope interrupted by concave bites.
Reduction: Chips reduced to dots for legible open space.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a88b68c-adf8-4916-9fdb-222550f8f7d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nibble_4a88b68c-adf8-4916-9fdb-222550f8f7d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitten-chip-cookie'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cookie', 'biscuit', 'bite', 'chips', 'snack', 'food')

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
        path('cookie',(24,4),[('A',(44,24),20,20,False,True),('C',(32,15),(36,28),(30,23)),('C',(24,4),(24,16),(21,10))],True)
        for j,p in enumerate([(16,16),(14,30),(28,32)]):self.add_dot(f'chip-{j}',p)

SOURCE_REFERENCES = (('f430644f-0902-4de5-ab0c-9a50f0332a1a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/cookie bite_f430644f-0902-4de5-ab0c-9a50f0332a1a.svg'),)
