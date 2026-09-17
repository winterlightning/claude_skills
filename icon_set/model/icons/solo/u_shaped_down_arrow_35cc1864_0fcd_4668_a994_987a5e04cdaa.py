"""U-Shaped Down Arrow — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35cc1864-0fcd-4668-a994-987a5e04cdaa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation down 1_35cc1864-0fcd-4668-a994-987a5e04cdaa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'u-shaped-down-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('u', 'shaped', 'down', 'arrow')

    def build(self):
        # Plan: broad rounded U boundary, squared arm caps, inward descending V.
        # VRECT_L extremes8,4,40,44. Preserve the source's combined arrow silhouette.
        self.add_line('left-arm-1',(18,18),(18,4));self.add_line('left-arm-2',(18,4),(8,4));self.add_line('left-arm-3',(8,4),(8,28))
        self.add_arc('base',(8,28),(40,28),radius_x=16,sweep=False)
        self.add_line('right-arm-1',(40,28),(40,4));self.add_line('right-arm-2',(40,4),(30,4));self.add_line('right-arm-3',(30,4),(30,18))
        self.add_contour('u','left-arm-1','left-arm-2','left-arm-3','base','right-arm-1','right-arm-2','right-arm-3')
        self.add_polyline('head',(16,16),(18,18),(24,24),(30,18),(32,16));self.relate('connect','u','head')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

