"""Capital S and E. Lucide type and strikethrough inform monoline terminals and coherent curves. E middle arm shortened as in the source.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65ff17d5-d6f4-45f8-9685-b215f34e7ba1'
SOURCE_PATH = 'pictographic-primitives/symbol/se (text)_65ff17d5-d6f4-45f8-9685-b215f34e7ba1.svg'
AUTHOR = 'gpt-6'


class SeText(Solo48):
    icon_id = 'se-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('se', 'letters', 'text', 'abbreviation', 'typography', 'label', 'language')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('s-crown',(18, 16),*(((16.73437775, 13.59300259), (14.45714319, 12.12063003), (11.5, 12.12063003)), ((8.42857101, 12.12063003), (5.58202781, 13.59300259), (4, 16))))
        self.add_bezier('s-upper-turn',(4, 16),*(((4, 19.66053238), (6.40886678, 22.95638042), (10, 24)),))
        self.add_bezier('s-lower-turn',(10, 24),*(((14.86599325, 24.0), (18.0, 27.581722), (18, 32)),))
        self.add_bezier('s-base',(18, 32),*(((16.73437775, 34.40699741), (14.45714319, 35.87936997), (11.5, 35.87936997)), ((8.42857101, 35.87936997), (5.58202781, 34.40699741), (4, 32))))
        self.add_line('e-outline-1',(44, 8),(28, 8))
        self.add_line('e-outline-2',(28, 8),(28, 24))
        self.add_line('e-outline-3',(28, 24),(28, 40))
        self.add_line('e-outline-4',(28, 40),(44, 40))
        self.add_line('e-middle',(28, 24),(42, 24))
        self.add_contour('s',*('s-crown', 's-upper-turn', 's-lower-turn', 's-base'),closed=False)
        self.add_contour('e-outline',*('e-outline-1', 'e-outline-2', 'e-outline-3', 'e-outline-4'),closed=False)
        self.relate('connect',*('e-outline', 'e-middle'))
