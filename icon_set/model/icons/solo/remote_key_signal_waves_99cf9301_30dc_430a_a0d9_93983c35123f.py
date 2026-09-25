"""Car Remote Key Signal.

Plan: Rounded vertical fob owns two equal button dots; paired signal arcs above. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Use two round buttons and one signal wave per side; omit redundant second wave and side ticks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99cf9301-30dc-430a-a0d9-93983c35123f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/11-99cf9301-30dc-430a-a0d9-93983c35123f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'remote-key-signal-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('remote', 'key', 'signal', 'waves')

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
        rect('fob',15,15,18,27,7)
        for y in (24,33): self.add_dot(f'button-{y}',(24,y))
        path('left-wave',(6,19),[('C',(17,6),(6,12),(11,6))])
        path('right-wave',(31,6),[('C',(42,19),(37,6),(42,12))])
