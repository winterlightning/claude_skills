'Task list: three straight baselines with even 9-unit spacing and balanced margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68f6dae1-f30e-46ca-8af8-fead1c27b152'
SOURCE_PATH = 'icons-json/office/task list text_68f6dae1-f30e-46ca-8af8-fead1c27b152.json'
AUTHOR = 'gpt-6'

class TaskListText(Solo48):
    icon_id = 'task-list-text'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('task', 'list', 'text', 'office')

    def build(self):
        # Task list: three straight baselines with even 9-unit spacing and balanced margins.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('page',6,6,42,42,3)
        for y,end in ((15,33),(24,33),(33,27)):
            l(f'text-{y}',(15,y),(end,y))
