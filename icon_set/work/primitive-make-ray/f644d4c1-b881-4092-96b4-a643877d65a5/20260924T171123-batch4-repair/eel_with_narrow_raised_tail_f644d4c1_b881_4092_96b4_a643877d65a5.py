"""Broad S-shaped eel with raised tail.
Plan: HRECT_L preserves the long horizontal silhouette. Body and neck bands remain crowded; not visually approved.
Reduction: No defining part omitted.
Construction references: No useful exact Lucide match used; source eel supplies its deliberate asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f644d4c1-b881-4092-96b4-a643877d65a5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/eel_f644d4c1-b881-4092-96b4-a643877d65a5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'eel-with-narrow-raised-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('eel', 'fish', 'tail', 'curve', 'body', 'aquatic', 'animal')

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
        path('eel',(9,8),[('L',(19,8)),('C',(28,17),(25,8),(28,11)),('C',(18,27),(28,24),(23,27)),('C',(13,32),(14,27),(13,29)),('C',(19,35),(13,35),(16,36)),('C',(35,29),(26,35),(28,29)),('C',(44,33),(39,29),(42,30)),('C',(28,37),(36,32),(35,35)),('C',(17,40),(24,39),(21,40)),('C',(4,29),(8,40),(4,36)),('C',(15,18),(4,22),(8,19)),('C',(18,16),(19,18),(20,16)),('L',(9,16)),('C',(9,8),(3,16),(3,8))],True)