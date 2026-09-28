"""Eight Segment Citrus Slice
Plan: Circular rind surrounding radial juicy segments.
Keyshape: CIRCLE; exact inset SOLO48 envelope.
Construction: Lucide citrus: rind and radial wedges.
Reduction: Eight spokes reduced to four for readable 48px wedges."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd06f9723-9870-4475-b5d2-ce03876c7ec1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/citrus_d06f9723-9870-4475-b5d2-ce03876c7ec1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eight-segment-citrus-slice'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('citrus', 'slice', 'fruit', 'segments', 'rind', 'food', 'orange')

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
        circle('rind',24,24,20)
        circle('flesh',24,24,11)
        for i,(x,y) in enumerate([(24,13),(35,24),(24,35),(13,24)]):
         name=f'spoke-{i}';self.add_line(name,(24,24),(x,y));self.relate('connect',name,'flesh')
        for a in range(4):
         for b in range(a+1,4):self.relate('connect',f'spoke-{a}',f'spoke-{b}')
