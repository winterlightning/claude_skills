# Variant of floppy-disk; parent file remains unchanged.
'Solid hub dot. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48975063-b353-533e-ada8-826f1f506264'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_48975063-b353-533e-ada8-826f1f506264.svg'
AUTHOR = 'gpt-6'

class FloppyDiskVariant2(Solo48):
    icon_id = 'floppy-disk-v2'
    variant_of = 'floppy-disk'
    variant_label = 'Solid hub dot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'media', 'data')

    def build(self) -> None:
        self.add_line('disk-t', (6, 6), (42, 6))

        self.add_line('disk-r', (42, 6), (42, 42))

        self.add_line('disk-b', (42, 42), (6, 42))

        self.add_line('disk-l', (6, 42), (6, 6))

        self.add_contour('disk', 'disk-t',  'disk-r',  'disk-b',  'disk-l',  closed=True)
        self.add_polyline('shutter', (11, 6), (11, 14), (37, 14), (37, 6), closed=False)
        self.relate('connect', 'disk', 'shutter')
        self.add_polyline('label', (11, 42), (11, 38), (37, 38), (37, 42), closed=False)
        self.relate('connect', 'disk', 'label')
        self.add_dot('hub', (24, 26))
