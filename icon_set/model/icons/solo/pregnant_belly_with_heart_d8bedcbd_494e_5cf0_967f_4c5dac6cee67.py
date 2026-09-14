"""Pregnant belly with an intrinsic heart, using a straight back, curved cradling arm and smooth elliptical belly. VRECT_XL preserves the vertical profile. Lucide heart informs paired lobes and smooth shoulders; the body profile is deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd8bedcbd-494e-5cf0-967f-4c5dac6cee67'
SOURCE_PATH = 'pictographic-primitives/babies/pregnancy hug_d8bedcbd-494e-5cf0-967f-4c5dac6cee67.svg'
AUTHOR = 'gpt-6'

class PregnantBellyWithHeart(Solo48):
    icon_id = 'pregnant-belly-with-heart'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/maternity'
    aliases = ('pregnancy-hug', 'baby-bump')
    keywords = ('pregnancy', 'belly', 'bump', 'expecting', 'heart', 'maternity', 'mother', 'prenatal')

    def build(self) -> None:
        # VRECT_XL centerline extremes (6,6)-(42,42).
        self.add_polyline('back', (6,6), (6,8), (6,42))
        self.add_arc('arm-left', (6,8), (17,14), radius_x=12, radius_y=6, sweep=False)
        self.add_arc('arm-right', (17,14), (32,8), radius_x=15, radius_y=6, sweep=False)
        self.add_contour('arm', 'arm-left', 'arm-right')
        self.relate('connect', 'back', 'arm')
        self.add_line('chest', (32,6), (32,8))
        self.add_arc('belly-top', (32,8), (42,27), radius_x=11, radius_y=19)
        self.add_arc('belly-bottom', (42,27), (28,42), radius_x=15, radius_y=19)
        self.add_contour('belly', 'belly-top', 'belly-bottom')
        self.relate('connect', 'arm', 'chest')
        self.relate('connect', 'arm', 'belly')
        self.relate('connect', 'chest', 'belly')
        self.add_arc('heart-left', (24,25), (16,25), radius_x=4, sweep=False)
        self.add_arc('heart-shoulder-left', (16,25), (18,30), radius_x=7, sweep=False)
        self.add_line('heart-down', (18,30), (24,37))
        self.add_line('heart-up', (24,37), (30,30))
        self.add_arc('heart-shoulder-right', (30,30), (32,25), radius_x=7, sweep=False)
        self.add_arc('heart-right', (32,25), (24,25), radius_x=4, sweep=False)
        self.add_contour('heart', 'heart-left', 'heart-shoulder-left', 'heart-down', 'heart-up', 'heart-shoulder-right', 'heart-right', closed=True)
