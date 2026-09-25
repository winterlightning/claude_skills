"""Upper and Lower Teeth.

Plan: Two rows of broad teeth across an open gap. Three teeth per row replace four; remove doubled gum contours. Mirrored bands with shared thirds. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bac9175-ec81-4a3c-8737-7515abe0d327'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dentistry tooth jaws_6bac9175-ec81-4a3c-8737-7515abe0d327.svg'
AUTHOR = 'gpt-6'


class UpperAndLowerTeeth(Solo48):
    icon_id = 'upper-and-lower-teeth'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('upper', 'and', 'lower', 'teeth')

    def build(self):
        for p,y in [('upper',8),('lower',28)]:
            points=[(8,y),(16,y),(32,y),(40,y)]
            for j,(a,b) in enumerate(zip(points,points[1:])):
                self.add_line(p+f'-top-{j}',a,b)
            self.add_arc(p+'-tr',(40,y),(44,y+4),radius_x=4)
            self.add_line(p+'-right',(44,y+4),(44,y+8))
            self.add_arc(p+'-br',(44,y+8),(40,y+12),radius_x=4)
            points=[(40,y+12),(32,y+12),(16,y+12),(8,y+12)]
            for j,(a,b) in enumerate(zip(points,points[1:])):
                self.add_line(p+f'-bottom-{j}',a,b)
            self.add_arc(p+'-bl',(8,y+12),(4,y+8),radius_x=4)
            self.add_line(p+'-left',(4,y+8),(4,y+4))
            self.add_arc(p+'-tl',(4,y+4),(8,y),radius_x=4)
            self.add_contour(p,*[p+f'-top-{j}' for j in range(3)],p+'-tr',p+'-right',p+'-br',*[p+f'-bottom-{j}' for j in range(3)],p+'-bl',p+'-left',p+'-tl',closed=True)
            for j,x in enumerate([16,32]):
                self.add_line(p+f'-seam-{j}',(x,y),(x,y+12))
                self.relate('connect',p,p+f'-seam-{j}')
