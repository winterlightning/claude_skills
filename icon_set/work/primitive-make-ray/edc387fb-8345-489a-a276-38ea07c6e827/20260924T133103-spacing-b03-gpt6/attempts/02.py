"""SQUARE centerline6,6,42,42. Empty pin occluded by larger circular plus badge. Shared badge boundary closes pin; actual31,20 and20,31 endpoint attachments. Plus arms2 with9-unit radial clearance."""
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
        self.add_bezier('pin-right',(28,17),((28,18),(29,18),(30,18)))
        self.add_line('pin-tip',(18,30),(12,34))
        self.add_bezier('pin-left',(12,34),((8,27),(6,23),(6,17)))
        self.add_contour('pin','pin-tip','pin-left','pin-cap','pin-right')
        pts=[(18,30),(30,18),(42,30),(30,42),(18,30)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            name='badge-'+str(i);ids.append(name);self.add_arc(name,a,b,radius_x=12)
        self.add_contour('badge',*ids,closed=True)
        self.relate('connect','pin','badge')
        self.add_polyline('plus-h',(27,30),(30,30),(33,30))
        self.add_polyline('plus-v',(30,27),(30,30),(30,33))
        self.relate('connect','plus-h','plus-v')
