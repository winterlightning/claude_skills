"""Plant Seedling Sprouting from Soil.
Plan: Two pointed leaves above a stem ending in two wavy soil tiers. Extrema (6,6)-(42,42).
Reference: Lucide sprout: broad paired leaves and a stem terminating at ground.
Reduction: Leaf veins and extra short soil strokes removed; two layered waves retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb521147-8fd9-4f84-aba9-c47244085768'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/grow crops_cb521147-8fd9-4f84-aba9-c47244085768.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'seedling-wavy-soil'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('plant', 'seedling', 'sprouting', 'from', 'soil')

    def build(self):

        self.add_bezier('left-a',(8,6),((20,6),(24,10),(24,22)))
        self.add_bezier('left-b',(24,22),((12,22),(8,18),(8,6)))
        self.add_contour('left','left-a','left-b',closed=True)

        self.add_bezier('right-a',(40,6),((28,6),(24,10),(24,22)))
        self.add_bezier('right-b',(24,22),((36,22),(40,18),(40,6)))
        self.add_contour('right','right-a','right-b',closed=True)

        self.relate('connect','left','right')
        self.add_line('stem',(24,22),(24,32))
        for n in ('left','right'):self.relate('connect',n,'stem')
        self.add_bezier('soil-top',(6,32),((8,32),(8,30),(12,30)),((18,30),(18,32),(24,32)),((30,32),(30,30),(36,30)),((40,30),(40,32),(42,32)))
        self.add_bezier('soil-low',(6,42),((8,42),(8,40),(12,40)),((18,40),(18,42),(24,42)),((30,42),(30,40),(36,40)),((40,40),(40,42),(42,42)))
        self.relate('connect','stem','soil-top')
