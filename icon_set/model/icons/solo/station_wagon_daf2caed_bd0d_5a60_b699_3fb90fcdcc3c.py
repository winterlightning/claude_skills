"""A long right-facing estate car with three side windows and a flat roof. Broad envelope supports all three windows. Lucide car informed body construction; hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'daf2caed-bd0d-5a60-b699-3fb90fcdcc3c'
SOURCE_PATH = 'pictographic-primitives/transportation/car wagon_daf2caed-bd0d-5a60-b699-3fb90fcdcc3c.svg'
SOURCE_REFERENCES = (('daf2caed-bd0d-5a60-b699-3fb90fcdcc3c', 'pictographic-primitives/transportation/car wagon_daf2caed-bd0d-5a60-b699-3fb90fcdcc3c.svg'),)
AUTHOR = 'gpt-6'

class StationWagon(Solo48):
    icon_id = 'station-wagon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('station wagon', 'estate car', 'car', 'wagon', 'family car', 'vehicle', 'side view', 'automobile')

    def build(self) -> None:
        self.add_line('back',(4,33),(4,20))
        self.add_line('top-0',(4,20),(12,20))
        self.add_line('top-1',(12,20),(22,20))
        self.add_line('top-2',(22,20),(34,20))
        self.add_arc('nose',(34,20),(44,30),radius_x=10)
        self.add_line('front',(44,30),(44,33))
        self.add_contour('body','back','top-0','top-1','top-2','nose','front')

        for name,x in [('rear',11),('front',37)]:
            self.add_arc(name+'-a',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(name+'-b',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(name+'-wheel',name+'-a',name+'-b',closed=True)
        self.add_line('chassis',(18,33),(30,33))
        for name in ['rear-wheel','front-wheel']:
            self.relate('connect','body',name)
            self.relate('connect','chassis',name)

        self.add_polyline('cabin',(4,20),(4,8),(12,8),(22,8),(26,8),(34,20))
        self.relate('connect','cabin','body')
        for x in (12,22):
            self.add_line(f'pillar-{x}',(x,8),(x,20))
            self.relate('connect',f'pillar-{x}','cabin')
            self.relate('connect',f'pillar-{x}','body')
