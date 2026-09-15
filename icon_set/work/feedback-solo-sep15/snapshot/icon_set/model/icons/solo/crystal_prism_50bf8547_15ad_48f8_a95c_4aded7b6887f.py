"""Crystal. Retains the pointed caps and central vertical edge; broad side faces keep all facet openings clear.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide gem: shared facet vertices and consistent straight edges; source sets the upright pointed hexagonal prism.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50bf8547-15ad-48f8-a95c-4aded7b6887f'
SOURCE_PATH = 'pictographic-primitives/symbol/crystal_50bf8547-15ad-48f8-a95c-4aded7b6887f.svg'
AUTHOR = 'gpt-6'


class CrystalPrism(Solo48):
    icon_id = 'crystal-prism'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('crystal', 'gem', 'gemstone', 'quartz', 'mineral', 'jewel', 'magic', 'prism')

    def build(self) -> None:
        self.add_polyline('outline', (24, 4), (40, 14), (40, 34), (24, 44), (8, 34), (8, 14), closed=True)
        self.add_polyline('top-facet', (8, 14), (24, 20), (40, 14))
        self.add_polyline('bottom-facet', (8, 34), (24, 28), (40, 34))
        self.add_line('center-edge', (24, 20), (24, 28))
        self.relate("connect", 'outline', 'top-facet')
        self.relate("connect", 'outline', 'bottom-facet')
        self.relate("connect", 'top-facet', 'center-edge')
        self.relate("connect", 'bottom-facet', 'center-edge')
