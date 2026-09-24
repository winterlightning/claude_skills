"""SQUARE centerline6,6,42,42. Domed empty pin with circular plus badge. Real shared24,26 node is a3-4-5 point on badge; plus has9-unit radial clearance."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'edc387fb-8345-489a-a276-38ea07c6e827'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pin add_edc387fb-8345-489a-a276-38ea07c6e827.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pin-add'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('pin-cap',(6,17),(28,17),radius_x=11)
        self.add_bezier('pin-right',(28,17),((28,21),(26,24),(24,26)))
        self.add_line('pin-tip',(24,26),(17,36))
        self.add_bezier('pin-left',(17,36),((10,28),(6,23),(6,17)))
        self.add_contour('pin','pin-cap','pin-right','pin-tip','pin-left',closed=True)
        pts=[(22,32),(24,26),(32,22),(42,32),(32,42),(24,38),(22,32)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            name='badge-'+str(i);ids.append(name);self.add_arc(name,a,b,radius_x=10)
        self.add_contour('badge',*ids,closed=True)
        self.relate('connect','pin','badge')
        self.add_polyline('plus-h',(31,32),(32,32),(33,32))
        self.add_polyline('plus-v',(32,31),(32,32),(32,33))
        self.relate('connect','plus-h','plus-v')
