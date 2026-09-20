"""Two binding calendar.

Construction reference: calendar.
Empty lower date area; label/check excluded.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'fc5ffdff-80e9-4119-bf62-fb7c515c5aad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'two-binding-calendar-solo-fc5ffdff'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('two-binding-calendar',)
    keywords = ('two', 'binding', 'calendar')

    def build(self):
        # Matching posts and an 8-unit clear header below their ends.
        box(self,'page',8,12,40,44,4,nodes=((16,12),(32,12),(8,28),(40,28)))
        for i,x in enumerate((16,32)):
            self.add_polyline(f'post-{i}',(x,4),(x,12),(x,20))
            self.relate('connect','page',f'post-{i}')
        self.add_line('header',(8,28),(40,28))
        self.relate('connect','page','header')
