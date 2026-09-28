"""Fresh SOLO48 revision of hologram-cube-projector from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '662b3074-f86b-483a-a095-4f5acc053b0c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hologram-cube-projector/20260927T061852Z-thuan-mac-1/reference/virtual box_662b3074-f86b-483a-a095-4f5acc053b0c.svg'
AUTHOR = 'gpt-6'

class HologramCubeProjector(Solo48):
    icon_id = 'hologram-cube-projector'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('hologram', 'projector', 'cube', 'virtual', '3d', 'projection', 'object')

    def build(self) -> None:

        # Floating cube above a lens with two projection beams.
        poly(self,'cube',(24,4),(34,10),(34,20),(24,26),(14,20),(14,10),closed=True)
        poly(self,'cube-top',(14,10),(24,16),(34,10))
        line(self,'cube-spine',(24,16),(24,26))
        ellipse(self,'lens',24,39,5)
        line(self,'beam-left',(8,27),(14,33))
        line(self,'beam-right',(40,27),(34,33))
        contacts(self)
