'Modern Music Headphones.\nSymbol plan: Symmetric arch reaches y6. Two rounded ear cushions width10 from y24 to42; separate external housings omitted.\nConstruction reference: Lucide headphones: continuous headband and rounded integrated ear cups.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '850fa91f-25e7-48df-92ee-d13bde0423ff'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/headset_850fa91f-25e7-48df-92ee-d13bde0423ff.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'padded-over-ear-headphones'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('padded', 'over', 'ear', 'headphones')

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

        path('band',(6,29),[(6,24),((24,6),18,18,True),((42,24),18,18,True),(42,29)])
        path('left-cup',(6,29),[((16,29),5,5,True),(16,37),((6,37),5,5,True),(6,29)],True)
        path('right-cup',(32,29),[((42,29),5,5,True),(42,37),((32,37),5,5,True),(32,29)],True)
        self.relate('connect','band','left-cup');self.relate('connect','band','right-cup')
