"""Vertically pointed hull with mirrored smooth sides, oval cockpit, and complete diagonal double-ended paddle behind the hull. Paddle remains deliberately asymmetric relative to boat axis.
Construction: Lucide kayak: pointed hull with smooth curved sides and complete paired blades; source supplies vertical orientation and cockpit."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a40dd6b4-7ef7-5a0e-b996-7bd77b8c7cf8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kayak-and-paddle/20260928T175102Z-thuan-mac/reference/canoe_a40dd6b4-7ef7-5a0e-b996-7bd77b8c7cf8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kayak-and-paddle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('canoe',)

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

        path('hull',(24,4),[('C',(31,14),(27,8),(30,11)),('C',(34,24),(33,18),(34,21)),('C',(24,44),(34,32),(28,40)),('C',(17,34),(21,40),(18,37)),('C',(14,24),(15,30),(14,27)),('C',(24,4),(14,16),(20,8))],True)
        oval('cockpit',24,25,4,5)
        path('blade-upper',(34,12),[('L',(32,10)),('L',(38,4)),('A',(44,10),5,5,True),('L',(38,16)),('L',(34,12))],True)
        path('blade-lower',(14,36),[('L',(16,38)),('L',(10,44)),('A',(4,38),5,5,True),('L',(10,32)),('L',(14,36))],True)
        line('shaft-upper',(31,14),(34,12));line('shaft-lower',(17,34),(14,36))
        for n in ['upper','lower']:
            join('blade-'+n,'shaft-'+n);join('hull','shaft-'+n)
