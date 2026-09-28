"""Bank Building. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide landmark: a separate pediment and regularly spaced columns; the supplied source determines the three-column count.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71fea618-8aac-45ba-aab5-f6dc58ab93f0'
SOURCE_PATH = 'pictographic-primitives/symbol/bank_71fea618-8aac-45ba-aab5-f6dc58ab93f0.svg'
AUTHOR = 'gpt-6'


class BankColumns(Solo48):
    icon_id = 'bank-columns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('bank', 'building', 'finance', 'columns', 'institution', 'museum', 'court', 'government')

    def build(self) -> None:
        self.add_polyline('pediment', (6, 20), (24, 6), (42, 20), closed=True)
        self.add_polyline('base', (6, 42), (12, 42), (24, 42), (36, 42), (42, 42))
        self.add_line('column-0', (12, 28), (12, 42))
        self.relate("connect", 'base', 'column-0')
        self.add_line('column-1', (24, 28), (24, 42))
        self.relate("connect", 'base', 'column-1')
        self.add_line('column-2', (36, 28), (36, 42))
        self.relate("connect", 'base', 'column-2')
