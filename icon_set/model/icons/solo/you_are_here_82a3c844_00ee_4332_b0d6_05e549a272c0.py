'You are here: compact rounded pin and circular location centre, raised above its separate ground rule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a3c844-00ee-4332-b0d6-05e549a272c0'
SOURCE_PATH = 'pictographic-primitives/maps/you are here_82a3c844-00ee-4332-b0d6-05e549a272c0.svg'
AUTHOR = 'gpt-6'

class YouAreHere(Solo48):
    icon_id = 'you-are-here'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    categories = ('maps', 'primitives')
    aliases = ()
    keywords = ('you', 'are', 'here', 'maps')

    def build(self) -> None:
        self.add_arc('dome',(8,20),(40,20),radius_x=16)
        self.add_bezier('right',(40,20),((40,26),(30,32),(24,35)))
        self.add_bezier('left',(24,35),((18,32),(8,26),(8,20)))
        self.add_contour('pin','dome','right','left',closed=True)
        self.add_line('ground',(8,44),(40,44))

        self.add_arc('centre-top', (20,18), (28,18), radius_x=4, radius_y=4)
        self.add_arc('centre-bottom', (28,18), (20,18), radius_x=4, radius_y=4)
        self.add_contour('centre', 'centre-top', 'centre-bottom', closed=True)
