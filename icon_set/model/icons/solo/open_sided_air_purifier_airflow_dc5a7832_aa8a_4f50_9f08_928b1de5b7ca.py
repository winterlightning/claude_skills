'Air Purifier with Airflow.\nPlan: Tall open-sided housing, short base division and three shallow airflow waves. Bounds6..42.\nReference: Lucide wind: repeated smooth streams; source open purifier enclosure retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc5a7832-aa8a-4f50-9f08-928b1de5b7ca'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/air purifier 4_dc5a7832-aa8a-4f50-9f08-928b1de5b7ca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-sided-air-purifier-airflow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'sided', 'air', 'purifier', 'airflow')

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

        path('housing',(16,6),[(10,6),((6,10),4,4,False),(6,32),(6,38),((10,42),4,4,False),(16,42)])
        self.add_line('base',(6,32),(16,32));self.relate('connect','base','housing')
        for j,y in enumerate((14,24,34)):path(f'air-{j}',(26,y),[((34,y),4,1,False),((42,y),4,1,True)])
