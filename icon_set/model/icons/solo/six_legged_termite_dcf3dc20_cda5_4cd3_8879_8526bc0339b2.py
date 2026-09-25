'Termite Pest Insect.\nPlan: Small round head, elongated body and three paired legs at shared side junctions. Antennae meet head top; thorax seam omitted. Bounds6..42.\nReference: Lucide bug: repeated paired legs and single rounded body. Source termite keeps long abdomen.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcf3dc20-cda5-4cd3-8879-8526bc0339b2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/termite_dcf3dc20-cda5-4cd3-8879-8526bc0339b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-legged-termite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('six', 'legged', 'termite')

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

        circle('head',24,14,5)
        path('body',(24,19),[((32,27),8,8,True),(32,28),(32,34),((24,42),8,8,True),((16,34),8,8,True),(16,28),(16,27),((24,19),8,8,True)],True);self.relate('connect','head','body')
        self.add_polyline('antennae',(18,6),(24,9),(30,6));self.relate('connect','antennae','head')
        for side,x,end in [('left',16,6),('right',32,42)]:
         self.add_polyline(f'legs-{side}',(end,18),(x,28),(end,40));self.add_line(f'middle-leg-{side}',(x,28),(end,28));self.relate('connect',f'legs-{side}','body');self.relate('connect',f'middle-leg-{side}','body');self.relate('connect',f'middle-leg-{side}',f'legs-{side}')
