'Retractable Measuring Tape Tool.\nPlan: Rounded tape housing with circular spindle and short extended strip. Tick marks omitted from narrow strip. Bounds4,8..44,40.\nReference: Lucide ruler: strong measurement-tool silhouette; source rounded housing retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bda009e-9307-44d2-81d1-0e1d95fcd9f0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tape measure_7bda009e-9307-44d2-81d1-0e1d95fcd9f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retractable-measuring-tape-tool'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('retractable', 'measuring', 'tape', 'tool')

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

        path('housing',(12,8),[(24,8),((32,16),8,8,True),(32,30),(32,32),((24,40),8,8,True),(12,40),((4,32),8,8,True),(4,16),((12,8),8,8,True)],True)
        circle('spindle',18,22,5)
        self.add_polyline('tape',(32,30),(44,30),(44,40),(24,40));self.relate('connect','tape','housing')
