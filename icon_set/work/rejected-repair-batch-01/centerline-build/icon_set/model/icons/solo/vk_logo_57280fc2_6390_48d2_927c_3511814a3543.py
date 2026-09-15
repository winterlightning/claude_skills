"""Curved V joins a shared upright K stem with two diagonal arms. Reduce the thick outline to a coherent monoline ligature."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57280fc2-6390-48d2-927c-3511814a3543'
SOURCE_PATH = 'pictographic-primitives/logos/vk logo_57280fc2-6390-48d2-927c-3511814a3543.svg'
AUTHOR = 'gpt-6'

class VkLogo(Solo48):
    icon_id = 'vk-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('vk', 'vkontakte', 'social', 'letters', 'logo', 'brand', 'russian')

    def build(self):
        # Plan: Curved V joins a shared upright K stem with two diagonal arms. Reduce the thick outline to a coherent monoline ligature.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_bezier('v',(4,8),((8,30),(14,40),(24,40)))
        self.add_polyline('stem',(24,40),(24,24),(24,8))
        self.add_polyline('k',(42,8),(24,24),(44,40));self.relate('connect','v','stem');self.relate('connect','stem','k')

