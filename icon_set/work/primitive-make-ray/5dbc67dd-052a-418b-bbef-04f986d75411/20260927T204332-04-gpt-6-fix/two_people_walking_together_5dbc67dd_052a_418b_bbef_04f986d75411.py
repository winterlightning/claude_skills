"""Two walking figures face right in staggered mid-stride.

Construction: person-standing: circular heads and coherent limb strokes, reposed in matched walking poses.
Reduction: Outlined limbs reduced to stick strokes. The figures repeat at a 22-unit offset; stride asymmetry is intentional.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5dbc67dd-052a-418b-bbef-04f986d75411'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-people-walking-together/20260927T133645Z-thuan-mac-1/reference/refugee immigration_5dbc67dd-052a-418b-bbef-04f986d75411.svg'
AUTHOR = "gpt-6"


class TwoPeopleWalkingTogether(Solo48):
    icon_id = 'two-people-walking-together'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
    aliases = ()
    keywords = ('refugee', 'immigration', 'walking', 'people', 'migration', 'journey', 'pair')

    def build(self) -> None:
        # SQUARE extremes (6,6)-(42,42); a shared walking figure definition repeats twice.
        for n,offset in enumerate((0,22)):
         x=14+offset
         self.add_arc(f'head-{n}-a',(x,6),(x,12),radius_x=3)
         self.add_arc(f'head-{n}-b',(x,12),(x,6),radius_x=3)
         self.add_contour(f'head-{n}',f'head-{n}-a',f'head-{n}-b',closed=True)
         self.add_line(f'torso-{n}',(x,22),(x-2,31))
         self.add_polyline(f'arm-{n}',(x,22),(x+4,27),(x+6,27))
         self.add_polyline(f'legs-{n}',(x-8,42),(x-2,31),(x+5,42))
         self.relate('connect',f'torso-{n}',f'arm-{n}')
         self.relate('connect',f'torso-{n}',f'legs-{n}')
         self.mark_human_figure(f'walker-{n}', head=f'head-{n}', torso=f'torso-{n}', torso_junction='start')
