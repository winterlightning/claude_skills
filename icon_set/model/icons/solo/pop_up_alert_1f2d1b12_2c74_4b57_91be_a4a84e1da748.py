'Popup question: widen the card and keep one clear question hook under three separated alert rays.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f2d1b12-2c74-4b57-91be-a4a84e1da748'
SOURCE_PATH = 'icons-json/apps/pop up alert_1f2d1b12-2c74-4b57-91be-a4a84e1da748.json'
AUTHOR = 'gpt-6'

class PopUpAlert(Solo48):
    icon_id = 'pop-up-alert'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('pop', 'up', 'alert', 'apps')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 12, 20, 36, 44, 3
        self.add_line('card-top', (left+radius,top), (right-radius,top))
        self.add_arc('card-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('card-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('card-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('card-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('card-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('card-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('card-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('card', *('card-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        # One coherent question hook; its dot is omitted where four-unit clearance would not fit.
        self.add_bezier('question',(21,31),((21,28),(27,28),(27,31)),((27,33),(24,33),(24,35)))
        self.add_line('ray',(24,4),(24,11))
        self.add_line('ray-left',(8,8),(11,12))
        self.add_line('ray-right',(37,12),(40,8))
