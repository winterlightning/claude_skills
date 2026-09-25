"""Strong Bodybuilder Flexing Arms.

Plan: Headless muscular torso with mirrored raised forearms and flexed biceps; bounds (4,8)-(44,40).
Construction: human_ref/full_body_ref.png: coherent limb construction; intentional headless strength subject follows source.
Reduction: Finger folds and muscle creases omitted; two broad raised forearms and tapered torso retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40884d36-f762-4ecf-a351-e11189a03a5d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/38-40884d36-f762-4ecf-a351-e11189a03a5d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'flexing-torso'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('flexing', 'torso')

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
        path('torso',(16,40),[('L',(14,28)),('C',(4,24),(8,29),(4,28)),('L',(6,8)),('L',(16,8)),('L',(16,20)),('C',(24,20),(18,18),(21,20)),('C',(32,20),(27,20),(30,18)),('L',(32,8)),('L',(42,8)),('L',(44,24)),('C',(34,28),(44,28),(40,29)),('L',(32,40)),('L',(16,40))],True)
