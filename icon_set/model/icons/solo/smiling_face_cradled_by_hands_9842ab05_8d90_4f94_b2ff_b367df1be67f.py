"""Smiling Face with Caring Hands.

Plan: Smile with two diagonal palm strokes at the cheeks; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Each palm reduced to a single diagonal supporting stroke; finger creases and occluded chin omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9842ab05-8d90-4f94-b2ff-b367df1be67f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/38-9842ab05-8d90-4f94-b2ff-b367df1be67f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'smiling-face-cradled-by-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('smiling', 'face', 'cradled', 'by', 'hands')

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
        path('head',(12,34),[('C',(8,22),(8,32),(8,27)),('A',(24,6),16,16,True),('A',(40,22),16,16,True),('C',(36,34),(40,27),(40,32))])
        poly('left-hand',(6,28),(12,34),(18,40),(18,42));poly('right-hand',(42,28),(36,34),(30,40),(30,42));join('head','left-hand');join('head','right-hand')
        self.add_dot('eye-left',(18,18));self.add_dot('eye-right',(30,18))
        path('smile',(20,27),[('C',(28,27),(22,30),(26,30))])
