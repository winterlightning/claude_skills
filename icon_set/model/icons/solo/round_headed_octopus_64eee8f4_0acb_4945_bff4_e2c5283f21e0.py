"""Round Headed Octopus
Plan: Domed head and separate curling lower arm strokes.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Six lower curls reduced to four and tiny eyes omitted to preserve negative space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64eee8f4-0acb-4945-bff4-e2c5283f21e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cephalopod_64eee8f4-0acb-4945-bff4-e2c5283f21e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-headed-octopus'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('octopus', 'arms', 'sea', 'marine', 'animal', 'eyes', 'tentacles')

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
        path('head',(16,21),[('C',(12,14),(16,21),(12,19)),('A',(36,14),12,8,True),('C',(32,21),(36,19),(32,21))])
        path('outer-left',(16,21),[('A',(6,21),5,4,True),('L',(6,22))])
        path('outer-right',(32,21),[('A',(42,21),5,4,False),('L',(42,22))])
        path('lower-left',(8,34),[('L',(8,36)),('A',(20,36),6,6,False),('L',(20,30))])
        path('lower-right',(40,34),[('L',(40,36)),('A',(28,36),6,6,True),('L',(28,30))])
        self.relate('connect','head','outer-left');self.relate('connect','head','outer-right')
        # Tiny eyes omitted to retain head clearance.
