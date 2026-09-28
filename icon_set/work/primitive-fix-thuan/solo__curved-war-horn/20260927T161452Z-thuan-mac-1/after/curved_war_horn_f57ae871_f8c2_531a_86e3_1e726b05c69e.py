'Curved Signal War Horn.\nPlan: Sweeping curved horn with wide elliptical bell, tapering lower tip. Decorative band omitted. Bounds6..42.\nReference: No useful local Lucide horn match; coherent source silhouette and elliptical opening.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f57ae871-f8c2-531a-86e3-1e726b05c69e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-war-horn/20260927T161452Z-thuan-mac-1/reference/war horn_f57ae871-f8c2-531a-86e3-1e726b05c69e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-war-horn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('curved', 'war', 'horn')

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

        path('rim',(22,12),[((42,12),10,6,True),((22,12),10,6,True)],True)
        # Lift the narrow horn tip as in the source's open, upward sweep.
        self.add_bezier('horn-inner',(22,12),((16,20),(10,22),(6,20)))
        self.add_bezier('horn-outer',(6,20),((6,34),(12,42),(20,42)))
        self.add_arc('horn-body',(20,42),(42,12),radius_x=22,radius_y=30,sweep=False)
        self.add_contour('horn','horn-inner','horn-outer','horn-body')
        self.relate('connect','rim','horn')
