# Variant of pharaoh-nemes-mask; parent file remains unchanged.
'Pharaoh nemes mask: independent spacing revision.\n\nBroader drapes and crest; central nose replaces crowded eye dots; retain nemes and beard.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1975cc8c-a609-4ae8-b0fe-2049efc52c92'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/sphinx_1975cc8c-a609-4ae8-b0fe-2049efc52c92.svg'
AUTHOR = 'gpt-6'

class PharaohNemesMaskVariant2(Solo48):
    icon_id = 'pharaoh-nemes-mask-v2'
    variant_of = 'pharaoh-nemes-mask'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('pharaoh', 'mask', 'tutankhamun', 'egyptian', 'nemes', 'ancient', 'tomb', 'gold')

    def build(self):
        self.add_arc('crown-left',(6, 34),(15, 14),radius_x=9,radius_y=20,sweep=True)
        self.add_polyline('crown-top',(15, 14),(20, 14),(28, 14),(33, 14),closed=False)
        self.add_arc('crown-right',(33, 14),(42, 34),radius_x=9,radius_y=20,sweep=True)
        self.add_polyline('drape-right',(42, 34),(42, 42),(33, 42),(33, 30),closed=False)
        self.add_arc('chin-right',(33, 30),(24, 34),radius_x=9,radius_y=4,sweep=True)
        self.add_arc('chin-left',(24, 34),(15, 30),radius_x=9,radius_y=4,sweep=True)
        self.add_polyline('drape-left',(15, 30),(15, 42),(6, 42),(6, 34),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'crown-top']
        self.contours = [c for c in self.contours if c.contour_id != 'drape-right']
        self.contours = [c for c in self.contours if c.contour_id != 'drape-left']
        self.add_contour('outline','crown-left','crown-top-1','crown-top-2','crown-top-3','crown-right','drape-right-1','drape-right-2','drape-right-3','chin-right','chin-left','drape-left-1','drape-left-2','drape-left-3',closed=True)
        self.add_line('face-left',(15, 14),(15, 30))
        self.add_line('face-right',(33, 14),(33, 30))
        self.add_polyline('crest',(20, 14),(20, 6),(28, 6),(28, 14),closed=False)
        self.add_line('beard',(24, 34),(24, 42))
        self.add_dot('nose',(24, 23))
        self.relate('connect','outline','face-left')
        self.relate('connect','outline','face-right')
        self.relate('connect','outline','crest')
        self.relate('connect','outline','beard')
