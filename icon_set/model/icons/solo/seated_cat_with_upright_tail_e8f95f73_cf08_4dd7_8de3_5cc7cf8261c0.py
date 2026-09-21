"""Seated Cat with Upright Tail
Plan: Pointed ears, featureless head, seated torso, forelegs and upright tail.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8f95f73-cf08-4dd7-8de3-5cc7cf8261c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bobcat_e8f95f73-cf08-4dd7-8de3-5cc7cf8261c0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-cat-with-upright-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cat', 'pet', 'feline', 'seated', 'tail', 'ears', 'animal')

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
        path('head',(8,6),[('L',(16,12)),('L',(26,12)),('L',(34,6)),('L',(34,24)),('C',(21,30),(34,27),(26,30)),('C',(8,24),(16,30),(8,27)),('L',(8,6))],True)
        path('body',(11,28),[('C',(6,42),(7,33),(6,37)),('L',(34,42)),('C',(31,28),(34,36),(33,31))])
        for x in (16,24):self.add_line(f'leg-{x}',(x,34),(x,42));self.relate('connect','body',f'leg-{x}')
        path('tail',(34,42),[('C',(42,34),(40,42),(42,40)),('L',(42,25))])
        self.relate('connect','head','body');self.relate('connect','body','tail')
