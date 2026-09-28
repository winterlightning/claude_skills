"""An ear surrounds a round physical hearing aid beside two sound-wave arcs. HRECT_L 4..44 x8..40 accommodates sound waves. Source supplies aid and outer ear; Lucide ear supplies flowing helix-to-lobe contour. Existing failed draft revised. Aid simplified to round earpiece; omit inner helix/fitting that crowds the device. Two separate wave curves keep outward rhythm."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'e1893637-f6ac-4602-b63a-d7fd5a641510'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/disability hearing aid t_e1893637-f6ac-4602-b63a-d7fd5a641510.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'ear-with-round-hearing-device-and-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Ear with Round Hearing Device and Waves']
    keywords = ['ear', 'hearing', 'device', 'aid', 'sound', 'waves', 'accessibility']
    def build(self):
        self.add_bezier('ear',(4,12),((7,8),(10,8),(16,8)),((22,8),(24,12),(24,18)),((24,26),(20,27),(18,33)),((16,39),(13,40),(10,40)),((6,40),(4,38),(4,36)))
        self.add_arc('aid-top',(4,24),(12,24),radius_x=4)
        self.add_arc('aid-bottom',(12,24),(4,24),radius_x=4)
        self.add_contour('aid','aid-top','aid-bottom',closed=True)
        self.add_bezier('wave-inner',(34,19),((36,22),(36,26),(34,29)))
        self.add_bezier('wave-outer',(41,10),((43,14),(44,20),(44,24)),((44,28),(43,34),(41,38)))
