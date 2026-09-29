"""Draw a complete symmetric pitched roof, small chimney above the right slope, rounded lower walls and an arched doorway.
Construction reference: Lucide house: symmetric gable and rounded wall turns; supplied original retains detached chimney and arched doorway."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '48ea3c6c-5c29-50ff-bdb7-99895f95d856'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-with-chimney-reference-batch-015-09/20260929T033618Z-thuan-mac/reference/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-chimney-reference-batch-015-09'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('house chimney',)

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

        poly('roof',(4,24),(24,4),(44,24))
        poly('chimney',(33,6),(40,6),(40,14))
        path('walls',(8,27),[('L',(8,40)),('A',(12,44),4,4,False),('L',(18,44)),('L',(18,36)),('A',(30,36),6,6,True),('L',(30,44)),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,27))])
