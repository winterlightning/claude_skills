"""One flowing side silhouette, lifted muzzle, two grounded legs and a curved hanging tail; asymmetry preserves the howling pose.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '02bbed8d-19bf-42c9-9539-d93fbda86791'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__howling-wolf/20260928T175102Z-thuan-mac/reference/wolf body howl_02bbed8d-19bf-42c9-9539-d93fbda86791.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'howling-wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('wolf body howl',)

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

        path('outline',(6,42),[('C',(9,31),(7,40),(7,35)),('C',(17,23),(11,27),(13,24)),('C',(28,17),(23,21),(27,20)),('L',(26,17)),('L',(30,10)),('L',(35,8)),('L',(39,6)),('C',(41,10),(41,6),(41,8)),('L',(41,24)),('C',(38,31),(41,27),(40,29)),('L',(38,42))])
        path('rear-leg',(17,23),[('C',(16,33),(15,26),(15,30)),('L',(16,42))])
        path('belly',(16,35),[('C',(31,31),(23,37),(27,33)),('L',(30,42)),('L',(42,42))])
        path('tail',(6,42),[('C',(16,35),(10,41),(13,38))])
        for a,b in [('outline','rear-leg'),('rear-leg','belly'),('outline','tail'),('tail','belly')]: join(a,b)
