"""A smartphone storefront with four scalloped awning panels and a bottom bezel.

VRECT_L: ink (8,0)-(56,64), centerlines (10,2)-(54,62).
Lucide store and smartphone originals and atomic-debug informed repeated
scallops and the rounded device outline. Source bezel and home mark restored;
panels, phone and home mark are symmetric about x=32. No identity detail omitted.
Hosting (compose.py): plus valid; heart blocked; check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'e8d293a0-8723-40a8-943c-5339aa55feb8'
SOURCE_PATH = 'container_icons/svg/smartphone-with-store-awning-e8d293a0-8723-40a8-943c-5339aa55feb8.svg'
AUTHOR = 'gpt-6'


class SmartphoneWithStoreAwningVariant2(Container64):
    icon_id = 'smartphone-with-store-awning-v2'
    variant_of = 'smartphone-with-store-awning'
    variant_label = 'Four balanced awning panels and restored phone bezel'
    keyshape = Keyshape.VRECT_L
    category = 'containers'
    aliases = ()
    keywords = ('smartphone', 'store', 'awning', 'shopping')

    def build(self):
        # Plan: mirrored canopy and four scallops; phone sides attach to the
        # outer scallops at their cardinal bottom points. Bezel owns the home dot.
        axis, top, rule, lip = 32, 2, 10, 18
        self.add_line('canopy-top', (20, top), (44, top))
        self.add_arc('canopy-ne', (44, top), (50, rule), radius_x=6, radius_y=8)
        self.add_line('canopy-right', (50, rule), (54, lip))
        edges = (54, 44, 32, 20, 10)
        lobes = []
        for j, (right, left) in enumerate(zip(edges, edges[1:])):
            name = f'lobe-{j}'
            self.add_arc(name, (right, lip), (left, lip), radius_x=(right-left)//2)
            lobes.append(name)
        self.add_line('canopy-left', (10, lip), (14, rule))
        self.add_arc('canopy-nw', (14, rule), (20, top), radius_x=6, radius_y=8)
        self.add_contour('canopy', 'canopy-top', 'canopy-ne', 'canopy-right',
                         *lobes, 'canopy-left', 'canopy-nw', closed=True)
        self.add_line('awning-rule', (14, rule), (50, rule))
        self.relate('connect', 'awning-rule', 'canopy')
        for j, (upper_x, lower_x) in enumerate(((22,20),(axis,axis),(42,44))):
            name = f'panel-seam-{j}'
            self.add_line(name, (upper_x, rule), (lower_x, lip))
            self.relate('connect', name, 'awning-rule')
            self.relate('connect', name, 'canopy')
        left, right, radius, bottom, bezel_y = 15, 49, 6, 62, 46
        self.add_line('body-right', (right,23), (right,bottom-radius))
        self.add_arc('body-se', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('body-base', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('body-sw', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('body-left', (left,bottom-radius), (left,23))
        self.add_contour('body', 'body-right', 'body-se', 'body-base', 'body-sw', 'body-left')
        self.relate('connect', 'body', 'canopy')
        self.add_line('bezel', (left,bezel_y), (right,bezel_y))
        self.relate('connect', 'bezel', 'body')
        self.add_dot('home', (axis,54))
