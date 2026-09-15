"""A storage box with an overhanging lid.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide archive: separate rounded lid and attached U-shaped body.
All identity features retained.
Hosting (compose.py): plus does not fit, heart does not fit, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class StorageBoxWithLid(Container64):
    icon_id = 'storage-box-with-lid'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('storage', 'box', 'with', 'lid')

    def build(self) -> None:
        self.add_line('lid-0', (5, 2), (59, 2))
        self.add_arc('lid-1', (59, 2), (62, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('lid-2', (62, 5), (62, 11))
        self.add_arc('lid-3', (62, 11), (59, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_line('lid-4', (59, 14), (5, 14))
        self.add_arc('lid-5', (5, 14), (2, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_line('lid-6', (2, 11), (2, 5))
        self.add_arc('lid-7', (2, 5), (5, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('lid', 'lid-0', 'lid-1', 'lid-2', 'lid-3', 'lid-4', 'lid-5', 'lid-6', 'lid-7', closed=True)
        self.add_line('body-0', (6, 14), (6, 52))
        self.add_arc('body-1', (6, 52), (16, 62), radius_x=10, radius_y=10, sweep=False)
        self.add_line('body-2', (16, 62), (48, 62))
        self.add_arc('body-3', (48, 62), (58, 52), radius_x=10, radius_y=10, sweep=False)
        self.add_line('body-4', (58, 52), (58, 14))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', closed=False)
        self.relate("connect", 'body', 'lid')
