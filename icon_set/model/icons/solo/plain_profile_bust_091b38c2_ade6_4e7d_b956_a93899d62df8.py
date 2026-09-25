'Simple Person Profile Avatar.\n\nSymbol plan: Plain circular head radius11 centered(24,15), head bottom26. Elliptical shoulders centered(24,44), radii16/14, start at y30. Exactly4 centerline units / zero ink gap. Neck and collar omitted.\nConstruction reference: human_ref/user.svg: circular head, rounded shoulder contour; avatar touching rule.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '091b38c2-ade6-4e7d-b956-a93899d62df8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/step brother_091b38c2-ade6-4e7d-b956-a93899d62df8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'plain-profile-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('plain', 'profile', 'bust')

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

        self.add_arc('head-top',(13,15),(35,15),radius_x=11)
        self.add_arc('head-bottom',(35,15),(13,15),radius_x=11)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=14)
        self.add_contour('body','body-top')
        self.relate('connect','head','body')
