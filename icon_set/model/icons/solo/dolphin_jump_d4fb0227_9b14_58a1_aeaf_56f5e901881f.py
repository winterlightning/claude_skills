"""Dolphin leaping left through an interrupted vertical hoop. Centerlines (2,2)-(46,46). Lucide fish informs body/fin contour; eye omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4fb0227-9b14-58a1-aeaf-56f5e901881f'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin jump_d4fb0227-9b14-58a1-aeaf-56f5e901881f.svg'
AUTHOR = 'gpt-6'


class DolphinThroughHoop(Solo48):
    icon_id = 'dolphin-through-hoop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/marine'
    aliases = ()
    keywords = ('dolphin', 'hoop', 'jump', 'circus', 'trick', 'marine', 'show', 'sea')

    def build(self) -> None:
        self.add_arc('head',(4,27),(16,17),radius_x=13)
        self.add_polyline('dorsal',(16,17),(23,11),(23,18))
        self.add_arc('back',(23,18),(37,25),radius_x=30)
        self.add_polyline('fluke',(37,25),(46,23),(42,30),(43,37),(35,31))
        self.add_arc('belly',(35,31),(24,28),radius_x=26,sweep=False)
        self.add_polyline('flipper',(24,28),(26,35),(17,29),(2,33),(4,27))
        self.relate('connect','head','dorsal')
        self.relate('connect','dorsal','back')
        self.relate('connect','back','fluke')
        self.relate('connect','fluke','belly')
        self.relate('connect','belly','flipper')
        self.relate('connect','flipper','head')
        self.add_arc('hoop-top-left',(16,9),(24,2),radius_x=8,radius_y=7)
        self.add_arc('hoop-top-right',(24,2),(34,14),radius_x=10,radius_y=12)
        self.add_contour('hoop-top','hoop-top-left','hoop-top-right')
        self.add_arc('hoop-bottom-right',(34,38),(24,46),radius_x=10,radius_y=8)
        self.add_arc('hoop-bottom-left',(24,46),(16,38),radius_x=8,radius_y=8)
        self.add_contour('hoop-bottom','hoop-bottom-right','hoop-bottom-left')
