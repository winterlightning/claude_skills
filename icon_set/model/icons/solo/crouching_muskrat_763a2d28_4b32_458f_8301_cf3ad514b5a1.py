"""muskrat: standalone SOLO48 repair.
Plan: Low crouching rodent with a curved trailing tail.
Keyshape: HRECT_L; shared dimensions and nodes own repeated elements.
Reduction: Raised belly and widened forefoot; tiny eye and extra leg seam omitted. Natural profile and tail asymmetry retained.
Lucide originals and atomic-debug construction reference: none.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '763a2d28-4b32-458f-8301-cf3ad514b5a1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/muskrat_763a2d28-4b32-458f-8301-cf3ad514b5a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crouching-muskrat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('muskrat', 'rodent', 'animal', 'mammal', 'tail', 'wildlife')

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
        path('muskrat',(4,22),[('C',(15,14),(4,18),(10,15)),('C',(19,8),(15,10),(16,8)),('C',(23,12),(22,8),(23,10)),('C',(40,28),(33,8),(40,15)),('C',(26,30),(40,30),(34,30)),('L',(22,30)),('L',(18,34)),('L',(8,34)),('L',(12,26)),('C',(4,22),(10,24),(8,26))],True)
        path('tail',(40,28),[('C',(44,34),(44,28),(44,30)),('C',(22,40),(44,40),(29,40))]);self.relate('connect','tail','muskrat')
