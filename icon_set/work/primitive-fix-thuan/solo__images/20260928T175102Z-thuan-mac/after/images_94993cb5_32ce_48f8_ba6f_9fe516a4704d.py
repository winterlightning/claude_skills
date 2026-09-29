"""Rounded rectangular image frame, a small sun and a gently rounded mountain; actual frame connections are split at the shared nodes.
Construction: Lucide image: rounded enclosure and rounded mountain summit with a separate sun."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '94993cb5-32ce-48f8-ba6f-9fe516a4704d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__images/20260928T175102Z-thuan-mac/reference/images_94993cb5-32ce-48f8-ba6f-9fe516a4704d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'images'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('images',)

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

        path('frame',(4,12),[('A',(8,8),4,4,True),('L',(40,8)),('A',(44,12),4,4,True),('L',(44,31)),('L',(44,36)),('A',(40,40),4,4,True),('L',(13,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12))],True)
        self.add_dot('sun',(15,19))
        path('mountain',(13,40),[('L',(28,25)),('A',(34,25),4,4,True),('L',(44,35))])
        join('frame','mountain')
