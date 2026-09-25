'Reply Message Bubble.\n\nSymbol plan: One bubble border with integrated return arrow in upper edge and lower-left tail. Rounded corners radius6; bounds (6,6)-(42,42). Arrow is intrinsic border feature.\nConstruction reference: Lucide message-circle-reply: clear reply arrow and speech tail; source rectangular border retained.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf2a7a37-b7f1-41c0-b15c-ac3ea1e05002'
SOURCE_PATH = 'pictographic-primitives/other/message bubble arrow_cf2a7a37-b7f1-41c0-b15c-ac3ea1e05002.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'reply-speech-bubble'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('container', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('reply', 'speech', 'bubble')

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

        path('bubble',(14,10),[(12,10),((6,16),6,6,False),(6,30),((12,36),6,6,False),(12,42),(22,36),(36,36),((42,30),6,6,False),(42,16),((36,10),6,6,False),(24,10)])
        self.add_polyline('arrow',(30,6),(24,10),(30,16))
        self.relate('connect','bubble','arrow')
