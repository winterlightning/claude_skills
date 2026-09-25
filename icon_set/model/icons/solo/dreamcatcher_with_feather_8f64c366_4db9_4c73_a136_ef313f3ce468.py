"""Dreamcatcher with Feather.

Plan: Round spoke web with three hanging cords and an oval feather. Reduce double rim and inner ring; shared exact radial attachment nodes. Bounds (10,4)-(38,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f64c366-4db9-4c73-a136-ef313f3ce468'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/dreamcatcher_8f64c366-4db9-4c73-a136-ef313f3ce468.svg'
AUTHOR = 'gpt-6'


class DreamcatcherWithFeather(Solo48):
    icon_id = 'dreamcatcher-with-feather'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('dreamcatcher', 'with', 'feather')

    def build(self):
        points=[(24,4),(34,14),(30,22),(24,24),(18,22),(14,14),(24,4)]
        for i,(a,b) in enumerate(zip(points,points[1:])):self.add_arc(f'ring-{i}',a,b,radius_x=10)
        self.add_contour('ring',*[f'ring-{i}' for i in range(6)],closed=True)
        self.add_polyline('web-horizontal',(14,14),(24,14),(34,14))
        self.add_polyline('web-vertical',(24,4),(24,14),(24,24))
        self.relate('connect','web-horizontal','web-vertical')
        for p in ['web-horizontal','web-vertical']:self.relate('connect',p,'ring')
        for p,a,b in [('left-cord',(18,22),(10,34)),('right-cord',(30,22),(38,34)),('middle-cord',(24,24),(24,32))]:
            self.add_line(p,a,b);self.relate('connect',p,'ring')
        self.add_arc('feather-r',(24,32),(24,44),radius_x=4,radius_y=6)
        self.add_arc('feather-l',(24,44),(24,32),radius_x=4,radius_y=6)
        self.add_contour('feather','feather-r','feather-l',closed=True)
        self.relate('connect','feather','middle-cord')
