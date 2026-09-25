"""An indent triangle beside four clean, consistently aligned text rules. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1a54286-e9bb-5b0c-b184-d01536f22cfa'
SOURCE_PATH = 'pictographic-primitives/interface-essential/increase indent_f1a54286-e9bb-5b0c-b184-d01536f22cfa.svg'
AUTHOR = 'gpt-6'

class IncreaseIndent(Solo48):
    icon_id = 'increase-indent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('increase', 'indent', 'interface-essential')

    def build(self) -> None:
        # One triangular indent marker and four mirrored text rows with balanced integer spacing.
        # Lucide list-indent-increase informs the clean marker and repeated rules.
        # HRECT_L centerline extremes: (4, 8)-(44, 40).
        self.add_polyline('indent-marker', (4, 14), (16, 24), (4, 34), closed=True)
        for index, y in enumerate((8, 19, 29, 40)):
            self.add_line(f'text-line-{index}', (25, y), (44, y))
