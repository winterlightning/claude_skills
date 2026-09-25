"""Ergonomic Gaming Chair.

Plan: Gaming chair with contoured back, horizontal opening, armrests, seat and pedestal. Extremes8,4,40,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Simplify seat cushion to one stroke and retain the high winged back and head opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '381295ef-1fc1-4c3b-8aa5-5e61c5f91512'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/50-381295ef-1fc1-4c3b-8aa5-5e61c5f91512.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gaming-chair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('gaming', 'chair')

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
        path('back',(19,32),[('L',(14,14)),('L',(16,4)),('L',(32,4)),('L',(34,14)),('L',(29,32))])
        line('opening',(23,13),(25,13))
        poly('seat',(12,32),(19,32),(24,32),(29,32),(36,32));join('back','seat')
        for x in (8,40):poly(f'arm-{x}',(x,23),(x,32),(12 if x==8 else 36,32));join('seat',f'arm-{x}')
        line('post',(24,32),(24,44));poly('base',(16,44),(24,44),(32,44));join('seat','post');join('post','base')
