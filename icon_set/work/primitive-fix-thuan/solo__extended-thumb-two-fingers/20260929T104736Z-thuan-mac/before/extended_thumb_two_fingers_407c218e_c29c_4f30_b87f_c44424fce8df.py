'I-love-you gesture: thumb, index and little finger extended with folded middle fingers. Meaning-specific hand anatomy retained for visual checking.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. Lucide hand original and atoms inform semicircular finger ends. The two folded fingers share one simplified valley; palm crease omitted for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '407c218e-c29c-4f30-b87f-c44424fce8df'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pinkie_407c218e-c29c-4f30-b87f-c44424fce8df.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'extended-thumb-two-fingers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ["I love you hand sign"]
    keywords = ["hand", "gesture", "thumb", "index", "little finger"]
    def build(self):

        self.add_bezier('thumb-outer',(16,40),((16,36),(4,32),(4,24)))
        self.add_bezier('thumb-tip',(4,24),((4,19),(7,17),(10,20)))
        self.add_line('thumb-inner',(10,20),(14,24))
        self.add_line('index-left',(14,24),(14,12))
        self.add_arc('index-tip',(14,12),(22,12),radius_x=4,sweep=True)
        self.add_line('index-right',(22,12),(22,24))
        self.add_bezier('folded',(22,24),((22,29),(36,29),(36,24)))
        self.add_line('pinky-left',(36,24),(36,16))
        self.add_arc('pinky-tip',(36,16),(44,16),radius_x=4,sweep=True)
        self.add_line('pinky-right',(44,16),(44,28))
        self.add_bezier('palm-right',(44,28),((44,34),(40,37),(38,40)))
        self.add_contour('hand','thumb-outer','thumb-tip','thumb-inner','index-left','index-tip','index-right','folded','pinky-left','pinky-tip','pinky-right','palm-right')
