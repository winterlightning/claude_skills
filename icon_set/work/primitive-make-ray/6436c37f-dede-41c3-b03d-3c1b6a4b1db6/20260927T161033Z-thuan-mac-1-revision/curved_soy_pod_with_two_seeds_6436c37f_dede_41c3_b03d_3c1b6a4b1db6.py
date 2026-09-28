"""Curved Soy Pod with Two Seeds
Plan: Curved vertical pod with two separate seed openings and short stem.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Pod rebalanced diagonally; two seed openings retained and normalized to circles.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6436c37f-dede-41c3-b03d-3c1b6a4b1db6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-soy-pod-with-two-seeds/20260927T160834Z-thuan-mac-1/reference/soy_6436c37f-dede-41c3-b03d-3c1b6a4b1db6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-soy-pod-with-two-seeds'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('soy', 'pod', 'seeds', 'legume', 'plant', 'food')

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
        path('pod',(16,44),[('C',(8,32),(10,40),(8,36)),('C',(20,16),(8,24),(15,17)),('C',(24,10),(19,12),(21,10)),('C',(40,18),(33,8),(40,10)),('C',(32,35),(40,25),(38,31)),('C',(16,44),(27,41),(20,44))],True)
        self.add_line('stem',(24,10),(25,4));self.relate('connect','stem','pod')
        circle('upper-seed',29,21,2);circle('lower-seed',19,32,2)
