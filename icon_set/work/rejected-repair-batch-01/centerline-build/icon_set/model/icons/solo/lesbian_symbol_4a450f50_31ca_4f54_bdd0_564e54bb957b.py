"""Two interlocking Venus symbols with opposing crossed stems. Lucide venus informs the crossed stems. The upper stem intentionally follows the reference diagonal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a450f50-31ca-4f54-bdd0-564e54bb957b'
SOURCE_PATH = 'pictographic-primitives/users/gender lesbian_4a450f50-31ca-4f54-bdd0-564e54bb957b.svg'
AUTHOR = 'gpt-6'


class LesbianSymbol(Solo48):
    icon_id = 'lesbian-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
    aliases = ()
    keywords = ('lesbian', 'gender', 'female', 'venus', 'symbol', 'couple', 'pride', 'women')

    def build(self) -> None:
        # Square extremes (6,6)-(42,42); r10 rings centered (16,21),(28,21).
        self.add_arc('outer-left-top',(22,13),(16,31),radius_x=10,large_arc=True,sweep=False)
        self.add_arc('outer-left-bottom',(16,31),(22,29),radius_x=10,sweep=False)
        self.add_arc('outer-right-bottom',(22,29),(34,13),radius_x=10,large_arc=True,sweep=False)
        self.add_arc('outer-right-top',(34,13),(22,13),radius_x=10,sweep=False)
        self.add_contour('linked-outline','outer-left-top','outer-left-bottom','outer-right-bottom','outer-right-top',closed=True)
        self.add_arc('lens-right',(22,13),(22,29),radius_x=10)
        self.add_arc('lens-left',(22,29),(22,13),radius_x=10)
        self.relate('connect','linked-outline','lens-right')
        self.relate('connect','linked-outline','lens-left')
        self.relate('connect','lens-right','lens-left')
        self.add_polyline('female-stem',(16,31),(16,40),(16,42))
        self.add_polyline('crossbar',(10,40),(16,40),(22,40))
        self.add_polyline('diagonal-stem',(34,13),(38,9),(41,6))
        self.add_polyline('diagonal-crossbar',(35,6),(38,9),(42,13))
        self.relate('connect','linked-outline','female-stem')
        self.relate('connect','female-stem','crossbar')
        self.relate('connect','linked-outline','diagonal-stem')
        self.relate('connect','diagonal-stem','diagonal-crossbar')
