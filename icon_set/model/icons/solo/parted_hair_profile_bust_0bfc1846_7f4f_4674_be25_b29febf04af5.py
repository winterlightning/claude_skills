'Simple Person Avatar.\n\nSymbol plan: Circular face radius11 centered (24,15), with a two-arc parted fringe. Elliptical shoulders centered (24,44), radii16/14, reach y30. Head bottom y26; 4-unit centerline separation gives zero ink gap. Collar and sleeve seams omitted.\nConstruction reference: human_ref/user.svg: circular face and rounded shoulders; avatar contact rule.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0bfc1846-7f4f-4674-be25-b29febf04af5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/step grandmother_0bfc1846-7f4f-4674-be25-b29febf04af5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'parted-hair-profile-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('parted', 'hair', 'profile', 'bust')

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
        path('hair',(13,15),[((24,10),11,11,False),((35,15),11,11,False)])
        self.relate('connect','head','hair')
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=14)
        self.add_contour('body','body-top')
        self.relate('connect','head','body')
