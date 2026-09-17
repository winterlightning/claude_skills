from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db3558a2-3a7b-5e7e-860f-ab7b0a4582cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color palette_db3558a2-3a7b-5e7e-860f-ab7b0a4582cd.svg'
AUTHOR = 'gpt-6'


class AngledThreeCardColorSwatchFan(Solo48):
    icon_id = 'angled-three-card-color-swatch-fan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('swatches', 'fan', 'color', 'cards', 'palette', 'pivot', 'samples', 'design')

    def build(self) -> None:
        # Three occluded cards share one pivot; only exposed rear edges are drawn.
        points=[(14,6),(32,10),(28,24),(24,38),(24,42),(14,42)]
        for n,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'front-top-{n}',a,b)
        self.add_arc('front-bottom',(14,42),(6,34),radius_x=8)
        self.add_line('front-left',(6,34),(14,6))
        self.add_contour('front',*[f'front-top-{n}' for n in range(1,6)],'front-bottom','front-left',closed=True)
        self.add_dot('pivot',(15,32))
        self.add_polyline('middle',(28,24),(36,16),(42,24),(33,31),(24,38))
        self.add_polyline('rear',(33,31),(42,31),(42,42),(24,42))
        self.relate('connect','front','middle');self.relate('connect','middle','rear');self.relate('connect','front','rear')
