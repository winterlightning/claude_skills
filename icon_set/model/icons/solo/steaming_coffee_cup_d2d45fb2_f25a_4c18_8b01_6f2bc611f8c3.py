"""Steaming Cup of Coffee.

Plan: Coffee cup with rounded base, rectangular loop handle, saucer and paired steam strokes; bounds (4,8)-(44,40).
Construction: Lucide cup construction: coherent rounded cup and true handle nodes.
Reduction: Bowl depth reduced; two steam wisps simplified to short upright strokes with separate saucer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2d45fb2-f25a-4c18-8b01-6f2bc611f8c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/30-d2d45fb2-f25a-4c18-8b01-6f2bc611f8c3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'steaming-coffee-cup'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('steaming', 'coffee', 'cup')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('cup',(4,20),[('L',(28,20)),('L',(28,28)),('A',(25,31),3,3,True),('L',(7,31)),('A',(4,28),3,3,True),('L',(4,20))],True)
        path('handle',(28,20),[('L',(40,20)),('A',(44,24),4,4,True),('A',(40,28),4,4,True),('L',(28,28))]);join('cup','handle')
        line('steam-left',(12,8),(12,11));line('steam-right',(24,8),(24,11));line('saucer',(4,40),(32,40))
