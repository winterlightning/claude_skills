"""Cradled pregnant torso with heart. VRECT_XL extremes (5,2)-(43,46). Lucide heart informs paired lobes; profile is deliberately asymmetric. Finger detail omitted."""
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
        self.add_polyline('back', (8,2), (8,12), (5,30), (8,46))
        self.add_polyline('arm', (8,12), (16,14), (32,8))
        self.relate('connect', 'back', 'arm')
        self.add_line('chest', (32,2), (32,8))
        self.relate('connect', 'arm', 'chest')
        self.add_arc('bump-top', (32,8), (43,27), radius_x=22, radius_y=22)
        self.add_arc('bump-bottom', (43,27), (28,46), radius_x=20, radius_y=20)
        self.add_contour('bump', 'bump-top', 'bump-bottom')
        self.relate('connect', 'bump', 'arm')
        self.relate('connect', 'bump', 'chest')
        self.add_arc('heart-left', (24,24), (16,24), radius_x=4, sweep=False)
        self.add_line('heart-down', (16,24), (24,34))
        self.add_line('heart-up', (24,34), (32,24))
        self.add_arc('heart-right', (32,24), (24,24), radius_x=4, sweep=False)
        self.add_contour('heart', 'heart-left', 'heart-down', 'heart-up', 'heart-right', closed=True)
