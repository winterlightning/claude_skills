'batch-01-monitor: independent smooth-curve repair.\n\nConstruction: Rounded monitor with central stand; shared stem and bottom edge junction.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/monitor.svg and atomic-debug/monitor.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '181755f1-a8ab-4d25-8475-ebcf6885f0c8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.svg'
AUTHOR = 'gpt-6'


class Batch01MonitorVariant2(Solo48):
    icon_id = 'batch-01-monitor-v2'
    variant_of = 'batch-01-monitor'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'monitor', 'computers')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'screen',4,8,44,30,4,xs=(24,))
        line(self,'stand',(24,30),(24,40))
        line(self,'foot',(16,40),(32,40))
        contacts(self)
