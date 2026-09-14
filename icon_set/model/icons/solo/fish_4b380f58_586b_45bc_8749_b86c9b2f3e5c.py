"""Pointed fish lens with open crossing tail; Lucide fish-symbol informs the two sweeping strokes. Omit the eye."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b380f58-586b-45bc-8749-b86c9b2f3e5c'
SOURCE_PATH = 'pictographic-primitives/animals/fish_4b380f58-586b-45bc-8749-b86c9b2f3e5c.svg'
AUTHOR = 'gpt-6'


class IchthysFish(Solo48):
    icon_id = 'ichthys-fish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('ichthys', 'fish')

    def build(self) -> None:
        # Visible keyshape bounds: (2, 6, 46, 42); centerlines inset by 2.
        self.add_arc('upper-left', (12, 24), (28, 8), radius_x=20, radius_y=40, sweep=True)
        self.add_arc('upper-right', (28, 8), (44, 24), radius_x=20, radius_y=40, sweep=True)
        self.add_arc('lower-right', (44, 24), (28, 40), radius_x=20, radius_y=40, sweep=True)
        self.add_arc('lower-left', (28, 40), (12, 24), radius_x=20, radius_y=40, sweep=True)
        self.add_contour('body', 'upper-left', 'upper-right', 'lower-right', 'lower-left')
        self.add_line('tail-upper', (12, 24), (4, 14))
        self.add_line('tail-lower', (12, 24), (4, 34))
        self.relate("connect", 'body', 'tail-upper')
        self.relate("connect", 'body', 'tail-lower')
        self.relate("connect", 'tail-upper', 'tail-lower')
