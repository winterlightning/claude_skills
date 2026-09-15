'Unified the van roof and cab, used a sloped windscreen and two equal true circular wheels; Lucide truck informs the round-corner construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3179d20f-4838-4c26-a054-f8bbabbc255f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_3179d20f-4838-4c26-a054-f8bbabbc255f.svg'
AUTHOR = 'gpt-6'


class PanelVan(Solo48):
    icon_id = 'panel-van'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('van', 'panel van', 'delivery van', 'vehicle', 'transport', 'cargo', 'courier', 'side view')

    def build(self) -> None:
        # One continuous van roof, a sloped windscreen and two equal circular wheels.
        # HRECT_L centerline extremes (4,8)-(44,40); all genuine junctions share endpoints.
        self.add_line('rear',(4,34),(4,12))
        self.add_arc('rear-corner',(4,12),(8,8),radius_x=4)
        self.add_line('roof-panel',(8,8),(26,8))
        self.add_line('roof-cab',(26,8),(28,8))
        self.add_bezier('roof-turn',(28,8),((30,8),(31,9),(32,10)))
        self.add_line('windscreen',(32,10),(42,20))
        self.add_bezier('nose',(42,20),((44,22),(44,25),(44,28)))
        self.add_line('front',(44,28),(44,34))
        self.add_contour('body','rear','rear-corner','roof-panel','roof-cab','roof-turn','windscreen','nose','front')
        self.add_polyline('cab-window',(26,8),(26,20),(42,20))
        self.relate('connect','body','cab-window')
        self.add_line('chassis',(16,34),(32,34))

        self.add_arc('rear-wheel-top', (4,34), (16,34), radius_x=6, radius_y=6)
        self.add_arc('rear-wheel-bottom', (16,34), (4,34), radius_x=6, radius_y=6)
        self.add_contour('rear-wheel', 'rear-wheel-top', 'rear-wheel-bottom', closed=True)

        self.add_arc('front-wheel-top', (32,34), (44,34), radius_x=6, radius_y=6)
        self.add_arc('front-wheel-bottom', (44,34), (32,34), radius_x=6, radius_y=6)
        self.add_contour('front-wheel', 'front-wheel-top', 'front-wheel-bottom', closed=True)

        for wheel in ('rear-wheel','front-wheel'):
         self.relate('connect','body',wheel)
         self.relate('connect','chassis',wheel)
