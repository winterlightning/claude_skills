"""A smiling oval face sits beneath two large symmetrical lobes that sweep outward and hang down beside the cheeks. A circular ornament rests at the forehead, with short angular lines rising from the temples.

HRECT_XL visible bounds (2,6)-(46,42); central smiling face, paired hanging lobes and forehead ornament. Eyes and temple marks omitted. No useful exact Lucide match; mirrored lobe dimensions and shared ornament attachments.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cbfd2f8-04d6-4b91-b205-3ee8299e6715'
SOURCE_PATH = 'pictographic-primitives/science/lethan lutian_1cbfd2f8-04d6-4b91-b205-3ee8299e6715.svg'
AUTHOR = 'gpt-6'

class AlienHeadTwinHangingLobes(Solo48):
    icon_id = 'alien-head-twin-hanging-lobes'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('twilek', 'alien', 'head', 'headdress', 'face', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('inner-left',(21,18),(14,8),radius_x=7,radius_y=10,sweep=False)
        self.add_arc('outer-left',(14,8),(4,24),radius_x=10,radius_y=16,sweep=False)
        self.segments('lobe-left',(4,24),(4,40),(12,32),(12,24))
        self.add_arc('face',(12,24),(36,24),radius_x=12,radius_y=16,sweep=False)
        self.segments('lobe-right',(36,24),(36,32),(44,40),(44,24))
        self.add_arc('outer-right',(44,24),(34,8),radius_x=10,radius_y=16,sweep=False)
        self.add_arc('inner-right',(34,8),(27,18),radius_x=7,radius_y=10,sweep=False)
        self.add_contour('outline','inner-left','outer-left','lobe-left-1','lobe-left-2','lobe-left-3','face','lobe-right-1','lobe-right-2','lobe-right-3','outer-right','inner-right')
        self.circle('ornament',24,18,3)
        self.relate('connect','outline','ornament')
        self.add_arc('smile',(22,29),(26,29),radius_x=3,sweep=False)
