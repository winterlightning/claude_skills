"""Ribbon Shape Bookmark Tag: independently authored container.

Construction plan: Single rounded-top vertical ribbon with centered V notch; mirrored corners.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/bookmark_1c26a9c6-fac8-4352-bc90-e409954efaf5.svg. Lucide bookmark original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '1c26a9c6-fac8-4352-bc90-e409954efaf5'
SOURCE_PATH = 'pictographic-primitives/interface-essential/bookmark_1c26a9c6-fac8-4352-bc90-e409954efaf5.svg'
AUTHOR = 'gpt-6'


class RibbonBookmarkContainer(Container64):
    icon_id = 'ribbon-bookmark-container'
    category = 'interface-essential'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('ribbon', 'bookmark', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'ribbon',(10,62),[('L',(10,6)),('A',(14,2),4,4,True),('L',(50,2)),('A',(54,6),4,4,True),('L',(54,62)),('L',(32,46)),('L',(10,62))],True)
