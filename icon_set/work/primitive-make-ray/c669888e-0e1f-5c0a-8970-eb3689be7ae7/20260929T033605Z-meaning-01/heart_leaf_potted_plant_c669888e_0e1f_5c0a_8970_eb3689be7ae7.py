"""Restore one upright heart leaf, two smaller outward-facing heart leaves and three stems entering a deep tapered pot.
Construction reference: Lucide sprout: joined leaf/stem structure; source supplies three heart leaves and pot."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c669888e-0e1f-5c0a-8970-eb3689be7ae7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-leaf-potted-plant/20260929T033618Z-thuan-mac/reference/indoor plant_c669888e-0e1f-5c0a-8970-eb3689be7ae7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-leaf-potted-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('indoor plant',)

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

        path('top-leaf',(24,8),[('C',(17,8),(18,1),(15,4)),('C',(24,18),(17,12),(20,15)),('C',(31,8),(28,15),(31,12)),('C',(24,8),(33,4),(30,1))],True)
        path('left-leaf',(17,27),[('C',(7,26),(12,29),(5,29)),('C',(10,21),(5,23),(8,20)),('C',(11,17),(7,17),(8,15)),('C',(17,27),(15,17),(17,23))],True)
        path('right-leaf',(31,27),[('C',(41,26),(36,29),(43,29)),('C',(38,21),(43,23),(40,20)),('C',(37,17),(41,17),(40,15)),('C',(31,27),(33,17),(31,23))],True)
        line('stem',(24,18),(24,32));line('stem-left',(17,27),(20,32));line('stem-right',(31,27),(28,32))
        path('pot',(12,32),[('L',(36,32)),('L',(33,42)),('A',(30,44),3,3,True),('L',(18,44)),('A',(15,42),3,3,True),('L',(12,32))],True)
        for leaf,stem in [('top-leaf','stem'),('left-leaf','stem-left'),('right-leaf','stem-right')]:join(leaf,stem);join('pot',stem)
