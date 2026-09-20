'Closed Door with Doorknob.\n\nSymbol plan: A plain upright door panel and small round knob. Panel exact (10,4)-(38,44); knob radius2 centered (27,26).\nConstruction reference: Lucide door-closed: uncluttered upright panel with a single knob.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d6b19e3-10f3-472b-a10f-0b9247ed5ce6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/door closed_0d6b19e3-10f3-472b-a10f-0b9247ed5ce6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'closed-door-with-doorknob'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('closed', 'door', 'with', 'doorknob')

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

        self.add_polyline('door',(10,4),(38,4),(38,44),(10,44),closed=True)
        circle('knob',27,26,2)
