'Eye: mirrored almond lids with exact horizontal keyshape bounds around a genuinely round iris.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6627b62c-9a54-43be-8f20-fccd8ae111e8'
SOURCE_PATH = 'pictographic-primitives/symbol/focus with eye_6627b62c-9a54-43be-8f20-fccd8ae111e8.svg'
AUTHOR = 'gpt-6'


class EyeOutlineFocus(Solo48):
    icon_id = 'eye-outline-focus'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('eye', 'view', 'see', 'visibility', 'watch', 'look', 'vision', 'focus')

    def build(self) -> None:
        # Paired coherent eyelids reach all four HRECT_L extrema without stretching the iris.
        self.add_bezier('upper',(4,24),((10,14),(16,8),(24,8)),((32,8),(38,14),(44,24)))
        self.add_bezier('lower',(44,24),((38,34),(32,40),(24,40)),((16,40),(10,34),(4,24)))
        self.add_contour('lids','upper','lower',closed=True)

        self.add_arc('iris-top', (18,24), (30,24), radius_x=6, radius_y=6)
        self.add_arc('iris-bottom', (30,24), (18,24), radius_x=6, radius_y=6)
        self.add_contour('iris', 'iris-top', 'iris-bottom', closed=True)
