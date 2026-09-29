"""Paired sloping dam towers, horizontal upper spillway, two falling water strokes and separated coherent waves.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6411cee5-9e14-533a-9adf-d5bcd2213734'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hydroelectric-dam/20260928T175102Z-thuan-mac/reference/water dam_6411cee5-9e14-533a-9adf-d5bcd2213734.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hydroelectric-dam'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('water dam',)

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

        for name,x in [('left',6),('right',34)]:
            poly(name,(x,34),(x+3,6),(x+8,6),(x+8,16),(x+5,34))
        line('bridge-top',(14,10),(34,10)); line('bridge-bottom',(14,18),(34,18))
        for j,x in enumerate((22,30)): line(f'water-{j}',(x,24),(x-2,30))
        for name,y in [('waterline',34),('river',42)]:
            path(name,(6,y),[('C',(15,y),(9,y-4),(12,y+4)),('C',(24,y),(18,y-4),(21,y+4)),('C',(33,y),(27,y-4),(30,y+4)),('C',(42,y),(36,y-4),(39,y+4))])
        for t in ['left','right']:
            for b in ['bridge-top','bridge-bottom','waterline']: join(t,b)
