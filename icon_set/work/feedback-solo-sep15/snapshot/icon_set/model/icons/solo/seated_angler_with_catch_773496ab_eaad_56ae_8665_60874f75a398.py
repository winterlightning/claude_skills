"""seated-angler-with-catch: Seated person, curved rod and hanging fish form a natural scene. Head radius 3 at (37,13); shoulder y24 gives exactly 4 ink units. Small stool, fish silhouette and rod retained; tail and body retained; fish eye omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '773496ab-eaad-56ae-8665-60874f75a398'
SOURCE_PATH = 'pictographic-primitives/outdoors/fishing sit_773496ab-eaad-56ae-8665-60874f75a398.svg'
AUTHOR = 'gpt-6'


class SeatedAnglerWithCatch(Solo48):
    icon_id = 'seated-angler-with-catch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('fishing', 'angler', 'rod', 'fish', 'catch', 'sitting', 'hobby', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Plan: Seated person, curved rod and hanging fish form a natural scene. Head radius 3 at (37,13); shoulder y24 gives exactly 4 ink units. Small stool, fish silhouette and rod retained; tail and body retained; fish eye omitted.
        # Lucide fishing-rod original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (4, 8, 44, 40).
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
        circle('head',37,13,3)
        poly('body',(37,24),(37,32),(27,32),(27,40))
        line('arm',(37,24),(28,24));join('arm','body')
        path('rod',(12,8),[('A',(28,24),16,16,True)]);join('rod','arm')
        line('line',(12,8),(12,20));join('line','rod')
        poly('fish',(12,20),(20,24),(16,28),(18,32),(12,40),(6,32),(8,28),(4,24),closed=True);join('fish','line')
        poly('stool',(37,32),(44,32),(44,40));join('stool','body')
