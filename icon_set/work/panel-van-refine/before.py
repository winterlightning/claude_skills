"""panel-van: reconstructed on SOLO48 from the supplied reference."""
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
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('body-rear-1',(6, 36),(4, 36))
        self.add_line('body-rear-2',(4, 36),(4, 8))
        self.add_line('body-rear-3',(4, 8),(26, 8))
        self.add_line('body-rear-4',(26, 8),(26, 14))
        self.add_line('body-rear-5',(26, 14),(32, 14))
        self.add_bezier('nose',(32, 14),*(((38.79604989, 14.98601184), (44, 20.08104057), (44, 26)),))
        self.add_line('body-front-1',(44, 26),(44, 36))
        self.add_line('body-front-2',(44, 36),(42, 36))
        self.add_line('chassis',(16, 36),(32, 36))
        self.add_bezier('rear-top',(6, 36),*(((6.5, 33.790861), (8.73857625, 32.0), (11.5, 32.0)), ((14.209139, 32.0), (16.0, 33.790861), (16, 36))))
        self.add_bezier('rear-bottom',(16, 36),*(((16.0, 38.209139), (14.209139, 40), (11.5, 40)), ((8.73857625, 40), (6.5, 38.209139), (6, 36))))
        self.add_bezier('front-top',(32, 36),*(((32.0, 33.790861), (33.790861, 32.0), (36.5, 32.0)), ((39.26142375, 32.0), (41.5, 33.790861), (42, 36))))
        self.add_bezier('front-bottom',(42, 36),*(((41.5, 38.209139), (39.26142375, 40), (36.5, 40)), ((33.790861, 40), (32.0, 38.209139), (32, 36))))
        self.add_contour('body-rear',*('body-rear-1', 'body-rear-2', 'body-rear-3', 'body-rear-4', 'body-rear-5'),closed=False)
        self.add_contour('body-front',*('body-front-1', 'body-front-2'),closed=False)
        self.add_contour('rear-wheel',*('rear-top', 'rear-bottom'),closed=True)
        self.add_contour('front-wheel',*('front-top', 'front-bottom'),closed=True)
        self.relate('connect',*('body-rear-1', 'body-rear-2'))
        self.relate('connect',*('body-rear-1', 'rear-top'))
        self.relate('connect',*('body-rear-1', 'rear-bottom'))
        self.relate('connect',*('body-rear-2', 'body-rear-3'))
        self.relate('connect',*('body-rear-3', 'body-rear-4'))
        self.relate('connect',*('body-rear-4', 'body-rear-5'))
        self.relate('connect',*('body-rear-5', 'nose'))
        self.relate('connect',*('nose', 'body-front-1'))
        self.relate('connect',*('body-front-1', 'body-front-2'))
        self.relate('connect',*('body-front-2', 'front-top'))
        self.relate('connect',*('body-front-2', 'front-bottom'))
        self.relate('connect',*('chassis', 'rear-top'))
        self.relate('connect',*('chassis', 'rear-bottom'))
        self.relate('connect',*('chassis', 'front-top'))
        self.relate('connect',*('chassis', 'front-bottom'))
        self.relate('connect',*('rear-top', 'rear-bottom'))
        self.relate('connect',*('front-top', 'front-bottom'))
