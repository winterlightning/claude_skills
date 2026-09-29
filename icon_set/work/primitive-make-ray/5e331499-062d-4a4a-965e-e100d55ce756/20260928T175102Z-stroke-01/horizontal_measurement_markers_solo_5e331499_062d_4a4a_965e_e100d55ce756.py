"""Two matching rounded left jaw ends with sloping right closures; separate central marker and lower right rule. Centerline extremes (6,6)-(42,42).
Construction: Lucide ruler: coherent rule strokes and consistent round joins; original supplies the jaw geometry."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-measurement-markers-solo/20260928T175102Z-thuan-mac/reference/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-measurement-markers-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('measurement markers',)

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

        path('upper-jaw',(24,6),[('L',(10,6)),('A',(10,14),4,4,False),('L',(19,14)),('L',(24,6)),('L',(42,6))])
        line('measure',(28,23),(42,23))
        path('lower-jaw',(24,34),[('L',(19,26)),('L',(10,26)),('A',(10,34),4,4,False),('L',(24,34)),('L',(42,34)),('L',(42,42))])
