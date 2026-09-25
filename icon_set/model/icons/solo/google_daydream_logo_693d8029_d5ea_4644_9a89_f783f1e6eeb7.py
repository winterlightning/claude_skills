"""A flower-like cloud of eight scalloped petals, each formed by a curling stroke that turns in toward an empty centre.

Plan: Eight scallops arranged about x=y=24; four axial lobes and four diagonal lobes share integer nodes.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful exact logo match; repeating scalloped lobes.
Simplification: Short inward curls removed to keep the eight-petal silhouette open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '693d8029-d5ea-4644-9a89-f783f1e6eeb7'
SOURCE_PATH = 'pictographic-primitives/logos/google daydream logo_693d8029-d5ea-4644-9a89-f783f1e6eeb7.svg'
AUTHOR = 'gpt-6'


class GoogleDaydreamLogo(Solo48):
    icon_id = 'google-daydream-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-daydream', 'daydream', 'vr', 'google', 'logo', 'brand', 'cloud')

    def build(self):
        # The shared nodes define the eight-petal rotational pattern.
        nodes=[(18,12),(30,12),(36,18),(36,30),(30,36),(18,36),(12,30),(12,18)]
        controls=[((16,4),(32,4)),((40,4),(44,12)),((44,16),(44,32)),((44,40),(36,44)),((32,44),(16,44)),((8,44),(4,36)),((4,32),(4,16)),((4,8),(12,4))]
        # Axial lobes use exact cardinal semicircles, making the square extremes exact.
        for i,(p,q) in enumerate(zip(nodes,nodes[1:]+nodes[:1])):
            if i%2==0:
                self.add_arc(f'petal-{i}',p,q,radius_x=6,sweep=True)
            else:
                self.add_bezier(f'petal-{i}',p,(*controls[i],q))
        self.add_contour('petals',*(f'petal-{i}' for i in range(8)),closed=True)
