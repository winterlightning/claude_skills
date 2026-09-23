"""Monitor with Art Palette and Brush.

Symbol plan: Rounded monitor encloses kidney palette and pointed brush; central stand. Palette curves use tangent quarter-arcs and reverse notch. Brush leans deliberately as in reference. HRECT_L extremes (4,8)-(44,40).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '69067a56-4a6a-4f02-bdcf-fc3b45bb66ac'
SOURCE_PATH = 'pictographic-primitives/other/monitor painting_69067a56-4a6a-4f02-bdcf-fc3b45bb66ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'monitor-with-art-palette-and-brush'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('monitor', 'with', 'art', 'palette', 'and', 'brush')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded_box(self, name, left, top, right, bottom, r):
        self.add_line(name+'-top', (left+r,top), (right-r,top))
        self.add_arc(name+'-tr', (right-r,top), (right,top+r), radius_x=r)
        self.add_line(name+'-right', (right,top+r), (right,bottom-r))
        self.add_arc(name+'-br', (right,bottom-r), (right-r,bottom), radius_x=r)
        self.add_line(name+'-bottom', (right-r,bottom), (left+r,bottom))
        self.add_arc(name+'-bl', (left+r,bottom), (left,bottom-r), radius_x=r)
        self.add_line(name+'-left', (left,bottom-r), (left,top+r))
        self.add_arc(name+'-tl', (left,top+r), (left+r,top), radius_x=r)
        self.add_contour(name, *(name+'-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

    def build(self):
        self.add_line('screen-top',(8,8),(40,8))
        self.add_arc('screen-tr',(40,8),(44,12),radius_x=4)
        self.add_line('screen-right',(44,12),(44,28))
        self.add_arc('screen-br',(44,28),(40,32),radius_x=4)
        self.add_line('screen-bottom-right',(40,32),(24,32))
        self.add_line('screen-bottom-left',(24,32),(8,32))
        self.add_arc('screen-bl',(8,32),(4,28),radius_x=4)
        self.add_line('screen-left',(4,28),(4,12))
        self.add_arc('screen-tl',(4,12),(8,8),radius_x=4)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-right','screen-bottom-left','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(24,32),(24,40))
        self.add_polyline('foot',(14,40),(24,40),(34,40))
        self.relate('connect','stand','screen')
        self.relate('connect','stand','foot')
        # Coherent kidney-shaped palette with a reverse-curved thumb indentation.
        self.add_arc('palette-outer',(16,14),(16,26),radius_x=6,sweep=False)
        self.add_arc('palette-lower',(16,26),(20,22),radius_x=4,sweep=False)
        self.add_arc('palette-notch',(20,22),(22,20),radius_x=2,sweep=True)
        self.add_arc('palette-tip',(22,20),(24,18),radius_x=2,sweep=False)
        self.add_arc('palette-upper',(24,18),(20,14),radius_x=4,sweep=False)
        self.add_line('palette-top',(20,14),(16,14))
        self.add_contour('palette','palette-outer','palette-lower','palette-notch','palette-tip','palette-upper','palette-top',closed=True)
        self.add_line('bristle-right',(37,14),(37,18))
        self.add_arc('bristle-lower-right',(37,18),(34,21),radius_x=3)
        self.add_arc('bristle-lower-left',(34,21),(31,18),radius_x=3)
        self.add_line('bristle-tip',(31,18),(37,14))
        self.add_contour('brush-head','bristle-right','bristle-lower-right','bristle-lower-left','bristle-tip',closed=True)
        self.add_line('brush-handle',(34,21),(30,26))
        self.relate('connect','brush-handle','brush-head')
