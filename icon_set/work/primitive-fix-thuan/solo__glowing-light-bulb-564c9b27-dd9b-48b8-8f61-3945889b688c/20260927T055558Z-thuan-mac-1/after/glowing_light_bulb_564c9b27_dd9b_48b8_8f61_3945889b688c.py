"""Glowing Light Bulb reconstructed from the supplied reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '564c9b27-dd9b-48b8-8f61-3945889b688c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c/20260927T055558Z-thuan-mac-1/reference/light bulb 1_564c9b27-dd9b-48b8-8f61-3945889b688c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c'
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "lights"
    categories = ("lights", "state")
    aliases = ()
    keywords = ('bulb', 'light', 'glowing', 'rays', 'lamp', 'electric')
    keyshape = Keyshape.SQUARE

    def build(self):
        # Plan: shared axis and mirrored tangent shoulder pairs. The head owns
        # radii, shoulder circles own a 3:4:5 transition, base owns its depth.
        # Lucide lightbulb informs the open glass, rounded shoulders and base.
        # Envelope: (6,6)..(42,42) on centerlines.
        axis = 24
        rx, ry, cy, shoulder_r, base_depth = (9, 9, 26, 5, 8)
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
        # Five short rays, paired positions reflected from the common axis.
        self.add_dot("ray-top",(axis,6))
        for side,sign in (("left",-1),("right",1)):
            self.add_dot("ray-"+side,(axis+sign*18,26))
            self.add_line("ray-upper-"+side,(axis+sign*14,10),(axis+sign*12,12))
