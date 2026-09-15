'peacock-with-spread-tail: independent smooth-curve repair.\n\nConstruction: Peacock beneath a flowing tail arch; circular head and tapered smooth body replace fragmentary center.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/feather.svg and atomic-debug/feather.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9e421611-5f19-400d-8a51-23357e8cb95c'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feathers up_9e421611-5f19-400d-8a51-23357e8cb95c.svg'
AUTHOR = 'gpt-6'


class PeacockWithSpreadTail(Solo48):
    icon_id = 'peacock-with-spread-tail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('peacock', 'with', 'spread', 'tail')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'tail',(4,40),('C',(7,18),(14,8),(24,8)),('C',(34,8),(41,18),(44,40)))
        path(self,'bird',(24,18),('C',(19,18),(19,23),(19,27)),('C',(19,30),(17,32),(17,35)),('C',(17,41.666666667),(31,41.666666667),(31,35)),('C',(31,32),(29,30),(29,27)),('C',(29,23),(29,18),(24,18)),closed=True)
        contacts(self)
