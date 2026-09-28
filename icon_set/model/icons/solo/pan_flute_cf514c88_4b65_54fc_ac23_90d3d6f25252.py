"""Five adjoining pipes share walls and one binding line. Pipe bottoms descend in a 3-unit series; all widths are 8. Omit two pipes and the doubled binding band. Extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='cf514c88-4b65-54fc-ac23-90d3d6f25252'
SOURCE_PATH='pictographic-primitives/music/pan flute_cf514c88-4b65-54fc-ac23-90d3d6f25252.svg'
AUTHOR='gpt-6'

class PanFlute(Solo48):
    icon_id='pan-flute'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('pan-flute', 'panpipes', 'wind', 'instrument', 'folk', 'music', 'pipes')

    def build(self):
        self.add_polyline('top',(4,8),(12,8),(20,8),(28,8),(36,8),(44,8))
        self.add_polyline('right',(44,8),(44,16),(44,24))
        parts=[*[f'top-{n}' for n in range(1,6)],'right-1','right-2']
        for n,x in enumerate((44,36,28,20,12)):
            y=24+3*n
            self.add_arc(f'pipe-bottom-{n}',(x,y),(x-8,y),radius_x=4)
            parts.append(f'pipe-bottom-{n}')
            if n<4:
                self.add_line(f'step-{n}',(x-8,y),(x-8,y+3))
                parts.append(f'step-{n}')
        self.add_line('left-low',(4,36),(4,16))
        self.add_line('left-high',(4,16),(4,8))
        parts+=['left-low','left-high']
        # Each primitive belongs to only one paint contour.
        self.contours=[]
        self.add_contour('outline',*parts,closed=True)
        for n,x in enumerate((12,20,28,36)):
            bottom=33-3*n
            self.add_polyline(f'wall-{n}',(x,8),(x,16),(x,bottom))
            self.relate('connect',f'wall-{n}','outline')
        self.add_polyline('binding',(4,16),(12,16),(20,16),(28,16),(36,16),(44,16))
        self.relate('connect','binding','outline')
        for n in range(4):self.relate('connect','binding',f'wall-{n}')
