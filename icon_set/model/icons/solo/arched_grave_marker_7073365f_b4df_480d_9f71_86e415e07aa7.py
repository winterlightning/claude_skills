"""Arched Grave Marker.

Plan: Round-topped memorial slab on wide plinth; reduce side wings into broad base and narrow inset into one vertical mark. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7073365f-b4df-480d-9f71-86e415e07aa7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/qingming festival_7073365f-b4df-480d-9f71-86e415e07aa7.svg'
AUTHOR = 'gpt-6'

class ArchedGraveMarker(Solo48):
    icon_id = 'arched-grave-marker'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('arched', 'grave', 'marker')

    def build(self):
        self.add_polyline('left',(8,44),(8,36),(14,36),(14,14))
        self.add_arc('arch',(14,14),(34,14),radius_x=10)
        self.add_polyline('right',(34,14),(34,36),(40,36),(40,44),(8,44))
        self.add_contour('marker','left-1','left-2','left-3','arch',*[f'right-{i}' for i in range(1,5)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['left','right']]
        self.add_line('base',(14,36),(34,36));self.relate('connect','marker','base')
        self.add_line('inset',(24,20),(24,28))
