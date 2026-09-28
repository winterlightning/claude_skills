# Review candidate; original preserved.
"""Five pointed oval leaves on a branching stem, with a shared lower-left branch and rounded pot. Lucide sprout informs the leaf arcs; asymmetrical lower-left cluster follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '53cfd912-2296-5a4a-a135-4701ab649e23'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_53cfd912-2296-5a4a-a135-4701ab649e23.svg'
AUTHOR = 'gpt-6'

class PottedBranchingLeafPlant(Solo48):
    icon_id = 'potted-branching-leaf-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        # Potted plant: two broad mirrored leaves, a central stem and open lower branches.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('pot',(16,34),(16,44),(32,44),(32,34),(16,34))
        l('stem',(24,34),(24,20))
        link('connect','stem','pot')
        for side in (-1,1):
            tip=(24+side*16,4)
            a(f'leaf-{side}-a',(24,20),tip,16,sweep=side<0)
            a(f'leaf-{side}-b',tip,(24,20),16,sweep=side<0)
            self.add_contour(f'leaf-{side}',f'leaf-{side}-a',f'leaf-{side}-b',closed=True)
            link('connect',f'leaf-{side}','stem')
            l(f'branch-{side}',(24,32),(24+side*16,26))
            link('connect',f'branch-{side}','stem')
        link('connect','leaf--1','leaf-1')
        link('connect','branch--1','branch-1')
