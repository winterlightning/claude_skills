"""A compact pickup truck in side view.
Repair plan: Raised chassis; equal wheels attach at top cardinal points. Cab stays intentionally on the right.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dd459eaf-90a6-4872-a777-772bcbc71cdf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pickup_dd459eaf-90a6-4872-a777-772bcbc71cdf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compact-pickup-side-view'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pickup', 'truck', 'vehicle', 'wheels', 'cab', 'transport')

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
        # Paired wheels meet a raised chassis at their top cardinal points.
        path('body',(12,28),[('L',(4,28)),('L',(4,18)),('L',(22,18)),('L',(22,10)),('L',(32,10)),('L',(38,18)),('L',(44,18)),('L',(44,28)),('L',(36,28))])
        self.add_line('base',(12,28),(36,28))
        self.relate('connect','base','body')
        for x in (12,36):
            circle(f'wheel-{x}',x,33,5)
            self.relate('connect','base',f'wheel-{x}')
            self.relate('connect','body',f'wheel-{x}')
