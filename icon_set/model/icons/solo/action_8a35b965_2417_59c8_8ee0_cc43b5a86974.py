'Action flowchart: balanced terminal, decision and process nodes with clean connecting edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a35b965-2417-59c8-8ee0-cc43b5a86974'
SOURCE_PATH = 'pictographic-primitives/diagrams/action_8a35b965-2417-59c8-8ee0-cc43b5a86974.svg'
AUTHOR = 'gpt-6'

class Action(Solo48):
    icon_id = 'action'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('action', 'diagrams')

    def build(self):
        # Action flowchart: balanced terminal, decision and process nodes with clean connecting edges.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

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

        r('start',8,8,24,16,4)
        p('decision',(16,16),(28,24),(16,32),(4,24),(16,16))
        c('end',16,36,4)
        r('process',32,18,44,30,2)
        l('branch',(28,24),(32,24))
        link('connect','start','decision')
        link('connect','end','decision')
        link('connect','branch','decision')
        link('connect','branch','process')
