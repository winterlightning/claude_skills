"""Rising Segmented Caterpillar
Plan: Five round segments curve upward into antenna-bearing head.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae78fe66-f815-4021-8709-b0f3e9e07497'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/caterpillar_ae78fe66-f815-4021-8709-b0f3e9e07497.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rising-segmented-caterpillar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('caterpillar', 'insect', 'segments', 'antennae', 'larva', 'animal', 'garden')

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

        import math
        centers=[(11,37),(21,37),(29,31),(35,23),(35,13)]
        contacts=[(16,37),(25,34),(32,27),(35,18)]
        for i,(x,y) in enumerate(centers):
         points={(x-5,y),(x,y-5),(x+5,y),(x,y+5)}
         if i:points.add(contacts[i-1])
         if i<4:points.add(contacts[i])
         points=sorted(points,key=lambda p:math.atan2(p[1]-y,p[0]-x))
         path(f'segment-{i}',points[0],[('A',p,5,5,True) for p in points[1:]+points[:1]],True)
        for i in range(4):self.relate('connect',f'segment-{i}',f'segment-{i+1}')
        path('antenna-left',(31,10),[('C',(28,6),(30,7),(29,6))])
        path('antenna-right',(39,10),[('C',(42,6),(40,7),(41,6))])
        self.relate('connect','antenna-left','segment-4');self.relate('connect','antenna-right','segment-4')
