"""Moving window with trailing edge. HRECT_L preserves a wide window; one broad echo replaces two crowded trails. Lucide smartphone-style rounded corners, inspected earlier in this task."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a027a723-6775-453a-b9a9-bbf4820ea975'
SOURCE_PATH = 'pictographic-primitives/technology/lazy moving animation_a027a723-6775-453a-b9a9-bbf4820ea975.svg'
AUTHOR = 'gpt-6'

class WindowWithMotionTrails(Solo48):
    icon_id = 'window-with-motion-trails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('animation', 'motion', 'window', 'movement', 'trail', 'interface', 'transition')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('windowt',(8, 14),(28, 14))
        self.add_arc('windowtr',(28, 14),(32, 18),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_line('windowr',(32, 18),(32, 30))
        self.add_arc('windowbr',(32, 30),(28, 34),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_line('windowb',(28, 34),(8, 34))
        self.add_arc('windowbl',(8, 34),(4, 30),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_line('windowl',(4, 30),(4, 18))
        self.add_arc('windowtl',(4, 18),(8, 14),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_bezier('trail-top',(39, 8),*(((42.15064767, 8.88631641), (44, 11.33247694), (44, 14)),))
        self.add_line('trail-side',(44, 14),(44, 34))
        self.add_bezier('trail-bottom',(44, 34),*(((44, 36.66752306), (42.15064767, 39.11368359), (39, 40)),))
        self.add_contour('window',*('windowt', 'windowtr', 'windowr', 'windowbr', 'windowb', 'windowbl', 'windowl', 'windowtl'),closed=True)
        self.add_contour('motion-trail',*('trail-top', 'trail-side', 'trail-bottom'),closed=False)
