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

        path('dog',(42,42),[('C',(37,29),(38,38),(37,34)),('C',(29,31),(34,33),(32,34)),('L',(31,25)),('L',(26,25)),('C',(23,21),(24,25),(23,24)),('L',(23,18)),('L',(29,18)),('C',(33,15),(31,18),(31,15)),('L',(36,15)),('L',(39,6)),('C',(42,13),(41,8),(42,11))])
        circle('ball',24,33,4)
        path('hand',(6,23),[('C',(14,28),(11,24),(12,25)),('L',(17,32)),('C',(14,35),(19,34),(17,35)),('L',(11,33))])
        path('palm',(7,36),[('C',(11,40),(8,39),(9,40)),('L',(18,42))])
