"""small-delivery-truck: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cc6a052-bd85-4786-ad57-af8947d75c17'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_1cc6a052-bd85-4786-ad57-af8947d75c17.svg'
AUTHOR = 'gpt-6'


class SmallDeliveryTruck(Solo48):
    icon_id = 'small-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('truck', 'delivery', 'lorry', 'cargo', 'shipping', 'logistics', 'transport', 'vehicle', 'sub icon')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('cargo-1',(6, 36),(4, 36))
        self.add_line('cargo-2',(4, 36),(4, 8))
        self.add_line('cargo-3',(4, 8),(24, 8))
        self.add_line('cargo-4',(24, 8),(24, 16))
        self.add_line('cargo-5',(24, 16),(24, 36))
        self.add_line('cargo-6',(24, 36),(16, 36))
        self.add_line('cab-roof',(24, 16),(32, 16))
        self.add_bezier('cab-nose',(32, 16),*(((38.79604989, 16.98601184), (44, 22.08104057), (44, 28)),))
        self.add_line('cab-bottom-1',(44, 28),(44, 36))
        self.add_line('cab-bottom-2',(44, 36),(42, 36))
        self.add_line('chassis',(24, 36),(32, 36))
        self.add_bezier('rear-top',(6, 36),*(((6.5, 33.790861), (8.73857625, 32.0), (11.5, 32.0)), ((14.209139, 32.0), (16.0, 33.790861), (16, 36))))
        self.add_bezier('rear-bottom',(16, 36),*(((16.0, 38.209139), (14.209139, 40), (11.5, 40)), ((8.73857625, 40), (6.5, 38.209139), (6, 36))))
        self.add_bezier('front-top',(32, 36),*(((32.0, 33.790861), (33.790861, 32.0), (36.5, 32.0)), ((39.26142375, 32.0), (41.5, 33.790861), (42, 36))))
        self.add_bezier('front-bottom',(42, 36),*(((41.5, 38.209139), (39.26142375, 40), (36.5, 40)), ((33.790861, 40), (32.0, 38.209139), (32, 36))))
        self.add_contour('cargo',*('cargo-1', 'cargo-2', 'cargo-3', 'cargo-4', 'cargo-5', 'cargo-6'),closed=False)
        self.add_contour('cab-bottom',*('cab-bottom-1', 'cab-bottom-2'),closed=False)
        self.add_contour('rear-wheel',*('rear-top', 'rear-bottom'),closed=True)
        self.add_contour('front-wheel',*('front-top', 'front-bottom'),closed=True)
        self.relate('connect',*('cargo-1', 'cargo-2'))
        self.relate('connect',*('cargo-1', 'rear-top'))
        self.relate('connect',*('cargo-1', 'rear-bottom'))
        self.relate('connect',*('cargo-2', 'cargo-3'))
        self.relate('connect',*('cargo-3', 'cargo-4'))
        self.relate('connect',*('cargo-4', 'cargo-5'))
        self.relate('connect',*('cargo-4', 'cab-roof'))
        self.relate('connect',*('cargo-5', 'cargo-6'))
        self.relate('connect',*('cargo-5', 'cab-roof'))
        self.relate('connect',*('cargo-5', 'chassis'))
        self.relate('connect',*('cargo-6', 'chassis'))
        self.relate('connect',*('cargo-6', 'rear-top'))
        self.relate('connect',*('cargo-6', 'rear-bottom'))
        self.relate('connect',*('cab-roof', 'cab-nose'))
        self.relate('connect',*('cab-nose', 'cab-bottom-1'))
        self.relate('connect',*('cab-bottom-1', 'cab-bottom-2'))
        self.relate('connect',*('cab-bottom-2', 'front-top'))
        self.relate('connect',*('cab-bottom-2', 'front-bottom'))
        self.relate('connect',*('chassis', 'front-top'))
        self.relate('connect',*('chassis', 'front-bottom'))
        self.relate('connect',*('rear-top', 'rear-bottom'))
        self.relate('connect',*('front-top', 'front-bottom'))


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('7fa4b356-9d73-4875-94fd-29e892bef9d8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/truck_7fa4b356-9d73-4875-94fd-29e892bef9d8.svg')]
