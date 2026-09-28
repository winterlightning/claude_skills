"""Toy Water Gun.
Plan: Water pistol outline owns the nozzle, slanted handle and attached guard. Centerline extremes (4,8)-(44,40).
Reference: No useful Lucide water-pistol match; tangent rounded rear and shared attachments.
Reduction: Body seam omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b55ad954-b536-58ab-8693-df90fc548d1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/party water gun_b55ad954-b536-58ab-8693-df90fc548d1a.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'water-pistol-flared-nozzle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    categories = ("entertainment", "primitives")
    aliases = ()
    keywords = ('toy', 'water', 'gun')

    def build(self):
        points=((10,8),(34,8),(34,12),(44,8),(44,24),(34,20),(30,20),(20,20),(17,30),(14,40),(4,40),(10,20),(4,20),(4,14))
        ids=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            name=f'edge-{i}';self.add_line(name,a,b);ids.append(name)
        self.add_arc('rear',(4,14),(10,8),radius_x=6)
        self.add_contour('outline',*ids,'rear',closed=True)
        self.add_arc('guard',(30,20),(17,30),radius_x=13,radius_y=10)
        self.relate('connect','outline','guard')
