'Square Selection Bounding Box.\nSymbol plan: Four equal8x8 corner handles joined by straight edges. Mirrored on both axes; center stays empty.\nConstruction reference: Lucide scan: repeated corner construction; source closed square handles retained.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '160c5423-2171-44a3-b5aa-55e80961b5a6'
SOURCE_PATH = 'pictographic-primitives/other/square block_160c5423-2171-44a3-b5aa-55e80961b5a6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'square-selection-corner-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('square', 'selection', 'corner', 'handles')

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

        for j,(x,y) in enumerate(((6,6),(34,6),(34,34),(6,34))):
         self.add_polyline(f'corner-{j}',(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        for j,(a,b,c1,c2) in enumerate([((14,10),(34,10),0,1),((38,14),(38,34),1,2),((34,38),(14,38),2,3),((10,34),(10,14),3,0)]):
         self.add_line(f'edge-{j}',a,b)
         self.relate('connect',f'edge-{j}',f'corner-{c1}');self.relate('connect',f'edge-{j}',f'corner-{c2}')
