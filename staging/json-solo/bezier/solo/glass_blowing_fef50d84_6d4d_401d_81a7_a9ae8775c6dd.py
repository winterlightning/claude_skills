"""Glass blowing (hobbies), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fef50d84-6d4d-401d-81a7-a9ae8775c6dd'
SOURCE_PATH = 'icons-json/hobbies/glass blowing_fef50d84-6d4d-401d-81a7-a9ae8775c6dd.json'
AUTHOR = 'json_to_solo'

class GlassBlowingHobbies(Solo48):
    icon_id = 'glass-blowing-hobbies'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('glass', 'blowing', 'hobbies')

    def build(self):
        self.add_line('sym-e0', (6, 42), (17, 31))
        self.add_line('sym-e1', (17, 31), (14, 29))
        self.add_bezier('sym-e2', (14, 29), ((12.421, 27.421), (15.943, 25.53), (16, 24)))
        self.add_bezier('sym-e3', (16, 24), ((16.025, 23.313), (16.09, 22.679), (16, 22)))
        self.add_bezier('sym-e4', (16, 22), ((15.804, 20.445), (15.64, 18.522), (16, 17)))
        self.add_bezier('sym-e5', (16, 17), ((17.456, 10.782), (23.487, 6), (30, 6)))
        self.add_bezier('sym-e6', (30, 6), ((30.065, 6), (29.935, 6), (30, 6)))
        self.add_bezier('sym-e7', (30, 6), ((30.262, 6), (30.738, 6), (31, 6)))
        self.add_bezier('sym-e8', (31, 6), ((33.908, 6), (36.878, 6.878), (39, 9)))
        self.add_bezier('sym-e9', (39, 9), ((41.122, 11.122), (42, 14.092), (42, 17)))
        self.add_bezier('sym-e10', (42, 17), ((42, 17.262), (42, 17.738), (42, 18)))
        self.add_bezier('sym-e11', (42, 18), ((42, 18.065), (42, 17.935), (42, 18)))
        self.add_bezier('sym-e12', (42, 18), ((42, 24.513), (37.218, 30.544), (31, 32)))
        self.add_bezier('sym-e13', (31, 32), ((29.478, 32.36), (27.555, 32.196), (26, 32)))
        self.add_bezier('sym-e14', (26, 32), ((25.321, 31.91), (24.687, 31.975), (24, 32)))
        self.add_bezier('sym-e15', (24, 32), ((22.47, 32.057), (20.579, 35.579), (19, 34)))
        self.add_line('sym-e16', (19, 34), (17, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
