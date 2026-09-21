"""Es Letters Underlined. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '901bbfbd-f392-4578-9592-ae246d76df6f'
SOURCE_PATH = 'pictographic-primitives/symbol/es (text u)_901bbfbd-f392-4578-9592-ae246d76df6f.svg'
AUTHOR = 'gpt-6'


class EsLettersUnderlined(Solo48):
    icon_id = 'es-letters-underlined'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('es', 'letters', 'spanish', 'text', 'underline', 'language', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_polyline('e', (18, 8), (4, 8), (4, 19), (4, 30), (18, 30))
        self.add_line('e-middle', (4, 19), (16, 19))
        self.relate("connect", 'e', 'e-middle')
        self.add_line('s-top', (44, 14), (37, 14))
        self.add_arc('s-upper', (37, 14), (37, 22), radius_x=7, radius_y=4, sweep=False)
        self.add_arc('s-lower', (37, 22), (37, 30), radius_x=7, radius_y=4, sweep=True)
        self.add_line('s-foot', (37, 30), (30, 30))
        self.add_contour('s', 's-top', 's-upper', 's-lower', 's-foot')
        self.add_line('underline', (4, 40), (44, 40))
