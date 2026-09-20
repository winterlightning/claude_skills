'Modern Lounge Chair.\nSymbol plan: Side-view padded seat, upright tilted back and single pedestal. Seat thickness10, pedestal at32, base y40.\nConstruction reference: Lucide armchair: rounded padded outline with explicit support attachments; side-view preserved.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da2ca27e-78de-46d5-9408-c53eae1490a8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_19/footrest_da2ca27e-78de-46d5-9408-c53eae1490a8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pedestal-lounge-chair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pedestal', 'lounge', 'chair')

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

        path('seat',(10,22),[(30,22),(34,8),(44,8),(40,26),((34,32),6,6,True),(32,32),(10,32),((10,22),6,5,True)],True)
        self.add_line('support',(32,32),(32,40))
        self.add_polyline('base',(18,40),(32,40),(42,40))
        self.relate('connect','seat','support')
        self.relate('connect','base','support')
