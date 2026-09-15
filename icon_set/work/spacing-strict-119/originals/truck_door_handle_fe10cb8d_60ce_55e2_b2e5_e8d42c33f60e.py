"""truck-door-handle: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe10cb8d-60ce-55e2-b2e5-e8d42c33f60e'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_fe10cb8d-60ce-55e2-b2e5-e8d42c33f60e.svg'
AUTHOR = 'gpt-6'


class TruckDoorHandle(Solo48):
    icon_id = 'truck-door-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('truck', 'delivery', 'lorry', 'cargo', 'moving', 'logistics', 'transport', 'vehicle')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('cargo-rear-1',(6, 36),(4, 36))
        self.add_line('cargo-rear-2',(4, 36),(4, 12))
        self.add_bezier('cargo-tl',(4, 12),*(((4, 10.3837142), (4.72578466, 8.80131331), (6, 8)),))
        self.add_line('cargo-roof',(6, 8),(22, 8))
        self.add_arc('cargo-tr',(22, 8),(26, 12),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_line('cargo-front-1',(26, 12),(26, 16))
        self.add_line('cargo-front-2',(26, 16),(26, 36))
        self.add_line('cargo-front-3',(26, 36),(16, 36))
        self.add_line('handle',(15, 18),(15, 23))
        self.add_line('cab-roof',(26, 16),(32, 16))
        self.add_bezier('cab-nose',(32, 16),*(((38.79604989, 16.98601184), (44, 22.08104057), (44, 28)),))
        self.add_line('cab-bottom-1',(44, 28),(44, 36))
        self.add_line('cab-bottom-2',(44, 36),(42, 36))
        self.add_line('chassis',(26, 36),(32, 36))
        self.add_bezier('rear-top',(6, 36),*(((6.5, 33.790861), (8.73857625, 32.0), (11.5, 32.0)), ((14.209139, 32.0), (16.0, 33.790861), (16, 36))))
        self.add_bezier('rear-bottom',(16, 36),*(((16.0, 38.209139), (14.209139, 40), (11.5, 40)), ((8.73857625, 40), (6.5, 38.209139), (6, 36))))
        self.add_bezier('front-top',(32, 36),*(((32.0, 33.790861), (33.790861, 32.0), (36.5, 32.0)), ((39.26142375, 32.0), (41.5, 33.790861), (42, 36))))
        self.add_bezier('front-bottom',(42, 36),*(((41.5, 38.209139), (39.26142375, 40), (36.5, 40)), ((33.790861, 40), (32.0, 38.209139), (32, 36))))
        self.add_contour('cargo-rear',*('cargo-rear-1', 'cargo-rear-2'),closed=False)
        self.add_contour('cargo-front',*('cargo-front-1', 'cargo-front-2', 'cargo-front-3'),closed=False)
        self.add_contour('cab-bottom',*('cab-bottom-1', 'cab-bottom-2'),closed=False)
        self.add_contour('rear-wheel',*('rear-top', 'rear-bottom'),closed=True)
        self.add_contour('front-wheel',*('front-top', 'front-bottom'),closed=True)
        self.relate('connect',*('cargo-rear-1', 'cargo-rear-2'))
        self.relate('connect',*('cargo-rear-1', 'rear-top'))
        self.relate('connect',*('cargo-rear-1', 'rear-bottom'))
        self.relate('connect',*('cargo-rear-2', 'cargo-tl'))
        self.relate('connect',*('cargo-tl', 'cargo-roof'))
        self.relate('connect',*('cargo-roof', 'cargo-tr'))
        self.relate('connect',*('cargo-tr', 'cargo-front-1'))
        self.relate('connect',*('cargo-front-1', 'cargo-front-2'))
        self.relate('connect',*('cargo-front-1', 'cab-roof'))
        self.relate('connect',*('cargo-front-2', 'cargo-front-3'))
        self.relate('connect',*('cargo-front-2', 'cab-roof'))
        self.relate('connect',*('cargo-front-2', 'chassis'))
        self.relate('connect',*('cargo-front-3', 'chassis'))
        self.relate('connect',*('cargo-front-3', 'rear-top'))
        self.relate('connect',*('cargo-front-3', 'rear-bottom'))
        self.relate('connect',*('cab-roof', 'cab-nose'))
        self.relate('connect',*('cab-nose', 'cab-bottom-1'))
        self.relate('connect',*('cab-bottom-1', 'cab-bottom-2'))
        self.relate('connect',*('cab-bottom-2', 'front-top'))
        self.relate('connect',*('cab-bottom-2', 'front-bottom'))
        self.relate('connect',*('chassis', 'front-top'))
        self.relate('connect',*('chassis', 'front-bottom'))
        self.relate('connect',*('rear-top', 'rear-bottom'))
        self.relate('connect',*('front-top', 'front-bottom'))
