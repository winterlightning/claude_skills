"""Romaine Leaf with Branching Vein
Plan: Pointed leaf with continuous central vein and paired side branches.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide leaf: enclosing curved blade and extended stem.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa44650c-65b0-4d6c-a791-d54f9f0089c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romaine_aa44650c-65b0-4d6c-a791-d54f9f0089c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'romaine-leaf-with-branching-vein'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('romaine', 'lettuce', 'leaf', 'vein', 'vegetable', 'plant')

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
        path('leaf',(24,4),[('C',(40,26),(31,11),(40,19)),('C',(24,38),(40,34),(33,38)),('C',(8,26),(15,38),(8,34)),('C',(24,4),(8,19),(17,11))],True)
        self.add_line('vein',(24,16),(24,44));self.relate('connect','leaf','vein')
        self.add_polyline('branches',(16,24),(24,31),(32,24));self.relate('connect','branches','vein')
