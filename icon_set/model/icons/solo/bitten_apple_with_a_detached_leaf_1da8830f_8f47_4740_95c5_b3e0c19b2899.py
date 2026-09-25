"""Bitten Apple with a Detached Leaf
Plan: Apple has a broad body, a concave right bite, and an upward leaf. Deliberate rightward bite asymmetry.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful exact Lucide match; broad coherent fruit silhouette.
Reduction: Reduced leaf to an open curved stroke; retained bite and lobed base.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1da8830f-8f47-4740-95c5-b3e0c19b2899'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/apple logo_1da8830f-8f47-4740-95c5-b3e0c19b2899.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitten-apple-with-a-detached-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('apple', 'fruit', 'bite', 'leaf', 'logo', 'food', 'orchard')

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
        path('apple',(24,16),[('C',(8,22),(14,10),(8,15)),('C',(17,44),(8,32),(10,44)),('C',(24,41),(21,44),(21,41)),('C',(31,44),(27,41),(27,44)),('C',(40,32),(36,44),(38,37)),('C',(40,17),(28,30),(29,19)),('C',(24,16),(34,11),(29,13))],True)
        path('leaf',(24,6),[('C',(34,4),(26,4),(29,4))])
