"""Kermit the Frog Face.

Plan: Kermit rounded frog face, prominent eye circles and pointed neck ruff. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit pupils and mouth closure; retain raised circular eyes and broad smile. Reduce the many-point collar to two short strokes below the jaw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eff967d-5df4-43e4-98a7-d78f84b1fc39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/16-4eff967d-5df4-43e4-98a7-d78f84b1fc39.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'kermit-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('kermit', 'face')

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
        path('face',(7,12),[('C',(6,25),(6,19),(6,22)),('C',(24,38),(6,32),(16,38)),('C',(42,25),(32,38),(42,32)),('C',(41,12),(42,22),(42,19))])
        circle('eye-left',13,12,6);circle('eye-right',35,12,6);join('face','eye-left');join('face','eye-right')
        path('smile',(18,26),[('C',(30,26),(21,30),(27,30))])
        poly('ruff',(16,42),(24,38),(32,42));join('face','ruff')
