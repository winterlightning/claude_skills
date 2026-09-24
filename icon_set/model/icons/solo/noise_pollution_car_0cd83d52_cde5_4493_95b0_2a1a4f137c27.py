"""A car beneath lightning and two noise marks.
Symbol plan and construction: car: coherent body silhouette and matched wheels.
Keyshape: HRECT_L gives the vehicle a broad lower band below the noise marks.
Omissions: Window divider, fine body rounding, and internal wheel/body seams.
Review: Wheel bulges are incorporated into one coherent car silhouette, eliminating the narrow fender pockets. The lightning is an open angular mark; side zigzags are reduced to chevrons. Vehicle and side marks are paired; lightning is deliberately directional."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0cd83d52-cde5-4493-95b0-2a1a4f137c27'
SOURCE_PATH = 'pictographic-primitives/ecology/noise pollution car_0cd83d52-cde5-4493-95b0-2a1a4f137c27.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='noise-pollution-car'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('noise', 'pollution', 'car')



    def build(self):
        # One car silhouette owns its rounded wheel bulges; wheel/body seams
        # are omitted so the fenders have no narrow enclosed pockets.
        self.add_polyline('bolt',(28,8),(18,14),(28,14),(26,18))
        self.add_polyline('noise-left',(6,8),(8,12),(6,16))
        self.add_polyline('noise-right',(42,8),(40,12),(42,16))
        self.add_polyline('body',(12,36),(4,36),(4,28),(12,28),(18,26),(30,26),(36,28),(44,28),(44,36),(36,36))
        self.add_arc('wheel-right',(36,36),(28,36),radius_x=4)
        self.add_line('chassis',(28,36),(20,36))
        self.add_arc('wheel-left',(20,36),(12,36),radius_x=4)
        self.add_contour('car',*(f'body-{j}' for j in range(1,10)),'wheel-right','chassis','wheel-left',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='body']
