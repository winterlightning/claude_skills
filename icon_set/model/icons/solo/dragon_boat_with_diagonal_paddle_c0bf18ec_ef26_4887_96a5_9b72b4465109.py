"""Dragon-headed boat and working paddle, a natural vessel/tool group. Wide HRECT_L x4..44 y8..40. Source provides neck and upturned stern. Lucide sailboat teaches rounded hull; no scales or eye. Paddle is visibly interrupted behind hull."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'c0bf18ec-ef26-4887-96a5-9b72b4465109'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/dragon boat_c0bf18ec-ef26-4887-96a5-9b72b4465109.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'dragon-boat-with-diagonal-paddle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ['Dragon Boat with Diagonal Paddle']
    keywords = ['dragon', 'boat', 'paddle', 'hull', 'watercraft', 'rowing', 'vessel']
    def build(self):
        self.add_bezier('boat',(4,16),((4,16),(12,16),(12,20)),((12,23),(4,25),(4,30)),((4,34),(8,36),(14,36)))
        self.add_line('bottom',(14,36),(34,36))
        self.add_bezier('stern',(34,36),((42,36),(44,31),(44,24)),((40,28),(36,26),(28,26)))
        self.add_line('deck',(28,26),(24,26))
        self.add_bezier('neck',(24,26),((20,26),(24,22),(24,18)),((24,12),(22,8),(16,8)))
        self.add_line('nose-top',(16,8),(4,8))
        self.add_line('nose',(4,8),(4,16))
        self.add_contour('hull','boat','bottom','stern','deck','neck','nose-top','nose',closed=True)
        self.add_line('paddle-shaft',(36,8),(33,17))
        self.add_line('paddle-blade',(26,40),(28,34))
        self.relate('occlude','hull','paddle-blade')
