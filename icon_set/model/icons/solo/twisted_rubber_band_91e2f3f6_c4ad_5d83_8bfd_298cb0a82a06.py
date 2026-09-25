"""A twisted rubber band with two smooth lobes; duplicate strands and short dashes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91e2f3f6-c4ad-5d83-8bfd-298cb0a82a06'
SOURCE_PATH = 'pictographic-primitives/tools/elastic band_91e2f3f6-c4ad-5d83-8bfd-298cb0a82a06.svg'
AUTHOR = 'gpt-6'

class TwistedRubberBand(Solo48):
    icon_id = 'twisted-rubber-band'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('elastic band', 'rubber band', 'elastic', 'stretch', 'loop', 'band', 'office', 'flexible')

    def build(self) -> None:
        self.add_arc('upper',(24,24),(6,15),radius_x=12)
        self.add_arc('upper-cap',(6,15),(15,6),radius_x=9)
        self.add_arc('upper-return',(15,6),(24,24),radius_x=12)
        self.add_arc('lower',(24,24),(42,33),radius_x=12)
        self.add_arc('lower-cap',(42,33),(33,42),radius_x=9)
        self.add_arc('lower-return',(33,42),(24,24),radius_x=12)
        self.add_contour('band','upper','upper-cap','upper-return','lower','lower-cap','lower-return',closed=True)
