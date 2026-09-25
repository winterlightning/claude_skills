"""A standalone minus sign. CIRCLE uses its horizontal diameter, centerline endpoints (4,24)-(44,24), ink radius22. Lucide minus informs the single centered round-ended stroke; retain the source without additional decoration."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7450985-5938-4c75-b40d-352e69b5080d'
SOURCE_PATH = 'pictographic-primitives/symbol/minus_b7450985-5938-4c75-b40d-352e69b5080d.svg'
AUTHOR = 'gpt-6'


class MinusSolo(Solo48):
    icon_id = 'minus-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('minus', 'subtract', 'remove', 'dash', 'less', 'negative', 'collapse', 'line')

    def build(self) -> None:
        self.add_line('minus',(4,24),(44,24))
