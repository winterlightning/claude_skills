"""A classical building facade: a shallow pitched pediment on top, three thick columns beneath it, and a long base bar at the bottom.

Plan: Three equal columns between shallow pediment and baseline.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: landmark: repeated columns, pitched pediment, baseline.
Simplification: Outlined columns and pediment become monoline strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bee109f7-7025-4eb4-9ddc-33b7df1410c4'
SOURCE_PATH = 'pictographic-primitives/logos/internet archive logo_bee109f7-7025-4eb4-9ddc-33b7df1410c4.svg'
AUTHOR = 'gpt-6'


class InternetArchiveLogo(Solo48):
    icon_id = 'internet-archive-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('internet-archive', 'archive', 'library', 'columns', 'logo', 'brand', 'wayback')

    def build(self):
        self.add_polyline('roof',(6,14),(24,6),(42,14))
        for x in (12,24,36):self.add_line(f'column{x}',(x,23),(x,33))
        self.add_line('base',(6,42),(42,42))
