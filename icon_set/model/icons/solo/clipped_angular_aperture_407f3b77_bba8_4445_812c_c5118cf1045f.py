'Camera Lens Aperture Symbol.\nSymbol plan: Clipped asymmetric frame and four interlocking bands around a central square. Frame box(6,6)-(42,42); central aperture(18,18)-(30,30).\nConstruction reference: Lucide aperture: rotating shared blade junctions; source clipped outer frame retained.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '407f3b77-bba8-4445-812c-c5118cf1045f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/affinity photo logo_407f3b77-bba8-4445-812c-c5118cf1045f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'clipped-angular-aperture'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('clipped', 'angular', 'aperture')

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

        self.add_polyline('frame',(18,6),(30,6),(42,6),(42,18),(42,30),(42,42),(30,42),(18,42),(6,42),(6,30),(6,18),closed=True)
        self.add_polyline('aperture',(18,18),(30,18),(30,30),(18,30),closed=True)
        for j,(a,b) in enumerate([((18,6),(30,18)),((42,18),(30,30)),((30,42),(18,30)),((6,30),(18,18))]):
         self.add_line(f'blade-{j}',a,b)
         self.relate('connect',f'blade-{j}','frame')
         self.relate('connect',f'blade-{j}','aperture')
