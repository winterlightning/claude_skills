"""Restore distinct outward-facing noses, chins and necks, with an offset rear skull and a central heart. Preserve the source open contour arrangement.
Construction reference: Shared human profile guidance and supplied opposing-head reference; no useful exact Lucide composition."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '26e8f72f-fceb-4a4f-95db-e00ca1a93624'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-profiles-with-heart/20260929T033618Z-thuan-mac/reference/empathy authentication heart intersect_26e8f72f-fceb-4a4f-95db-e00ca1a93624.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-profiles-with-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('empathy authentication heart intersect',)

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

        path('left-profile',(13,13),[('C',(7,22),(9,15),(8,18)),('L',(4,29)),('L',(8,29)),('L',(8,34)),('A',(12,38),4,4,False),('L',(15,38)),('L',(15,44))])
        path('right-profile',(18,9),[('C',(28,4),(20,5),(24,4)),('C',(39,16),(35,4),(38,9)),('L',(44,25)),('L',(40,25)),('L',(40,31)),('A',(36,35),4,4,True),('L',(33,35)),('L',(33,40))])
        poly('inner-neck',(25,44),(25,37),(27,32))
        path('heart',(24,17),[('C',(16,18),(20,12),(16,13)),('C',(24,28),(16,21),(20,25)),('C',(32,18),(28,25),(32,21)),('C',(24,17),(32,13),(28,12))],True)
