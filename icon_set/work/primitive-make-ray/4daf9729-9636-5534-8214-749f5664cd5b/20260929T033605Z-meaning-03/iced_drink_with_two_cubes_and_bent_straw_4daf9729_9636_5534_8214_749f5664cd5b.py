"""Restore a tall tapered glass, wavy liquid level, two staggered diamond ice cubes and a bent straw extending into the drink.
Construction reference: Lucide cup-soda: tapered glass and wavy level; source supplies two diamond ice cubes and tall proportions."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4daf9729-9636-5534-8214-749f5664cd5b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iced-drink-with-two-cubes-and-bent-straw/20260929T033618Z-thuan-mac/reference/coffee coldbrew_4daf9729-9636-5534-8214-749f5664cd5b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'iced-drink-with-two-cubes-and-bent-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('coffee coldbrew',)

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

        path('glass',(6,12),[('L',(32,12)),('L',(42,12)),('L',(41,17)),('L',(38,42)),('A',(34,46),4,4,True),('L',(14,46)),('A',(10,42),4,4,True),('L',(7,17)),('L',(6,12))],True)
        path('liquid',(7,17),[('C',(24,17),(13,15),(18,19)),('C',(41,17),(30,15),(35,19))]);join('glass','liquid')
        poly('straw',(30,20),(32,12),(34,6),(40,4));join('glass','straw')
        poly('ice-upper',(19,23),(23,27),(19,31),(15,27),closed=True)
        poly('ice-lower',(27,32),(31,36),(27,40),(23,36),closed=True)
