"""Container Truck in Side View
Plan: Box cargo and right-facing cab with two wheels
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide truck wheel and cab construction.
Reduction: Reduce cargo ribs to two, omit small window."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49e3783b-b77c-4b02-9013-5cd8c893c8f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shipping logistic free shipping delivery container_49e3783b-b77c-4b02-9013-5cd8c893c8f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'container-truck-in-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('truck', 'container', 'freight', 'delivery', 'vehicle', 'logistics')

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
        path('cargo',(4,32),[('L',(4,8)),('L',(28,8)),('L',(28,32))])
        path('cab',(28,16),[('L',(36,16)),('L',(44,24)),('L',(36,24)),('L',(36,32))]);self.relate('connect','cab','cargo')
        for x in (12,20):self.add_line(f'rib-{x}',(x,8),(x,24));self.relate('connect',f'rib-{x}','cargo')
        circle('rear',12,36,4);circle('front',36,36,4)
        self.add_line('chassis',(16,36),(32,36));self.relate('connect','chassis','rear');self.relate('connect','chassis','front')

        self.relate('connect','cab','front')

# Final review: Reduce cargo ribs to two, wheels to radius 4, and cab to one stepped outline without a small window.
