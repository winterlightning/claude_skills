'Security Access Key Symbol.\nSymbol plan: Circular left bow with beveled right shoulder joins broad toothed shaft. One prominent tooth replaces the small repeated notches; hole radius3 at(16,24).\nConstruction reference: Lucide key-round: integrated bow and shaft silhouette with an isolated hole.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ea86669-dd94-4c67-81eb-5997c3e0caf5'
SOURCE_PATH = 'pictographic-primitives/other/crypto encryption key_4ea86669-dd94-4c67-81eb-5997c3e0caf5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'security-key-with-notched-shaft'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('security', 'key', 'with', 'notched', 'shaft')

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

        path('key',(30,16),[(18,10),((4,24),14,14,False),((18,38),14,14,False),(30,32),(34,32),(34,24),(40,24),(44,20),(40,16),(30,16)],True)
        circle('hole',16,24,3)
