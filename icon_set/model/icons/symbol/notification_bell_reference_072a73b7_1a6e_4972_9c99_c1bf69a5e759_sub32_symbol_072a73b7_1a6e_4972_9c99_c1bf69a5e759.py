"""Independent 32px profile of notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '072a73b7-1a6e-4972-9c99-c1bf69a5e759'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell_072a73b7-1a6e-4972-9c99-c1bf69a5e759.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('072a73b7-1a6e-4972-9c99-c1bf69a5e759', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell_072a73b7-1a6e-4972-9c99-c1bf69a5e759.svg'), ('85384c6e-0df4-408f-bf41-58882794cc0a', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm bell_85384c6e-0df4-408f-bf41-58882794cc0a.svg'))
PROFILE_SOURCE_KEYS = ('solo/notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759', 'solo/notification-bell-reference-85384c6e-0df4-408f-bf41-58882794cc0a')
SOLO_SOURCE_ICON_IDS = ('notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759', 'notification-bell-reference-85384c6e-0df4-408f-bf41-58882794cc0a')
REFERENCE_EXPORT_SHA256 = '0ef6b411da6b7386ef6749579636e81996fb3979e24ac16b1ff798c94f810608'

class DrawingContainerSymbol(Sub32):
    icon_id = 'notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759-sub32-symbol'
    related_origin_icon_id = 'notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759-sub32'
    counterpart_icon_id = 'notification-bell-reference-072a73b7-1a6e-4972-9c99-c1bf69a5e759-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((12, 4), (8, 4), (8, 10)))
        self.add_bezier('p1-r1-2', (8, 10), ((8, 15), (6, 18), (5, 20)))
        self.add_line('p1-r1-3', (5, 20), (27, 20))
        self.add_bezier('p1-r1-4', (27, 20), ((26, 18), (24, 15), (24, 10)))
        self.add_bezier('p1-r1-5', (24, 10), ((24, 4), (20, 4), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (12, 26), (20, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
