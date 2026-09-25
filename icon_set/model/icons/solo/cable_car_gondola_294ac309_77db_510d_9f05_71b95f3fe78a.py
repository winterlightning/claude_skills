"""A gondola with three windows suspended from a diagonal cable. SQUARE ink (6,6)-(42,42). Lucide cable-car informed the shared roof hanger and windows; the pulley is merged into the hanger joint."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '294ac309-77db-510d-9f05-71b95f3fe78a'
SOURCE_PATH = 'pictographic-primitives/transportation/cable car_294ac309-77db-510d-9f05-71b95f3fe78a.svg'
SOURCE_REFERENCES = (('294ac309-77db-510d-9f05-71b95f3fe78a', 'pictographic-primitives/transportation/cable car_294ac309-77db-510d-9f05-71b95f3fe78a.svg'),)
AUTHOR = 'gpt-6'

class CableCarGondola(Solo48):
    icon_id = 'cable-car-gondola'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('cable car', 'gondola', 'ropeway', 'aerial lift', 'ski lift', 'cabin', 'mountain', 'transport')

    def build(self) -> None:
        self.add_line('cabin-top-0',(12, 20),(18, 20))
        self.add_line('cabin-top-1',(18, 20),(24, 20))
        self.add_line('cabin-top-2',(24, 20),(30, 20))
        self.add_line('cabin-top-3',(30, 20),(36, 20))
        self.add_arc('cabin-top-corner',(36, 20),(40, 24),radius_x=4)
        self.add_line('cabin-right-0',(40, 24),(40, 30))
        self.add_line('cabin-right-1',(40, 30),(40, 38))
        self.add_arc('cabin-right-corner',(40, 38),(36, 42),radius_x=4)
        self.add_line('cabin-bottom-0',(36, 42),(12, 42))
        self.add_arc('cabin-bottom-corner',(12, 42),(8, 38),radius_x=4)
        self.add_line('cabin-left-0',(8, 38),(8, 30))
        self.add_line('cabin-left-1',(8, 30),(8, 24))
        self.add_arc('cabin-left-corner',(8, 24),(12, 20),radius_x=4)
        self.add_contour('cabin','cabin-top-0','cabin-top-1','cabin-top-2','cabin-top-3','cabin-top-corner','cabin-right-0','cabin-right-1','cabin-right-corner','cabin-bottom-0','cabin-bottom-corner','cabin-left-0','cabin-left-1','cabin-left-corner',closed=True)

        self.add_polyline('cable',(6,14),(24,10),(42,6))
        self.add_line('hanger',(24,10),(24,20))
        self.relate('connect','hanger','cable')
        self.relate('connect','hanger','cabin')
        self.add_polyline('window-bottom',(8,30),(18,30),(30,30),(40,30))
        self.relate('connect','window-bottom','cabin')
        for i,x in enumerate((18,30)):
            self.add_line(f'window-{i}',(x,20),(x,30))
            self.relate('connect',f'window-{i}','cabin')
            self.relate('connect',f'window-{i}','window-bottom')
