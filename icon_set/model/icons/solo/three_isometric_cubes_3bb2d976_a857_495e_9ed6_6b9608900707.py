'Three Isometric Cubes.\nPlan: Three attached isometric cubes in a compact stack. Equalized sizes preserve three readable faces per cube at48px. Bounds6..42.\nReference: Lucide boxes: shared Y-shaped face junctions; validated stacked-cube-pyramid construction used for generous openings.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bb2d976-a857-495e-9ed6-6b9608900707'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/tools and sdk 1_3bb2d976-a857-495e-9ed6-6b9608900707.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-isometric-cubes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'isometric', 'cubes')

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

        self.add_polyline('outline',(24,6),(33,11),(33,21),(42,26),(42,37),(33,42),(24,37),(15,42),(6,37),(6,26),(15,21),(15,11),closed=True)
        self.add_polyline('top-face',(15,11),(24,16),(33,11));self.add_polyline('center',(24,16),(24,26),(24,37));self.add_polyline('middle',(15,21),(24,26),(33,21))
        self.add_polyline('left-face',(6,26),(15,31),(24,26));self.add_line('left-edge',(15,31),(15,42));self.add_polyline('right-face',(24,26),(33,31),(42,26));self.add_line('right-edge',(33,31),(33,42))
        for a,b in [('outline','top-face'),('center','top-face'),('center','outline'),('middle','outline'),('middle','center'),('left-face','outline'),('left-face','center'),('left-face','middle'),('left-edge','left-face'),('left-edge','outline'),('right-face','outline'),('right-face','center'),('right-face','middle'),('right-face','left-face'),('right-edge','right-face'),('right-edge','outline')]:self.relate('connect',a,b)
