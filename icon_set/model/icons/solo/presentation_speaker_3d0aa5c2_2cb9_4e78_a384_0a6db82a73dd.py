'Presentation speaker: round detached head and smooth shoulders in front of a broad screen; remove the cramped podium crossbar.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d0aa5c2-2cb9-4e78-a384-0a6db82a73dd'
SOURCE_PATH = 'pictographic-primitives/office/presentation speaker_3d0aa5c2-2cb9-4e78-a384-0a6db82a73dd.svg'
AUTHOR = 'gpt-6'

class PresentationSpeaker(Solo48):
    icon_id = 'presentation-speaker'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('presentation', 'speaker', 'office')

    def build(self) -> None:
        self.add_arc('head-top', (21,20), (27,20), radius_x=3, radius_y=3)
        self.add_arc('head-bottom', (27,20), (21,20), radius_x=3, radius_y=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)

        # Shared human reference: head bottom22, body top30; exact4-unit ink gap.
        self.add_bezier('shoulders',(16,40),((16,33),(19,31),(24,31)),((29,31),(32,33),(32,40)))
        self.add_polyline('screen',(10,30),(4,30),(4,8),(44,8),(44,30),(38,30))
