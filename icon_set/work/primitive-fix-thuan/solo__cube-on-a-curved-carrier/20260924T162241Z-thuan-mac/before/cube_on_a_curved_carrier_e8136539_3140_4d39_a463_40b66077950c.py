"""Cube on a Curved Carrier
Plan: Isometric cube above curved carrier and two supports
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful Lucide match; source cube planes.
Reduction: Keep cube and carrier, reduce support outlines to legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8136539-3140-4d39-a463-40b66077950c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon web service fargate_e8136539-3140-4d39-a463-40b66077950c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cube-on-a-curved-carrier'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cube', 'carrier', 'platform', 'isometric', 'container', 'compute', 'geometry')

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
        self.add_polyline('cube',(24,4),(34,10),(34,20),(24,26),(14,20),(14,10),closed=True)
        path('planes',(14,10),[('L',(24,16)),('L',(34,10))]);self.add_line('edge',(24,16),(24,26));self.relate('connect','planes','cube');self.relate('connect','edge','planes');self.relate('connect','edge','cube')
        path('carrier',(8,28),[('C',(40,28),(8,44),(40,44))])
        self.add_line('left-leg',(16,37),(12,44));self.add_line('right-leg',(32,37),(36,44));self.relate('connect','left-leg','carrier');self.relate('connect','right-leg','carrier')
