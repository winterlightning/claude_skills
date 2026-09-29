"""Four rounded fingers from shared 7-unit spacing, rounded thumb, broad palm and short cuff. Preserve five-digit glove identity while allowing compact finger spacing.
Construction: Lucide hand: rounded finger tips, shared finger junctions, smooth thumb-to-palm contour; source adds the glove cuff."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6288b5a8-887b-4031-b7cf-6d2c2cf7edf6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__latex-glove/20260928T175102Z-thuan-mac/reference/latex_6288b5a8-887b-4031-b7cf-6d2c2cf7edf6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'latex-glove'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('latex',)

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

        path('glove',(14,25),[('L',(14,14)),('C',(21,14),(14,8),(21,8)),('L',(21,10)),('C',(28,10),(21,4),(28,4)),('L',(28,12)),('C',(35,12),(28,6),(35,6)),('L',(35,17)),('C',(42,17),(35,11),(42,11)),('L',(42,29)),('C',(37,38),(42,33),(38,36)),('L',(37,42)),('L',(18,42)),('L',(18,38)),('C',(13,32),(18,36),(15,34)),('L',(6,23)),('C',(11,20),(3,19),(7,16)),('L',(17,27))])
        for j,(x,y) in enumerate([(21,14),(28,12),(35,17)]):
            line(f'finger-{j}',(x,y),(x,26));join('glove',f'finger-{j}')
