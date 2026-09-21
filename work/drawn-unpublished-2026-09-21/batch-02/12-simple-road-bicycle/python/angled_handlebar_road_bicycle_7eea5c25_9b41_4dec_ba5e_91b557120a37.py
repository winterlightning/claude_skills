"""Angled Handlebar Road Bicycle
Plan: Two shared-radius wheels, triangular frame, saddle and angled handlebar.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eea5c25-9b41-4dec-ba5e-91b557120a37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bike parking 2_7eea5c25-9b41-4dec-ba5e-91b557120a37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angled-handlebar-road-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bicycle', 'road', 'bike', 'cycling', 'transport', 'wheels', 'handlebar')

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
        for x in (12,36):circle(f'wheel-{x}',x,32,8)
        self.add_polyline('frame',(12,32),(19,19),(29,19),(23,32),closed=True)
        self.add_polyline('seat-post',(23,32),(17,16),(14,16))
        self.add_polyline('handlebar',(36,32),(28,8),(34,8))
        self.relate('connect','frame','wheel-12');self.relate('connect','handlebar','wheel-36')
        self.relate('connect','frame','seat-post');self.relate('connect','frame','handlebar')
