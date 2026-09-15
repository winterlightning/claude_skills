'batch-01-monitor-computers: distinct review variant.\n\nConstruction: Monitor on two splayed feet; keep the rounded screen and a shared central attachment.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: monitor from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/monitor_78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb.svg'
AUTHOR = 'gpt-6'


class Batch01MonitorComputersVariant2(Solo48):
    icon_id = 'batch-01-monitor-computers-v2'
    variant_of = 'batch-01-monitor-computers'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'monitor', 'computers')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'screen',4,8,44,28,4,xs=(24,))
        poly(self,'feet',(16,40),(24,28),(32,40))
        contacts(self)
