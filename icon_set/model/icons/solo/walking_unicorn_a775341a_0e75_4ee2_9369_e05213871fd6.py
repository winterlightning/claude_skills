"""Magical Walking Unicorn.

Plan: Left-facing unicorn with lifted front leg, horn and flowing tail. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit the small eye and distant legs; retain the horn, left-facing horse head, long tail and two visible legs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a775341a-0e75-4ee2-9369-e05213871fd6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/20-a775341a-0e75-4ee2-9369-e05213871fd6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'walking-unicorn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('walking', 'unicorn')

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
        path('horse',(6,18),[('L',(14,10)),('L',(14,6)),('L',(20,16)),('L',(24,23)),('L',(33,23)),('A',(39,29),6,6,True),('L',(38,42)),('L',(30,42)),('L',(30,33)),('L',(20,33)),('L',(17,42)),('L',(8,42)),('L',(12,30)),('L',(18,24)),('L',(6,27)),('L',(6,18))],True)
        path('tail',(39,29),[('C',(42,36),(42,29),(42,32))]);join('horse','tail')
        line('horn',(14,10),(6,6));join('horse','horn')
