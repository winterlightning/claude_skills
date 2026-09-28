from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51c8e679-859d-5949-a9e7-c38c98a4994e'
SOURCE_PATH = 'pictographic-primitives/transportation/road tunnel_51c8e679-859d-5949-a9e7-c38c98a4994e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '51c8e679-859d-5949-a9e7-c38c98a4994e', 'source_path': 'pictographic-primitives/transportation/road tunnel_51c8e679-859d-5949-a9e7-c38c98a4994e.svg'}]

class RailwayTunnel(Solo48):
    icon_id = 'railway-tunnel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('railway tunnel', 'tunnel', 'rail', 'track', 'train', 'arch', 'underground', 'infrastructure')

    def build(self):
        self.add_line('outer-left',(4,40),(4,28))
        self.add_arc('outer-arch',(4,28),(44,28),radius_x=20,sweep=True)
        self.add_line('outer-right',(44,28),(44,40))
        self.add_contour('outer','outer-left','outer-arch','outer-right')
        self.add_arc('inner-arch',(17,27),(31,27),radius_x=7,sweep=True)
        self.add_polyline('left-rail',(17,27),(14,36),(13,40))
        self.add_polyline('right-rail',(31,27),(34,36),(35,40))
        self.add_line('far-sleeper',(17,27),(31,27))
        self.add_line('near-sleeper',(14,36),(34,36))
        for a,b in (('inner-arch','left-rail'),('inner-arch','right-rail'),('far-sleeper','left-rail'),('far-sleeper','right-rail'),('near-sleeper','left-rail'),('near-sleeper','right-rail')):self.relate('connect',a,b)
