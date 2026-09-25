"""Arched Castle Gate with Keyhole.

Plan: Single broad arched dungeon door with bottom masonry block band and central keyhole. Extremes8,4,40,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Remove inner surround line to retain the keyhole and masonry band with legal spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd08173a-d186-5611-b50e-f129b1a96e2d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/32-dd08173a-d186-5611-b50e-f129b1a96e2d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'arched-dungeon-gate'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('arched', 'dungeon', 'gate')

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
        path('door',(8,44),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,44)),('L',(8,44))],True)
        line('base-top',(8,35),(40,35));join('door','base-top')
        line('block-left',(17,35),(17,44));line('block-right',(31,35),(31,44));join('base-top','block-left');join('base-top','block-right');join('door','block-left');join('door','block-right')
        line('keyhole',(24,19),(24,24))
