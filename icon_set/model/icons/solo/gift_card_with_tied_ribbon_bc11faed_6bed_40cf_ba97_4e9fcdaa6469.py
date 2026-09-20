"""Gift Card with Ribbon Bow.

Plan: Gift card with central ribbon bow integrated into its horizontal ribbon; bounds (4,8)-(44,40).
Construction: Lucide gift: two mirrored bow loops join a ribbon at a shared knot.
Reduction: Trailing bow ends and tiny card inscription omitted to keep the bow readable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc11faed-6bed-40cf-ba97-4e9fcdaa6469'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/27-bc11faed-6bed-40cf-ba97-4e9fcdaa6469.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gift-card-with-tied-ribbon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('gift', 'card', 'with', 'tied', 'ribbon')

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
        path('card',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,27)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,27)),('L',(4,12)),('A',(8,8),4,4,True)],True)
        path('bow-left',(24,27),[('C',(14,17),(21,20),(19,17)),('C',(14,27),(12,17),(12,27)),('L',(24,27))],True)
        path('bow-right',(24,27),[('C',(34,17),(27,20),(29,17)),('C',(34,27),(36,17),(36,27)),('L',(24,27))],True)
        line('ribbon-left',(4,27),(14,27));line('ribbon-right',(34,27),(44,27))
        for a,b in [('card','ribbon-left'),('card','ribbon-right'),('bow-left','ribbon-left'),('bow-right','ribbon-right'),('bow-left','bow-right')]:join(a,b)
