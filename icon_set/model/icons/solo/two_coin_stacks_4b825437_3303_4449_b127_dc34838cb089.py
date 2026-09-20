'Two Stacks of Coins.\nPlan: Three coins in the tall left stack and two in the shorter right stack. One left coin omitted; repeated ellipse seams and shared sidewalls. Bounds6..42.\nReference: Lucide coins: rounded currency forms; source stacked cylinders reconstructed with repeated ellipses.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b825437-3303-4449-b127-dc34838cb089'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/accounting coins stack 1_4b825437-3303-4449-b127-dc34838cb089.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-coin-stacks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('two', 'coin', 'stacks')

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

        for j,(l,r,top,levels) in enumerate(((6,20,9,(19,29,39)),(30,42,19,(29,39)))):
         rx=(r-l)//2
         steps=[((r,top),rx,3,True)]+[(r,y) for y in levels]+[((l,levels[-1]),rx,3,True)]+[(l,y) for y in reversed((top,)+levels[:-1])]
         path(f'stack-{j}',(l,top),steps,True)
         for k,y in enumerate((top,)+levels[:-1]):path(f'coin-{j}-{k}',(l,y),[((r,y),rx,3,False)]);self.relate('connect',f'coin-{j}-{k}',f'stack-{j}')
