"""Restore the full horse silhouette with curved rump, tail, sloping chest and separate front/rear legs. Add an upright rider with a bent leg and forward arm.
Construction reference: human_ref/full_body_ref.png: upright rider head/body alignment; source defines complete horse silhouette."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bebbb6da-7e2b-58de-b56f-770e3a08a34d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horseback-rider/20260929T033618Z-thuan-mac/reference/outdoors horse_bebbb6da-7e2b-58de-b56f-770e3a08a34d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horseback-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('outdoors horse',)

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

        path('horse',(8,42),[('L',(8,32)),('C',(14,26),(8,28),(10,26)),('L',(29,26)),('L',(35,15)),('L',(36,20)),('L',(44,26)),('L',(42,29)),('L',(36,27)),('L',(33,34)),('L',(34,44)),('L',(29,44)),('L',(27,35)),('L',(15,35)),('L',(13,44)),('L',(8,44)),('L',(8,42))],True)
        path('tail',(10,28),[('C',(4,34),(5,26),(5,29))]);join('horse','tail')
        circle('head',20,7,3)
        line('torso',(20,18),(20,27))
        poly('arm',(20,18),(25,23),(30,23))
        poly('rider-leg',(20,27),(24,30),(24,34))
        join('torso','arm');join('torso','rider-leg')
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
