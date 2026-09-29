"""Restore the complete room boundary and floor strip, a tall door and a separate four-pane window. Preserve the source orthogonal room layout.
Construction reference: Supplied interior reference; shared rectangular dimensions and equal window panes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '15d7928a-0a97-4ec4-b4c0-f21360f062be'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__interior-wall-with-door-and-window/20260929T033618Z-thuan-mac/reference/interior_15d7928a-0a97-4ec4-b4c0-f21360f062be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'interior-wall-with-door-and-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('interior',)

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

        poly('room',(4,4),(44,4),(44,36),(44,44),(4,44),(4,36),closed=True)
        poly('floor',(4,36),(10,36),(18,36),(44,36));join('room','floor')
        poly('door',(10,36),(10,14),(18,14),(18,36));join('floor','door')
        poly('window',(26,14),(32,14),(38,14),(38,20),(38,26),(32,26),(26,26),(26,20),closed=True)
        line('window-vertical',(32,14),(32,26));line('window-horizontal',(26,20),(38,20))
        join('window','window-vertical');join('window','window-horizontal');join('window-vertical','window-horizontal')
