"""The lowercase letter e, re-authored from the supplied reference for SOLO48.

Centerline extremes: left 6, top 6, right 42, bottom 42.
Plan: An open lower bowl and a semicircular upper bowl sharing a horizontal bar.
Reference: Lucide type — coherent monoline runs and explicit stroke junctions.
Source extraction fragments are omitted; the recognizable character is retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f38bbf0d-ebf5-5541-8ba3-dacda870ad9a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__letter-e/20260927T101636Z-thuan-mac-1/reference/letter-e_f38bbf0d-ebf5-5541-8ba3-dacda870ad9a.svg'
AUTHOR = 'gpt-6'


class LetterE(Solo48):
    icon_id = 'letter-e-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface"
    categories = ("typeface",)
    # Semantic body region for text composition; source geometry stays unchanged.
    typeface = {'character': 'e', 'kind': 'lowercase'}
    aliases = ()
    keywords = ('e', "typeface", "typography", 'lowercase')

    def build(self):
        # Open lowercase e with a continuous bowl and long readable crossbar.
        self.add_arc('upper',(6,24),(42,24),radius_x=18,radius_y=18,sweep=True)
        self.add_line('bar',(42,24),(6,24))
        self.add_arc('lower',(6,24),(24,42),radius_x=18,radius_y=18,sweep=False)
        self.add_arc('terminal',(24,42),(42,32),radius_x=18,radius_y=10,sweep=False)
        self.add_contour('e','upper','bar','lower','terminal',closed=False)
