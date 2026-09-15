"""Pod on elevated track, with shared rail/leg junctions. Wide envelope; Lucide train-front vehicle/rail relationship. One leg per side replaces double supports."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '92e4f6ba-4d5d-48a4-8318-02d1f6e40faf'
SOURCE_PATH = 'pictographic-primitives/technology/hyperloop track_92e4f6ba-4d5d-48a4-8318-02d1f6e40faf.svg'
AUTHOR = 'gpt-6'

class HyperloopPodOnTrack(Solo48):
    icon_id = 'hyperloop-pod-on-track'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hyperloop', 'pod', 'track', 'rail', 'train', 'transport', 'maglev')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('top',(9, 8),(24, 8))
        self.add_bezier('nose-top',(24, 8),*(((34.32253232, 8.51541981), (44, 12.84521932), (44, 18)),))
        self.add_line('nose-tip',(44, 18),(44, 22))
        self.add_bezier('nose-bottom',(44, 22),*(((44, 24.66752306), (42.15064767, 27.11368359), (39, 28)),))
        self.add_line('floor-1',(39, 28),(32, 28))
        self.add_line('floor-2',(32, 28),(16, 28))
        self.add_line('floor-3',(16, 28),(9, 28))
        self.add_bezier('rear-bottom',(9, 28),*(((5.84935233, 27.11368359), (4, 24.66752306), (4, 22)),))
        self.add_line('rear',(4, 22),(4, 14))
        self.add_bezier('rear-top',(4, 14),*(((4, 11.33247694), (5.84935233, 8.88631641), (9, 8)),))
        self.add_arc('window-curve',(24, 8),(34, 18),radius_x=10,radius_y=10,large_arc=False,sweep=False)
        self.add_line('window-bottom',(34, 18),(44, 18))
        self.add_line('leg-left-1',(16, 28),(10, 38))
        self.add_line('leg-left-2',(10, 38),(9, 40))
        self.add_line('leg-right-1',(32, 28),(38, 38))
        self.add_line('leg-right-2',(38, 38),(39, 40))
        self.add_line('rail-1',(4, 38),(10, 38))
        self.add_line('rail-2',(10, 38),(38, 38))
        self.add_line('rail-3',(38, 38),(44, 38))
        self.add_contour('pod',*('top', 'nose-top', 'nose-tip', 'nose-bottom', 'floor-1', 'floor-2', 'floor-3', 'rear-bottom', 'rear', 'rear-top'),closed=True)
        self.add_contour('window',*('window-curve', 'window-bottom'),closed=False)
        self.add_contour('leg-left',*('leg-left-1', 'leg-left-2'),closed=False)
        self.add_contour('leg-right',*('leg-right-1', 'leg-right-2'),closed=False)
        self.add_contour('rail',*('rail-1', 'rail-2', 'rail-3'),closed=False)
        self.relate('connect',*('window', 'pod'))
        self.relate('connect',*('leg-left', 'pod'))
        self.relate('connect',*('leg-right', 'pod'))
        self.relate('connect',*('rail', 'leg-left'))
        self.relate('connect',*('rail', 'leg-right'))
