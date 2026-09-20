"""Three binding calendar.

Construction reference: calendar.
Three binding posts; page symbols excluded.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '8c9afa4f-6b92-41b3-8bcd-f538c69afde6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/pg_app_cdn/all_icons/8c9afa4f-6b92-41b3-8bcd-f538c69afde6.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'three-binding-calendar-solo-8c9afa4f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('three-binding-calendar',)
    keywords = ('three', 'binding', 'calendar')

    def build(self):
        # Three posts are one centered series. Each is split at the page top.
        box(self,'page',6,14,42,42,4,nodes=((14,14),(24,14),(34,14)))
        for i,x in enumerate((14,24,34)):
            self.add_polyline(f'binding-{i}',(x,6),(x,14),(x,22))
            self.relate('connect','page',f'binding-{i}')
