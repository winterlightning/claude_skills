"""VRECT_L centerline8,4,40,44. Globe dome above symmetric open book. Shared exact globe latitude/longitude nodes. Remove small page text to open the book interior."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '707a74f4-f696-4ab1-aaf2-6be7de8a3c1a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/read world_707a74f4-f696-4ab1-aaf2-6be7de8a3c1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'read-world'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        nodes=[(9,19),(12,10),(24,4),(36,10),(39,19)]
        for i,(a,b) in enumerate(zip(nodes,nodes[1:])):self.add_arc('dome-'+str(i),a,b,radius_x=15)
        self.add_contour('globe-dome',*['dome-'+str(i) for i in range(4)])
        for name,a,b in [('left-top',(24,4),(20,10)),('left-bottom',(20,10),(19,19)),('right-top',(24,4),(28,10)),('right-bottom',(28,10),(29,19))]:
            self.add_arc(name,a,b,radius_x=5,radius_y=15,sweep=name.startswith('right'))
        self.add_contour('longitude-left','left-top','left-bottom')
        self.add_contour('longitude-right','right-top','right-bottom')
        for name in ('longitude-left','longitude-right'):self.relate('connect',name,'globe-dome')
        self.relate('connect','longitude-left','longitude-right')
        self.add_polyline('latitude',(12,10),(20,10),(28,10),(36,10))
        for name in ('globe-dome','longitude-left','longitude-right'):self.relate('connect','latitude',name)
        self.add_bezier('book-top',(8,27),((16,27),(20,28),(24,31)),((28,28),(32,27),(40,27)))
        self.add_line('book-right',(40,27),(40,40))
        self.add_bezier('book-bottom',(40,40),((32,40),(28,41),(24,44)),((20,41),(16,40),(8,40)))
        self.add_line('book-left',(8,40),(8,27))
        self.add_contour('book','book-top','book-right','book-bottom','book-left',closed=True)
        self.add_line('spine',(24,31),(24,44))
        self.relate('connect','spine','book')
