"""Locomotive front grille; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1261a1dd-5b20-41fe-b8ee-3a27dbda4a58'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad train_1261a1dd-5b20-41fe-b8ee-3a27dbda4a58.svg'
AUTHOR = 'gpt-6'

class LocomotiveFrontGrille(Solo48):
    icon_id = 'locomotive-front-grille'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('locomotive', 'train', 'front', 'railway', 'diesel', 'rail', 'engine', 'transport')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('roof-left',(12, 4),(24, 4))
        self.add_line('roof-right',(24, 4),(36, 4))
        self.add_bezier('top-right',(36, 4),*(((37.6162858, 4), (39.19868669, 4.72578466), (40, 6)),))
        self.add_line('right-upper',(40, 6),(40, 18))
        self.add_line('right-middle',(40, 18),(40, 26))
        self.add_line('right-lower',(40, 26),(40, 34))
        self.add_arc('bottom-right',(40, 34),(36, 38),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_line('floor-0',(36, 38),(34, 38))
        self.add_line('floor-1',(34, 38),(32, 38))
        self.add_line('floor-2',(32, 38),(24, 38))
        self.add_line('floor-3',(24, 38),(16, 38))
        self.add_line('floor-4',(16, 38),(14, 38))
        self.add_line('floor-5',(14, 38),(12, 38))
        self.add_arc('bottom-left',(12, 38),(8, 34),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_line('left-lower',(8, 34),(8, 26))
        self.add_line('left-middle',(8, 26),(8, 18))
        self.add_line('left-upper',(8, 18),(8, 6))
        self.add_bezier('top-left',(8, 6),*(((8.80131331, 4.72578466), (10.3837142, 4), (12, 4)),))
        self.add_line('divider-1',(8, 18),(24, 18))
        self.add_line('divider-2',(24, 18),(40, 18))
        self.add_line('window-post',(24, 4),(24, 18))
        self.add_line('left-rail',(14, 38),(8, 44))
        self.add_line('right-rail',(34, 38),(40, 44))
        self.add_line('left-lamp',(8, 26),(10, 26))
        self.add_line('right-lamp',(38, 26),(40, 26))
        self.add_line('grille-left',(16, 38),(16, 35))
        self.add_arc('grille-upper-left',(16, 35),(24, 27),radius_x=8,radius_y=8,large_arc=False,sweep=True)
        self.add_arc('grille-upper-right',(24, 27),(32, 35),radius_x=8,radius_y=8,large_arc=False,sweep=True)
        self.add_line('grille-right',(32, 35),(32, 38))
        self.add_line('grille-slat',(24, 27),(24, 38))
        self.add_contour('body',*('roof-left', 'roof-right', 'top-right', 'right-upper', 'right-middle', 'right-lower', 'bottom-right', 'floor-0', 'floor-1', 'floor-2', 'floor-3', 'floor-4', 'floor-5', 'bottom-left', 'left-lower', 'left-middle', 'left-upper', 'top-left'),closed=True)
        self.add_contour('divider',*('divider-1', 'divider-2'),closed=False)
        self.add_contour('grille',*('grille-left', 'grille-upper-left', 'grille-upper-right', 'grille-right'),closed=False)
        self.relate('connect',*('divider', 'body'))
        self.relate('connect',*('window-post', 'body'))
        self.relate('connect',*('window-post', 'divider'))
        self.relate('connect',*('left-rail', 'body'))
        self.relate('connect',*('right-rail', 'body'))
        self.relate('connect',*('left-lamp', 'body'))
        self.relate('connect',*('right-lamp', 'body'))
        self.relate('connect',*('grille', 'body'))
        self.relate('connect',*('grille-slat', 'body'))
        self.relate('connect',*('grille-slat', 'grille'))
