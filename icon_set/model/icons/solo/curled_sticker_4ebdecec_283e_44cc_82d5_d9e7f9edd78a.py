"""Square Sticker with Curled Corner.

Plan: Rounded sticker with peeled lower-right corner and broad inward curl; bounds (6,6)-(42,42).
Construction: Lucide sticker: shared nodes at diagonal peel boundary and curved fold.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ebdecec-283e-44cc-82d5-d9e7f9edd78a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/16-4ebdecec-283e-44cc-82d5-d9e7f9edd78a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'curled-sticker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('curled', 'sticker')

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
        path('sticker',(12,6),[('L',(36,6)),('A',(42,12),6,6,True),('L',(42,24)),('L',(24,42)),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,12)),('A',(12,6),6,6,True)],True)
        path('fold',(24,42),[('L',(24,32)),('A',(32,24),8,8,True),('L',(42,24))]);join('sticker','fold')
