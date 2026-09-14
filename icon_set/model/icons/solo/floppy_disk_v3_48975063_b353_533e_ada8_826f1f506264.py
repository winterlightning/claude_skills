# Variant of floppy-disk-v2; parent file remains unchanged.
"""Solid hub dot. Independent feedback revision; preserve source subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48975063-b353-533e-ada8-826f1f506264'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_48975063-b353-533e-ada8-826f1f506264.svg'
AUTHOR = 'gpt-6'

class FloppyDiskVariant3(Solo48):
    icon_id = 'floppy-disk-v3'
    variant_of = 'floppy-disk-v2'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'media', 'data')

    def build(self):
        # Lucide save: clipped outer corner, open shutter stroke and large lower label. Remove the nonessential hub dot to give the label room; no collapsed counters.
        self.add_polyline('disk', (6, 6), (36, 6), (42, 12), (42, 42), (6, 42), closed=True)
        self.add_polyline('shutter', (15, 6), (15, 15), (28, 15), closed=False)
        self.relate("connect", 'disk', 'shutter')
        self.add_polyline('label', (15, 42), (15, 29), (33, 29), (33, 42), closed=False)
        self.relate("connect", 'disk', 'label')
