"""Complete floating interface window with integral ornament toolbar and lower baseline. Lucide smartphone rounded corners; structural UI treated as one solo subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6f72285-8383-5eda-aeb5-2c86f3adb877'
SOURCE_PATH = 'pictographic-primitives/technology/element ornament_b6f72285-8383-5eda-aeb5-2c86f3adb877.svg'
AUTHOR = 'gpt-6'

class WindowWithOrnamentBar(Solo48):
    icon_id = 'window-with-ornament-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('window', 'ornament', 'toolbar', 'display', 'spatial', 'interface', 'screen')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('top',(9, 8),(39, 8))
        self.add_bezier('tr',(39, 8),*(((42.15064767, 8.88631641), (44, 11.33247694), (44, 14)),))
        self.add_line('right',(44, 14),(44, 20))
        self.add_bezier('br',(44, 20),*(((44, 22.66752306), (42.15064767, 25.11368359), (39, 26)),))
        self.add_line('bottom-r',(39, 26),(34, 26))
        self.add_line('ornamentt',(19, 21),(29, 21))
        self.add_arc('ornamenttr',(29, 21),(34, 26),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_line('ornamentr',(34, 26),(34, 26))
        self.add_arc('ornamentbr',(34, 26),(29, 31),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_line('ornamentb',(29, 31),(19, 31))
        self.add_arc('ornamentbl',(19, 31),(14, 26),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_line('ornamentl',(14, 26),(14, 26))
        self.add_arc('ornamenttl',(14, 26),(19, 21),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_line('bottom-l',(14, 26),(9, 26))
        self.add_bezier('bl',(9, 26),*(((5.84935233, 25.11368359), (4, 22.66752306), (4, 20)),))
        self.add_line('left',(4, 20),(4, 14))
        self.add_bezier('tl',(4, 14),*(((4, 11.33247694), (5.84935233, 8.88631641), (9, 8)),))
        self.add_line('base',(19, 40),(29, 40))
        self.add_contour('ornament',*('ornamentt', 'ornamenttr', 'ornamentr', 'ornamentbr', 'ornamentb', 'ornamentbl', 'ornamentl', 'ornamenttl'),closed=True)
        self.add_contour('window',*('bottom-l', 'bl', 'left', 'tl', 'top', 'tr', 'right', 'br', 'bottom-r'),closed=False)
        self.relate('connect',*('window', 'ornament'))
