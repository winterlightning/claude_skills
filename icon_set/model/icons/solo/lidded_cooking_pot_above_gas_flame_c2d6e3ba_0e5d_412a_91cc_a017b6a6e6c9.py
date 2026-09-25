"""Lidded Cooking Pot above Gas Flame
Plan: Lidded pot above a simple gas flame
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide cooking-pot body and handles.
Reduction: One flame replaces crowded three-point flame; knob reduced to stem."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2d6e3ba-0e5d-412a-91cc-a017b6a6e6c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stove steamer gas_c2d6e3ba-0e5d-412a-91cc-a017b6a6e6c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lidded-cooking-pot-above-gas-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pot', 'lid', 'flame', 'cooking', 'gas', 'kitchen')

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
        path('pot',(8,12),[('L',(8,24)),('A',(12,28),4,4,False),('L',(36,28)),('A',(40,24),4,4,False),('L',(40,12))])
        self.add_line('lid',(8,12),(40,12));self.relate('connect','lid','pot');self.add_line('knob',(24,4),(24,12));self.relate('connect','knob','lid')
        path('flame',(24,36),[('C',(20,44),(18,40),(18,44)),('C',(28,44),(22,44),(26,44)),('C',(24,36),(34,44),(28,40))],True)
