"""canoe-and-paddle: Top-view canoe with a circular cockpit and a separate double paddle. Repeated blades mirror vertically. Wide HRECT_L reserves space for the cockpit; long rib omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b8e9bf7-9bed-5b92-918e-e02031e1e3e3'
SOURCE_PATH = 'pictographic-primitives/outdoors/canoe single_7b8e9bf7-9bed-5b92-918e-e02031e1e3e3.svg'
AUTHOR = 'gpt-6'


class CanoeAndPaddle(Solo48):
    icon_id = 'canoe-and-paddle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddle', 'kayak', 'boat', 'water', 'sport', 'outdoors', 'outdoors-batch-01', 'sub icon')

    def build(self):
        # Plan: Top-view canoe with a circular cockpit and a separate double paddle. Repeated blades mirror vertically. Wide HRECT_L reserves space for the cockpit; long rib omitted.
        # Lucide sailboat: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (4, 8, 44, 40).

        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        # Wide top-view hull reserves a clear circular cockpit.
        path('canoe',(32,8),[('A',(44,26),12,18,True),('L',(44,32)),('A',(20,32),12,8,True),('L',(20,26)),('A',(32,8),12,18,True)],True)
        circle('cockpit',32,26,3)
        for i in range(2):
            def p(x,y): return (x,y) if i == 0 else (x,48-y)
            poly(f'blade-{i}',p(4,8),p(12,8),p(12,16),p(8,20),p(4,16),closed=True)
        line('shaft',(8,20),(8,28));join('shaft','blade-0');join('shaft','blade-1')


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('18ef3c0c-f96b-4a36-b74d-e15aada31f40', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/canoe paddle_18ef3c0c-f96b-4a36-b74d-e15aada31f40.svg')]
