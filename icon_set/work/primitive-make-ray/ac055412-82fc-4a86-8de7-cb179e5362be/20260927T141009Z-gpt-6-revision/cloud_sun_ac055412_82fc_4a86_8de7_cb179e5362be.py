"Cloud with Sun at Upper Right.\nSymbol plan: A broad rounded cloud partly covers a circular sun at its upper right. Short straight rays extend around the exposed portion of the sun above the cloud's flat base.\nConstruction: Lucide cloud-sun: occluded sun arc behind a continuous cloud.\nReduction: Separate the sun slightly above the cloud for clear ink spacing; omit fine rays.\nKeyshape SQUARE."
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ac055412-82fc-4a86-8de7-cb179e5362be'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cloud-with-sun-at-upper-right/20260927T140026Z-thuan-mac-1/reference/cloud sun_ac055412-82fc-4a86-8de7-cb179e5362be.svg'
AUTHOR = "gpt-6"

class BatchIcon(Solo48):
    icon_id = 'cloud-with-sun-at-upper-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('cloud', 'sun', 'weather', 'partly-cloudy', 'sky', 'rays', 'day')
    def build(self):
        # The round sun sits at upper right; the broad three-lobed cloud remains dominant.
        self.add_arc('sun-upper',(32,11),(42,11),radius_x=5)
        self.add_arc('sun-lower',(42,11),(32,11),radius_x=5)
        self.add_contour('sun','sun-upper','sun-lower',closed=True)
        self.add_bezier('cloud-left',(14,42),((9,42),(6,38),(6,33)))
        self.add_bezier('cloud-shoulder',(6,33),((6,26),(11,22),(17,24)))
        self.add_bezier('cloud-dome',(17,24),((19,16),(27,17),(30,25)))
        self.add_bezier('cloud-right',(30,25),((38,22),(42,27),(42,34)))
        self.add_bezier('cloud-lower',(42,34),((42,39),(38,42),(34,42)))
        self.add_line('cloud-base',(34,42),(14,42))
        self.add_contour('cloud','cloud-left','cloud-shoulder','cloud-dome','cloud-right','cloud-lower','cloud-base',closed=True)
