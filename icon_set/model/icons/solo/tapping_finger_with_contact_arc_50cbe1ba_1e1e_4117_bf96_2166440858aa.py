'Finger Tap Gesture.\nPlan: Upright index finger and bent thumb below one broad contact arc. Second concentric arc omitted for clearance. Bounds6..42.\nReference: Lucide hand: rounded raised finger and coherent palm; shared human-part vocabulary.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50cbe1ba-1e1e-4117-bf96-2166440858aa'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gesture tap 1_50cbe1ba-1e1e-4117-bf96-2166440858aa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapping-finger-with-contact-arc'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tapping', 'finger', 'with', 'contact', 'arc')

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

        path('contact',(6,22),[((42,22),18,16,True)])
        path('hand',(14,42),[(6,34),((14,30),8,4,True),(20,36),(20,24),((28,24),4,4,True),(28,30),(34,34),(34,42)])
