"""Seated Chinchilla with Curved Tail
Plan: Seated rodent with round ear, bent hind leg and raised curved tail.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'df04551f-f9b1-422f-a44f-8a7dfd1d0dda'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chinchilla_df04551f-f9b1-422f-a44f-8a7dfd1d0dda.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-chinchilla-with-curved-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('chinchilla', 'rodent', 'tail', 'seated', 'animal', 'pet', 'mammal')

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
        path('chinchilla',(6,20),[('C',(16,12),(6,16),(11,12)),('C',(20,6),(16,8),(17,6)),('C',(26,10),(25,6),(26,8)),('L',(25,17)),('C',(33,34),(30,19),(33,26)),('L',(33,42)),('L',(22,42)),('L',(12,42)),('L',(15,36)),('C',(6,20),(9,31),(10,25))],True)
        path('leg',(25,31),[('C',(22,42),(18,31),(18,40))]);self.relate('connect','chinchilla','leg')
        path('tail',(33,42),[('C',(42,30),(42,40),(42,36)),('C',(42,14),(42,24),(35,20))]);self.relate('connect','chinchilla','tail')
