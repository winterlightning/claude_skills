"""Domed Diaphragm with Thick Lower Rim
Plan: Round domed cap with a lower inset rim
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: No useful Lucide match; concentric arcs.
Reduction: Remove third inner arch to preserve clear dome."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab591fb1-da95-4677-8beb-82ec667316b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/diaphragm_ab591fb1-da95-4677-8beb-82ec667316b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-diaphragm-with-thick-lower-rim'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diaphragm', 'dome', 'rim', 'device', 'contraceptive', 'medical', 'barrier')

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
        circle('outline',24,24,20)
        path('rim',(4,24),[('C',(44,24),(8,40),(40,40))]);self.relate('connect','rim','outline')
