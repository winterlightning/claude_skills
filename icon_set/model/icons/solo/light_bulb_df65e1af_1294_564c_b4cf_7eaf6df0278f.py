"""Light Bulb reconstructed from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df65e1af-1294-564c-b4cf-7eaf6df0278f'
SOURCE_PATH = 'pictographic-primitives/lights/light bulb shine_df65e1af-1294-564c-b4cf-7eaf6df0278f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'light-bulb-df65e1af-1294-564c-b4cf-7eaf6df0278f'
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "lights"
    categories = ("lights", "primitives")
    aliases = ()
    keywords = ('bulb', 'light', 'lamp', 'electric', 'glass', 'base')
    keyshape = Keyshape.VRECT_L

    def build(self):
        # Plan: shared axis and mirrored tangent shoulder pairs. The head owns
        # radii, shoulder circles own a 3:4:5 transition, base owns its depth.
        # Lucide lightbulb informs the open glass, rounded shoulders and base.
        # Envelope: (8,4)..(40,44) on centerlines.
        axis = 24
        rx, ry, cy, shoulder_r, base_depth = (16, 16, 20, 10, 8)
        offset = shoulder_r * 2 // 5
        step = shoulder_r * 4 // 5
        neck = rx - 2 * offset
        seam_y = cy + 2 * step
        self.add_arc("head",(axis-rx,cy),(axis+rx,cy),radius_x=rx,radius_y=ry)
        for side, sign in (("right",1),("left",-1)):
            a=(axis+sign*rx,cy)
            b=(axis+sign*(rx-offset),cy+step)
            c=(axis+sign*neck,seam_y)
            if sign==1:
                self.add_arc(side+"-shoulder",a,b,radius_x=shoulder_r)
                self.add_arc(side+"-neck",b,c,radius_x=shoulder_r,sweep=False)
            else:
                self.add_arc(side+"-neck",c,b,radius_x=shoulder_r,sweep=False)
                self.add_arc(side+"-shoulder",b,a,radius_x=shoulder_r)
        self.add_arc("base",(axis+neck,seam_y),(axis-neck,seam_y),radius_x=neck,radius_y=base_depth)
        self.add_contour("outline","head","right-shoulder","right-neck","base","left-neck","left-shoulder",closed=True)
        self.add_line("seam",(axis-neck,seam_y),(axis+neck,seam_y))
        self.relate("connect","outline","seam")
