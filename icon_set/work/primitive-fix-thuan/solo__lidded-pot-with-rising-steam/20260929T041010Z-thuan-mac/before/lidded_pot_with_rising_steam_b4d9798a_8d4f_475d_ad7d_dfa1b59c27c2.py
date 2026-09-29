"""Lidded Pot with Rising Steam
Plan: Deep pot, lid and two rising steam curves
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide cooking-pot rounded vessel.
Reduction: Omit knob and handles to allow steam and deep vessel at 48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4d9798a-8d4f-475d-ad7d-dfa1b59c27c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cooking_b4d9798a-8d4f-475d-ad7d-dfa1b59c27c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lidded-pot-with-rising-steam'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pot', 'cooking', 'lid', 'steam', 'kitchen', 'hot', 'cookware')

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
        path('pot',(8,24),[('L',(12,40)),('A',(16,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('L',(40,24))])
        self.add_line('lid',(8,24),(40,24));self.relate('connect','lid','pot')
        for x in (16,32):path(f'steam-{x}',(x,16),[('C',(x,4),(x-6,12),(x+6,8))])
