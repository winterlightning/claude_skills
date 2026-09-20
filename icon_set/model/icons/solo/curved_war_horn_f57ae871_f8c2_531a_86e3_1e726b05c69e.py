'Curved Signal War Horn.\nPlan: Sweeping curved horn with wide elliptical bell, tapering lower tip. Decorative band omitted. Bounds6..42.\nReference: No useful local Lucide horn match; coherent source silhouette and elliptical opening.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f57ae871-f8c2-531a-86e3-1e726b05c69e'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-12/war horn_f57ae871-f8c2-531a-86e3-1e726b05c69e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-war-horn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
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
        path('horn',(22,12),[((6,26),16,14,True),((20,42),14,16,False),((42,12),22,30,False)]);self.relate('connect','rim','horn')
