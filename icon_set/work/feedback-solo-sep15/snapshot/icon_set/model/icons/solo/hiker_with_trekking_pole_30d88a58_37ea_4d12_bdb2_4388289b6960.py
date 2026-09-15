"""hiker-with-trekking-pole: Walking hiker with backpack, bent arm and planted pole. Head center (28,9), radius 3; shoulder y20 gives exact 4-unit ink gap. Shared torso/backpack attachment points keep the pose coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '30d88a58-37ea-4d12-bdb2-4388289b6960'
SOURCE_PATH = 'pictographic-primitives/outdoors/trekking person_30d88a58-37ea-4d12-bdb2-4388289b6960.svg'
AUTHOR = 'gpt-6'

class HikerWithTrekkingPole(Solo48):
    icon_id = 'hiker-with-trekking-pole'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('hiking', 'trekking', 'hiker', 'backpack', 'pole', 'walking', 'outdoors', 'outdoors-batch-03')

    def build(self):
        # Plan: Walking hiker with backpack, bent arm and planted pole. Head center (28,9), radius 3; shoulder y20 gives exact 4-unit ink gap. Shared torso/backpack attachment points keep the pose coherent.
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
        poly('body',(28,20),(24,25),(16,35),(26,35),(28,42))
        line('rear-leg',(16,35),(6,42));join('rear-leg','body')
        poly('pack',(24,25),(14,17),(6,27),(16,35));join('pack','body');join('pack','rear-leg')
        poly('arm',(28,20),(34,26),(41,26));join('arm','body')
        poly('pole',(42,18),(41,26),(40,34),(39,42));join('pole','arm')
