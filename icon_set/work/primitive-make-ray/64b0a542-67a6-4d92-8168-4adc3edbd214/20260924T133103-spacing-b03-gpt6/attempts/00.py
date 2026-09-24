"""Patent certificate with fold, writing and ribbon seal. VRECT_L extremes8,4,40,44; true circular attachment nodes derive from a 3-4-5 triangle."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '64b0a542-67a6-4d92-8168-4adc3edbd214'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/patentee_64b0a542-67a6-4d92-8168-4adc3edbd214.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'patentee'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        # Folded patent page, text and ribbon seal; seal attachment nodes lie exactly on radius5 circle.
        self.add_polyline('page',(20,36),(8,36),(8,4),(30,4),(40,14))
        self.add_polyline('fold',(30,4),(30,14),(40,14))
        self.relate('connect','fold','page')
        self.add_line('text-top',(16,16),(22,16))
        self.add_line('text-bottom',(16,24),(20,24))
        pts=[(34,24),(39,29),(38,32),(34,34),(30,32),(29,29),(34,24)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            name='seal-'+str(i);ids.append(name)
            self.add_arc(name,a,b,radius_x=5)
        self.add_contour('seal',*ids,closed=True)
        self.add_polyline('ribbon',(30,32),(30,44),(34,42),(38,44),(38,32))
        self.relate('connect','seal','ribbon')
