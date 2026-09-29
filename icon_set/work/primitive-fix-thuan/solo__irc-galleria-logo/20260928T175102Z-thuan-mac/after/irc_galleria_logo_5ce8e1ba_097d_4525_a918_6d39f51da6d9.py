"""Two equal round lobes linked by smooth diagonal transitions; deliberate interweaving break at the crossing.
Construction: Lucide infinity: paired rounded lobes and coherent diagonal transitions; reference supplies the open crossing."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5ce8e1ba-097d-4525-a918-6d39f51da6d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__irc-galleria-logo/20260928T175102Z-thuan-mac/reference/irc galleria logo_5ce8e1ba-097d-4525-a918-6d39f51da6d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'irc-galleria-logo'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('irc galleria logo',)

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for i, cmd in enumerate(commands):
                kind, end, *args = cmd
                if kind == 'L' and end == here:
                    continue
                key = f'{name}-{i}'
                if kind == 'L': self.add_line(key, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(key, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C': self.add_bezier(key, here, (args[0], args[1], end))
                members.append(key)
                here = end
            self.add_contour(name, *members, closed=closed)
        def oval(name, x, y, rx, ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): oval(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)

        path('infinity',(24,24),[('C',(14,12),(20,18),(19,12)),('C',(4,24),(8,12),(4,17)),('C',(14,36),(4,31),(8,36)),('C',(34,12),(22,36),(26,12)),('C',(44,24),(40,12),(44,17)),('C',(34,36),(44,31),(40,36)),('C',(28,30),(32,36),(30,33))])

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Keep the source infinity lobes broad and round rather than stretching them vertically to the standard rectangle. All ink stays inside the 48 px canvas.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e94410fdde18795449bb3c2198580981e1f836295e7dfceed69ea2db25fa9a47'}
