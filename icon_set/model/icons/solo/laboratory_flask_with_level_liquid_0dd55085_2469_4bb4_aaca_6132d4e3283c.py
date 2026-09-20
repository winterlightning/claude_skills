'Erlenmeyer Science Laboratory Flask.\nPlan: Conical flask with narrow neck, projecting lip and shared horizontal liquid level. Bounds8,4..40,44.\nReference: Lucide flask-conical: narrow neck, sloping vessel and shared liquid boundary.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0dd55085-2469-4bb4-aaca-6132d4e3283c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/lab_0dd55085-2469-4bb4-aaca-6132d4e3283c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laboratory-flask-with-level-liquid'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('laboratory', 'flask', 'with', 'level', 'liquid')

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

        self.add_polyline('lip',(16,4),(20,4),(28,4),(32,4))
        path('flask',(20,4),[(20,16),(14,28),(8,40),((12,44),4,4,False),(36,44),((40,40),4,4,False),(34,28),(28,16),(28,4)]);self.relate('connect','lip','flask')
        self.add_line('liquid',(14,28),(34,28));self.relate('connect','liquid','flask')
