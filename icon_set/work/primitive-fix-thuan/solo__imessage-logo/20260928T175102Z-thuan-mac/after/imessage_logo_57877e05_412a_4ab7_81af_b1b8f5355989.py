"""Four smooth oval quadrants with one integrated curved tail; avoid an acute interior kink.
Construction: Lucide message-circle: one continuous bubble/tail contour; original supplies the oval proportions."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '57877e05-412a-4ab7-81af-b1b8f5355989'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__imessage-logo/20260928T175102Z-thuan-mac/reference/imessage logo_57877e05-412a-4ab7-81af-b1b8f5355989.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'imessage-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('imessage logo',)

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

        path('bubble',(24,8),[('C',(44,23),(35,8),(44,14)),('C',(24,36),(44,31),(35,36)),('C',(19,35),(22,36),(20,36)),('C',(7,40),(16,39),(11,40)),('C',(11,33),(10,38),(12,35)),('C',(4,23),(6,30),(4,27)),('C',(24,8),(4,14),(13,8))],True)
