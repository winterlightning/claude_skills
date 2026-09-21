'fluted-classical-column. Plan: Column shaft with one central flute and broad cap and base. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide landmark: equally spaced verticals. Reduction: Reduce three flutes to one and moldings to cap/base bars.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '304e385d-cf54-49b7-a74b-5d81908e19fd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pillar_304e385d-cf54-49b7-a74b-5d81908e19fd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fluted-classical-column'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('column', 'pillar', 'flutes', 'classical', 'architecture', 'stone')

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
        rect('capital',8,4,32,8,4);rect('base',8,36,32,8,4)
        for x in (16,32):
         self.add_line(f'wall-{x}',(x,12),(x,36));self.relate('connect','capital',f'wall-{x}');self.relate('connect','base',f'wall-{x}')
        self.add_line('flute',(24,20),(24,28))
