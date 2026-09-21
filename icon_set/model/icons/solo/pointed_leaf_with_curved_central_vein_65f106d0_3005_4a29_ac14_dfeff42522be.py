"""Pointed Leaf with Curved Central Vein
Plan: Broad asymmetric leaf with continuous stem and vein.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide leaf: coherent outer curves and continuous stem.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65f106d0-3005-4a29-ac14-dfeff42522be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/silk_65f106d0-3005-4a29-ac14-dfeff42522be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-leaf-with-curved-central-vein'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('leaf', 'plant', 'vein', 'stem', 'nature', 'foliage')

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
        path('leaf',(12,36),[('C',(6,24),(7,34),(6,30)),('C',(24,10),(6,15),(15,12)),('C',(40,6),(32,9),(36,8)),('C',(42,22),(41,11),(42,16)),('C',(25,39),(42,32),(35,39)),('C',(12,36),(19,39),(15,38))],True)
        path('vein',(6,42),[('C',(12,36),(7,39),(9,37)),('C',(29,23),(18,29),(24,28))])
        self.relate('connect','leaf','vein')
