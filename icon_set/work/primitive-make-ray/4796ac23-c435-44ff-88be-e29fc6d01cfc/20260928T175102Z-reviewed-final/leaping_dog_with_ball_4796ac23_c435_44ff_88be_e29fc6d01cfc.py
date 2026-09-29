"""Smooth dog head in profile, upright ear, curved neck and throat, separate ball and a minimal presenting hand. Keep the complete source composition.
Construction: Lucide dog: smooth muzzle and distinct ear; source controls side profile, ball and hand."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4796ac23-c435-44ff-88be-e29fc6d01cfc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leaping-dog-with-ball/20260928T175102Z-thuan-mac/reference/dog bring ball training_4796ac23-c435-44ff-88be-e29fc6d01cfc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leaping-dog-with-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('dog bring ball training',)

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

        path('dog',(42,42),[('C',(37,29),(38,38),(37,34)),('C',(31,30),(34,32),(33,33)),('C',(33,23),(29,28),(33,26)),('L',(28,23)),('C',(25,20),(26,23),(25,22)),('L',(25,16)),('L',(31,16)),('C',(35,13),(33,16),(33,13)),('L',(37,13)),('L',(40,6)),('C',(42,14),(42,9),(42,11))])
        circle('ball',22,34,3)
        path('hand',(6,24),[('C',(10,28),(8,25),(9,26)),('L',(11,30)),('C',(9,33),(13,32),(12,34)),('L',(7,32))])
        path('palm',(6,37),[('C',(10,40),(7,39),(8,40)),('L',(14,42))])

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Preserve dog, ball and presenting hand in one 48 px scene. Compact hand anatomy and muzzle/ball spacing are visible in both themes, with no ball contact or missing composition elements.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9790ba92ef820c5c372b482e0c9f79222c1d2c7380fcc3f87df05f681186e6cd'}
