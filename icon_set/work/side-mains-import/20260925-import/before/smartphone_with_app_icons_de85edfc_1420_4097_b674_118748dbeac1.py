'Smartphone with App Icons.\nPlan: Rounded phone with bottom bezel and one square app tile. Two reference tiles reduced to one to retain readable openings. Bounds8,4..40,44.\nReference: Lucide smartphone: rounded shell and sparse screen detail.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de85edfc-1420-4097-b674-118748dbeac1'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone small squares_de85edfc-1420-4097-b674-118748dbeac1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartphone-with-app-icons'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('smartphone', 'with', 'app', 'icons')

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

        path('phone',(12,4),[(36,4),((40,8),4,4,True),(40,34),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,34),(8,8),((12,4),4,4,True)],True)
        self.add_line('bezel',(8,34),(40,34));self.relate('connect','bezel','phone');box('app-tile',20,16,28,24,2)
