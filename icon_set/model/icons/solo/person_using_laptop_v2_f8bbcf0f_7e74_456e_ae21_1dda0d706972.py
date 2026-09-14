"""Front view replaces the cramped side view: a round head, broad shoulders and a clear laptop screen. No face or keyboard details.
Lucide hand, crown and user/laptop construction; independently revised on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8bbcf0f-7e74-456e-ae21-1dda0d706972'
SOURCE_PATH = 'pictographic-primitives/work/working remotely_f8bbcf0f-7e74-456e-ae21-1dda0d706972.svg'
AUTHOR = 'gpt-6'

class PersonUsingLaptopVariant2(Solo48):
    icon_id = 'person-using-laptop-v2'
    variant_of = 'person-using-laptop'
    variant_label = 'Cleaner silhouette and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('person', 'laptop', 'computer', 'remote', 'work', 'seated')

    def build(self) -> None:
        self.add_arc('head-top', (19, 11), (29, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (29, 11), (19, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder-left', (14, 22), (6, 30), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_polyline('body', (6, 30), (6, 42), (42, 42), (42, 30), closed=False)
        self.add_arc('shoulder-right', (42, 30), (34, 22), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.relate("connect", 'shoulder-left', 'body')
        self.relate("connect", 'shoulder-right', 'body')
        self.add_polyline('screen', (15, 42), (15, 30), (33, 30), (33, 42), closed=False)
        self.relate("connect", 'screen', 'body')
