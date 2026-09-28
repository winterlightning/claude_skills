"""Smooth the belly using matched vertical tangents and balance the arm curve across the torso. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd8bedcbd-494e-5cf0-967f-4c5dac6cee67'
SOURCE_PATH = 'pictographic-primitives/babies/pregnancy hug_d8bedcbd-494e-5cf0-967f-4c5dac6cee67.svg'
AUTHOR = 'gpt-6'

class PregnantBellyWithHeart(Solo48):
    icon_id = 'pregnant-belly-with-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ('pregnancy-hug', 'baby-bump')
    keywords = ('pregnancy', 'belly', 'bump', 'expecting', 'heart', 'maternity', 'mother', 'prenatal')

    def build(self) -> None:
        """Symbol plan: Smooth the belly using matched vertical tangents and balance the arm curve across the torso. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_polyline('back', (8, 4), (8, 8), (8, 44))
        self.add_arc('arm-left', (8, 8), (20, 13), radius_x=12, radius_y=5, sweep=False)
        self.add_arc('arm-right', (20, 13), (32, 8), radius_x=12, radius_y=5, sweep=False)
        self.add_contour('arm', 'arm-left', 'arm-right')
        self.relate('connect', 'back', 'arm')
        self.add_line('chest', (32, 4), (32, 8))
        self.add_arc('belly-top', (32, 8), (40, 27), radius_x=8, radius_y=19)
        self.add_arc('belly-bottom', (40, 27), (28, 44), radius_x=12, radius_y=17)
        self.add_contour('belly', 'belly-top', 'belly-bottom')
        self.relate('connect', 'arm', 'chest')
        self.relate('connect', 'arm', 'belly')
        self.relate('connect', 'chest', 'belly')
        self.add_arc('heart-left', (24, 25), (17, 25), radius_x=4, sweep=False)
        self.add_arc('heart-shoulder-left', (17, 25), (18, 30), radius_x=7, sweep=False)
        self.add_line('heart-down', (18, 30), (24, 37))
        self.add_line('heart-up', (24, 37), (30, 30))
        self.add_arc('heart-shoulder-right', (30, 30), (31, 25), radius_x=7, sweep=False)
        self.add_arc('heart-right', (31, 25), (24, 25), radius_x=4, sweep=False)
        self.add_contour('heart', 'heart-left', 'heart-shoulder-left', 'heart-down', 'heart-up', 'heart-shoulder-right', 'heart-right', closed=True)
