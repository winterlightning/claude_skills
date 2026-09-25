"""A continuous outline of head, neck and shoulders, open below. VRECT_L extremes (8,4)-(40,44). Lucide user-round informs the arched head and paired shoulders; preserve the source continuous neck connection. Remove tiny temple bumps and use coherent mirrored cheek and shoulder arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bbf46af-b1e3-4c99-a128-75a6fbed4550'
SOURCE_PATH = 'pictographic-primitives/symbol/person 1_1bbf46af-b1e3-4c99-a128-75a6fbed4550.svg'
AUTHOR = 'gpt-6'


class PersonSilhouetteOutline(Solo48):
    icon_id = 'person-silhouette-outline'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('person', 'user', 'silhouette', 'profile', 'avatar', 'anonymous', 'account', 'member')

    def build(self) -> None:
        self.add_line('left-base',(8,44),(8,38))
        self.add_arc('left-shoulder',(8,38),(12,34),radius_x=4)
        self.add_arc('left-neck',(12,34),(16,30),radius_x=4,sweep=False)
        self.add_line('left-neck-up',(16,30),(16,28))
        self.add_arc('left-cheek',(16,28),(12,20),radius_x=10)
        self.add_line('left-temple',(12,20),(12,16))
        self.add_arc('head',(12,16),(36,16),radius_x=12)
        self.add_line('right-temple',(36,16),(36,20))
        self.add_arc('right-cheek',(36,20),(32,28),radius_x=10)
        self.add_line('right-neck-down',(32,28),(32,30))
        self.add_arc('right-neck',(32,30),(36,34),radius_x=4,sweep=False)
        self.add_arc('right-shoulder',(36,34),(40,38),radius_x=4)
        self.add_line('right-base',(40,38),(40,44))
        self.add_contour('silhouette','left-base','left-shoulder','left-neck','left-neck-up','left-cheek','left-temple','head','right-temple','right-cheek','right-neck-down','right-neck','right-shoulder','right-base')
