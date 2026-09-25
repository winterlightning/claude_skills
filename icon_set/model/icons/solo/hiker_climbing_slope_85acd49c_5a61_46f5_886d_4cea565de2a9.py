"""hiker-climbing-slope: Backpacked hiker stepping uphill and planting a pole on an inclined ground segment. Head center (28,9), radius 3; shoulder y20 gives exact 4-unit ink clearance. Ground shortened beneath the forward foot; minimal limbs preserve the climb."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '85acd49c-5a61-46f5-886d-4cea565de2a9'
SOURCE_PATH = 'pictographic-primitives/outdoors/trekking mountain_85acd49c-5a61-46f5-886d-4cea565de2a9.svg'
AUTHOR = 'gpt-6'

class HikerClimbingSlope(Solo48):
    icon_id = 'hiker-climbing-slope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('hiking', 'trekking', 'mountain', 'climb', 'backpack', 'pole', 'uphill', 'outdoors-batch-03')

    def build(self):
        # Plan: Backpacked hiker stepping uphill and planting a pole on an inclined ground segment. Head center (28,9), radius 3; shoulder y20 gives exact 4-unit ink clearance. Ground shortened beneath the forward foot; minimal limbs preserve the climb.
        # Lucide construction reference: backpack; original and atomic-debug inspected where named.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (6, 6, 42, 42).
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        circle('head',28,9,3)
        poly('body',(28,20),(24,24),(16,32),(6,42))
        poly('pack',(24,24),(14,16),(6,26),(16,32));join('pack','body')
        poly('front-leg',(16,32),(28,32),(30,34));join('front-leg','body')
        line('arm',(28,20),(42,20));join('arm','body')
        poly('pole',(42,16),(42,20),(42,30));join('pole','arm')
        line('slope',(30,34),(42,30));join('slope','front-leg');join('slope','pole')
