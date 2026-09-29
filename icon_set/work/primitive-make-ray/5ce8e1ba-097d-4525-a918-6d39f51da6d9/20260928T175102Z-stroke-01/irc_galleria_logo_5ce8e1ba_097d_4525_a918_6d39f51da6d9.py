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

        path('left-to-right',(24,24),[('C',(14,10),(19,18),(18,10)),('C',(4,24),(7,10),(4,16)),('C',(14,38),(4,32),(7,38)),('C',(29,18),(21,38),(24,24)),('C',(34,10),(31,13),(32,10)),('C',(44,24),(41,10),(44,16)),('C',(34,38),(44,32),(41,38)),('C',(27,29),(31,38),(29,32))])
