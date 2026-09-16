"""Mountain Summit with Pennant.

Plan: SQUARE centerlines (6,6)-(42,42); a tall mountain and smaller left peak share a baseline, with snow boundary and a physical flagpole at the summit. Asymmetry follows the source landscape.
Construction references: Lucide mountain-snow: coherent peak silhouette and attached snow boundary; Lucide flag inspected in batch03 for pole attachment.
Reduction: Simplified snow contour while retaining the folded rectangular flag or swallowtail pennant.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'c7be2aeb-b63e-4df6-8ee7-f6124673ad5b'
SOURCE_PATH = 'pictographic-primitives/business/climb top_c7be2aeb-b63e-4df6-8ee7-f6124673ad5b.svg'
SOURCE_ICON_IDS = ('c7be2aeb-b63e-4df6-8ee7-f6124673ad5b',)
SOURCE_PATHS = ('pictographic-primitives/business/climb top_c7be2aeb-b63e-4df6-8ee7-f6124673ad5b.svg',)
AUTHOR = 'gpt-6'


class MountainSummitWithPennant(Solo48):
    icon_id = 'mountain-summit-with-pennant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('mountain', 'summit', 'with', 'pennant')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        self.add_polyline("mountain",(16,42),(19,36),(21,32),(26,22),(34,32),(42,42),closed=True)
        self.add_polyline("small-peak",(16,42),(6,42),(10,30),(19,36))
        self.relate("connect","mountain","small-peak")
        self.add_polyline("pole",(26,22),(26,14),(26,6))
        self.relate("connect","pole","mountain")

        self.add_polyline("flag",(26,6),(40,6),(36,10),(40,14),(26,14))
        path("snow",(21,32),[("C",(34,32),(25,29),(29,35))])

        self.relate("connect","flag","pole")
        self.relate("connect","snow","mountain")
