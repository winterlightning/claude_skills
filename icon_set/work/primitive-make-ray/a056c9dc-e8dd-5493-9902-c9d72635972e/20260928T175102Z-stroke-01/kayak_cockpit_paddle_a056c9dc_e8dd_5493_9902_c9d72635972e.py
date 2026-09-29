"""Vertically pointed hull with mirrored smooth sides, oval cockpit, and complete diagonal double-ended paddle behind the hull. Paddle remains deliberately asymmetric relative to boat axis.
Construction: Lucide kayak: pointed hull with smooth curved sides and complete paired blades; source supplies vertical orientation and cockpit."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a056c9dc-e8dd-5493-9902-c9d72635972e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kayak-cockpit-paddle/20260928T175102Z-thuan-mac/reference/kayak_a056c9dc-e8dd-5493-9902-c9d72635972e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kayak-cockpit-paddle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('kayak',)

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

        path('hull',(24,6),[('C',(34,24),(30,12),(34,18)),('C',(24,42),(34,30),(30,36)),('C',(14,24),(18,36),(14,30)),('C',(24,6),(14,18),(18,12))],True)
        oval('cockpit',24,25,4,8)
        path('blade-upper',(35,15),[('C',(34,12),(34,14),(34,13)),('L',(39,6)),('L',(42,9)),('L',(37,15)),('C',(35,15),(36,16),(35,16))],True)
        path('blade-lower',(13,33),[('C',(14,36),(14,34),(14,35)),('L',(9,42)),('L',(6,39)),('L',(11,33)),('C',(13,33),(12,32),(13,32))],True)
        line('shaft-upper',(35,15),(33,18));line('shaft-lower',(13,33),(15,30))
        join('blade-upper','shaft-upper');join('blade-lower','shaft-lower')
