'Handheld Hair Dryer Blowing Air.\nPlan: Rounded horizontal dryer housing, attached handle and three separated airflow waves. Cord omitted. Bounds4,8..44,40.\nReference: Lucide wind: repeated shallow airflow curves; source dryer barrel and handle retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92b3ba61-efc9-446c-83d0-a1f1cd01946e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/hair dryer_92b3ba61-efc9-446c-83d0-a1f1cd01946e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hair-dryer-with-air-streams'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hair', 'dryer', 'with', 'air', 'streams')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('housing',(12,8),[(24,8),((28,12),4,4,True),(28,20),((24,24),4,4,True),(20,24),(12,24),((4,16),8,8,True),((12,8),8,8,True)],True)
        path('handle',(12,24),[(12,36),((20,36),4,4,False),(20,24)]);self.relate('connect','handle','housing')
        for j,y in enumerate((10,20,30)):path(f'air-{j}',(36,y),[((40,y),2,1,False),((44,y),2,1,True)])
