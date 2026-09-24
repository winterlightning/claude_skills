"""SQUARE centerline6,6,42,42. Clipped-corner document and centered radius9 clock. Minute and hour hands genuinely meet the dial at12 and3, with split cardinal endpoints. Bottom text rule removed to open the frame."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/rectangle history_5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rectangle-history'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('document',(6,6),(32,6),(42,16),(42,42),(6,42),closed=True)
        pts=[(15,24),(24,15),(33,24),(24,33),(15,24)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            name='clock-'+str(i);ids.append(name);self.add_arc(name,a,b,radius_x=9)
        self.add_contour('clock',*ids,closed=True)
        self.add_polyline('hands',(24,15),(24,24),(27,24))
        self.relate('connect','hands','clock')
