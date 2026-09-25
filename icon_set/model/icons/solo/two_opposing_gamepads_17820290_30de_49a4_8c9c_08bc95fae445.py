'Two Stacked Game Controllers.\n\nSymbol plan: Two identical mirrored controller silhouettes with inward notches and outward grips. Shared horizontal axis y=24. Tiny control marks omitted to keep 8-unit clearances.\nConstruction reference: Lucide gamepad-2: one rounded grip silhouette; two source controllers retained.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17820290-30de-49a4-8c9c-08bc95fae445'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-08/one vs one mode 1_17820290-30de-49a4-8c9c-08bc95fae445.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-opposing-gamepads'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    aliases = ()
    keywords = ('two', 'opposing', 'gamepads')

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

        for j,sy in enumerate((1,-1)):
            def pt(x,y): return (x,24+sy*(y-24))
            start=pt(6,12)
            steps=[(pt(18,12),6,6,True if sy==1 else False),pt(30,12),(pt(42,12),6,6,True if sy==1 else False),pt(42,14),(pt(36,20),6,6,True if sy==1 else False),pt(12,20),(pt(6,14),6,6,True if sy==1 else False),start]
            path(f'controller-{j}',start,steps,True)
