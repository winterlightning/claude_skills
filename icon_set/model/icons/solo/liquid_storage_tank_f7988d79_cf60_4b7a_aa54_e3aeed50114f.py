'Liquid Tank Level Indicator.\nPlan: Broad rounded tank, upper-right cap and one wave dividing liquid from air. Bounds6..42.\nReference: Lucide glass-water: shared water boundary and vessel; source cap position retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7988d79-cf60-4b7a-aa54-e3aeed50114f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tankful_f7988d79-cf60-4b7a-aa54-e3aeed50114f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'liquid-storage-tank'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('liquid', 'storage', 'tank')

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

        path('tank',(10,14),[(30,14),(38,14),((42,18),4,4,True),(42,26),(42,38),((38,42),4,4,True),(10,42),((6,38),4,4,True),(6,26),(6,18),((10,14),4,4,True)],True)
        self.add_polyline('cap',(30,14),(30,6),(38,6),(38,14));self.relate('connect','cap','tank')
        path('water',(6,26),[((24,26),9,2,False),((42,26),9,2,True)]);self.relate('connect','water','tank')
