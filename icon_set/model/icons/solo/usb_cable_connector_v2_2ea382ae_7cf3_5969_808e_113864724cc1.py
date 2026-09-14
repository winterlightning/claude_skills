# Variant of usb-cable-connector; parent file remains unchanged.
'Usb cable connector: independent spacing revision.\n\nWider connector and raised rounded grip; remove cramped tip mark and open cable return.\nNative solo family, VRECT_M keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ea382ae-7cf3-5969-808e-113864724cc1'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/usb cable_2ea382ae-7cf3-5969-808e-113864724cc1.svg'
AUTHOR = 'gpt-6'

class UsbCableConnectorVariant2(Solo48):
    icon_id = 'usb-cable-connector-v2'
    variant_of = 'usb-cable-connector'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('usb', 'cable', 'connector', 'plug', 'cord', 'charging', 'port', 'computer')

    def build(self):
        self.add_polyline('tip',(20, 16),(20, 4),(36, 4),(36, 16),closed=False)
        self.add_polyline('body-top',(16, 16),(20, 16),(36, 16),(40, 16),(40, 20),closed=False)
        self.add_arc('body-right',(40, 20),(28, 32),radius_x=12,radius_y=12,sweep=True)
        self.add_arc('body-left',(28, 32),(16, 20),radius_x=12,radius_y=12,sweep=True)
        self.add_line('side',(16, 20),(16, 16))
        self.contours = [c for c in self.contours if c.contour_id != 'body-top']
        self.add_contour('body','body-top-1','body-top-2','body-top-3','body-top-4','body-right','body-left','side',closed=True)
        self.add_line('cable-rise',(28, 32),(28, 34))
        self.add_arc('cable-bend',(28, 34),(18, 44),radius_x=10,radius_y=10,sweep=True)
        self.add_line('cable-tip',(18, 44),(8, 44))
        self.add_contour('cable','cable-rise','cable-bend','cable-tip',closed=False)
        self.relate('connect','tip','body')
        self.relate('connect','body','cable')
