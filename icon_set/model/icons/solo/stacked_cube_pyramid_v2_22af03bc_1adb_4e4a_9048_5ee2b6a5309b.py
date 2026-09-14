# Variant of stacked-cube-pyramid; parent file remains unchanged.
'Stacked cube pyramid: independent spacing revision.\n\nDeeper isometric faces and taller lower cubes retain all three blocks with wider perpendicular spacing.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '22af03bc-1adb-4e4a-9048-5ee2b6a5309b'
SOURCE_PATH = 'pictographic-primitives/technology/element reallity kit_22af03bc-1adb-4e4a-9048-5ee2b6a5309b.svg'
AUTHOR = 'gpt-6'

class StackedCubePyramidVariant2(Solo48):
    icon_id = 'stacked-cube-pyramid-v2'
    variant_of = 'stacked-cube-pyramid'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('cubes', 'blocks', '3d', 'stack', 'objects', 'reality-kit', 'geometry')

    def build(self):
        self.add_polyline('outline',(24, 6),(33, 11),(33, 21),(42, 26),(42, 37),(33, 42),(24, 37),(15, 42),(6, 37),(6, 26),(15, 21),(15, 11),closed=True)
        self.add_polyline('top-face',(15, 11),(24, 16),(33, 11),closed=False)
        self.add_polyline('center',(24, 16),(24, 26),(24, 37),closed=False)
        self.add_polyline('middle',(15, 21),(24, 26),(33, 21),closed=False)
        self.add_polyline('left-face',(6, 26),(15, 31),(24, 26),closed=False)
        self.add_line('left-edge',(15, 31),(15, 42))
        self.add_polyline('right-face',(24, 26),(33, 31),(42, 26),closed=False)
        self.add_line('right-edge',(33, 31),(33, 42))
        self.relate('connect','outline','top-face')
        self.relate('connect','center','top-face')
        self.relate('connect','center','outline')
        self.relate('connect','middle','outline')
        self.relate('connect','middle','center')
        self.relate('connect','left-face','outline')
        self.relate('connect','left-face','center')
        self.relate('connect','left-face','middle')
        self.relate('connect','left-edge','left-face')
        self.relate('connect','left-edge','outline')
        self.relate('connect','right-face','outline')
        self.relate('connect','right-face','center')
        self.relate('connect','right-face','middle')
        self.relate('connect','right-face','left-face')
        self.relate('connect','right-edge','right-face')
        self.relate('connect','right-edge','outline')
