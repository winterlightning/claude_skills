'Musical Tambourine Percussion Instrument.\n\nSymbol plan: Tambourine face with five short exterior jingle marks. A regular circular rim remains dominant.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91da39d2-af7e-4d33-886a-5cb86291b205'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tambour_91da39d2-af7e-4d33-886a-5cb86291b205.svg'
AUTHOR = 'gpt-6'

class FiveJingleTambourine(Solo48):
    icon_id = 'five-jingle-tambourine'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('five', 'jingle', 'tambourine')

    def build(self):
        # Tambourine face with five short exterior jingle marks. A regular circular rim remains dominant.
        axis_x = 24
        p_4_24 = (4, 24)
        p_8_24 = (8, 24)
        p_11_38 = (11, 38)
        p_13_36 = (13, 36)
        p_24_4 = (24, 4)
        p_24_8 = (24, 8)
        p_35_36 = (2 * axis_x - p_13_36[0], p_13_36[1])
        p_37_38 = (2 * axis_x - p_11_38[0], p_11_38[1])
        p_40_24 = (2 * axis_x - p_8_24[0], p_8_24[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('rim-1', p_8_24, p_40_24, radius_x=16, radius_y=16, sweep=True)
        self.add_arc('rim-2', p_40_24, p_8_24, radius_x=16, radius_y=16, sweep=True)
        self.add_contour('rim', 'rim-1', 'rim-2', closed=True)
        self.add_line('top-1', p_24_8, p_24_4)
        self.add_contour('top', 'top-1', closed=False)
        self.relate("connect", 'rim', 'top')
        self.add_line('left-1', p_8_24, p_4_24)
        self.add_contour('left', 'left-1', closed=False)
        self.relate("connect", 'rim', 'left')
        self.add_line('right-1', p_40_24, p_44_24)
        self.add_contour('right', 'right-1', closed=False)
        self.relate("connect", 'rim', 'right')
        self.add_line('lower-left-1', p_13_36, p_11_38)
        self.add_contour('lower-left', 'lower-left-1', closed=False)
        self.relate("connect", 'rim', 'lower-left')
        self.add_line('lower-right-1', p_35_36, p_37_38)
        self.add_contour('lower-right', 'lower-right-1', closed=False)
        self.relate("connect", 'rim', 'lower-right')
