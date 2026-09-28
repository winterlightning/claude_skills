"""Strained and Irritated Eye.

Plan: Strained almond eye with circular pupil and two rising irritation waves; bounds (4,8)-(44,40).
Construction: Lucide eye: two coherent opposing curves around centered pupil; paired strain marks follow source.
Reduction: Iris side arcs omitted; pupil reduced to a dot; two irritation marks retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4452b8b-56b6-409c-8450-ac0b79fa3c9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/34-f4452b8b-56b6-409c-8450-ac0b79fa3c9e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'eye-with-strain-marks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('eye', 'with', 'strain', 'marks')

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
        path('eye',(4,30),[('C',(24,20),(10,24),(16,20)),('C',(44,30),(32,20),(38,24)),('C',(24,40),(38,36),(32,40)),('C',(4,30),(16,40),(10,36))],True)
        self.add_dot('pupil',(24,30))
        path('strain-left',(14,8),[('C',(16,12),(11,9),(19,11))]);path('strain-right',(30,8),[('C',(32,12),(27,9),(35,11))])
