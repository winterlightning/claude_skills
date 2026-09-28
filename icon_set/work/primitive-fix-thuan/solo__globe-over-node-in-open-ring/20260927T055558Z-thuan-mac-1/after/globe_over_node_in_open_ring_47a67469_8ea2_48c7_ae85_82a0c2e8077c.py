"""Globe over node within open circular network ring. Radial envelope admits a legible continent division and detached node; continent simplified to one smooth S-shaped division."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '47a67469-8ea2-48c7-ae85-82a0c2e8077c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__globe-over-node-in-open-ring/20260927T055558Z-thuan-mac-1/reference/amazon web service cross region data delivery 1_47a67469-8ea2-48c7-ae85-82a0c2e8077c.svg'
AUTHOR = 'gpt-6'

class GlobeOverNodeInOpenRing(Solo48):
    icon_id = 'globe-over-node-in-open-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology', 'networks')
    aliases = ()
    keywords = ('globe', 'world', 'region', 'network', 'cloud', 'delivery', 'node', 'data')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('ring-a', (12, 38), (6, 22), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('ring-b', (6, 22), (24, 4), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('ring-c', (24, 4), (42, 22), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('ring-d', (42, 22), (36, 38), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('globea', (24, 13), (24, 27), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('globeb', (24, 27), (24, 13), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('land-a', (24, 13), (24, 20), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('land-b', (24, 20), (24, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('nodea', (20, 40), (28, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('nodeb', (28, 40), (20, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('ring', *('ring-a', 'ring-b', 'ring-c', 'ring-d'), closed=False)
        self.add_contour('globe', *('globea', 'globeb'), closed=True)
        self.add_contour('land', *('land-a', 'land-b'), closed=False)
        self.add_contour('node', *('nodea', 'nodeb'), closed=True)
        self.relate('connect', *('land', 'globe'))
