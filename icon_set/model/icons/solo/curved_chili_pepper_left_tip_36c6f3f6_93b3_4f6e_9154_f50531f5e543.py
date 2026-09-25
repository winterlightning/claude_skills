"""Spicy Hot Chili Pepper.

Plan: Centerline4,8,44,40. Curved horizontal pepper points left, with upper-right curved stem.
Construction: No useful direct Lucide match; coherent cubic curves preserve source pepper direction.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36c6f3f6-93b3-4f6e-9154-f50531f5e543'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/34-36c6f3f6-93b3-4f6e-9154-f50531f5e543.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'curved-chili-pepper-left-tip'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('curved', 'chili', 'pepper', 'left', 'tip')

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
        path('pepper',(4,26),[('C',(30,20),(17,29),(22,20)),('C',(35,18),(32,20),(33,18)),('C',(40,24),(38,18),(40,20)),('C',(22,40),(40,33),(32,40)),('C',(4,26),(12,40),(6,34))],True)
        path('stem',(35,18),[('C',(44,13),(35,10),(44,19)),('C',(40,8),(44,10),(42,8))]);join('pepper','stem')
