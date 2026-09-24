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
        self.add_bezier('pin-right',(28,17),((28,19),(29,20),(31,20)))
        self.add_line('pin-tip',(20,31),(17,36))
        self.add_bezier('pin-left',(17,36),((10,28),(6,23),(6,17)))
        self.add_contour('pin','pin-tip','pin-left','pin-cap','pin-right')
        pts=[(20,31),(31,20),(42,31),(31,42),(20,31)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            name='badge-'+str(i);ids.append(name);self.add_arc(name,a,b,radius_x=11)
        self.add_contour('badge',*ids,closed=True)
        self.relate('connect','pin','badge')
        self.add_polyline('plus-h',(29,31),(31,31),(33,31))
        self.add_polyline('plus-v',(31,29),(31,31),(31,33))
        self.relate('connect','plus-h','plus-v')
