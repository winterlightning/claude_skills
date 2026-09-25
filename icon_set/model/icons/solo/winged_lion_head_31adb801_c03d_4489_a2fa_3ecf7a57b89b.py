"""Mythical Winged Lion Head.

Plan: Frontal lion shield mane below two outward feathered wings. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduce inner muzzle to nose chevron and wings to long feather contours; retain frontal mane and paired wings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31adb801-c03d-4489-a2fa-3ecf7a57b89b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/28-31adb801-c03d-4489-a2fa-3ecf7a57b89b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'winged-lion-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('winged', 'lion', 'head')

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
        path('mane',(14,22),[('L',(34,22)),('L',(38,33)),('L',(24,42)),('L',(10,33)),('L',(14,22))],True)
        poly('wing-left',(14,22),(6,6),(18,10),(20,16));join('mane','wing-left')
        poly('wing-right',(34,22),(42,6),(30,10),(28,16));join('mane','wing-right')
        poly('nose',(22,31),(24,32),(26,31))
