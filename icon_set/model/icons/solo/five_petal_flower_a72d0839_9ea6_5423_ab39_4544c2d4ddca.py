"""Five Petal Flower.

Plan: Five broad pointed lobes form one closed bloom, mirrored about x24; centerlines (6,6)-(42,42). A detached central disc.
Construction: Lucide flower: continuous petal silhouette and circular center; source supplies five pointed petals.
Reduction: Removed radial seams to preserve open petal interiors.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'a72d0839-9ea6-5423-ab39-4544c2d4ddca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas flower_a72d0839-9ea6-5423-ab39-4544c2d4ddca.svg'
AUTHOR = 'gpt-6'


class FivePetalFlower(Solo48):
    icon_id = 'five-petal-flower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('five', 'petal', 'flower')

    def build(self) -> None:

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('bloom',(24,6),[
         ('C',(32,18),(31,10),(32,12)),('C',(42,18),(36,15),(40,16)),
         ('C',(36,30),(42,25),(40,28)),('C',(36,42),(39,34),(38,39)),
         ('C',(24,36),(30,42),(27,40)),('C',(12,42),(21,40),(18,42)),
         ('C',(12,30),(10,39),(9,34)),('C',(6,18),(8,28),(6,25)),
         ('C',(16,18),(8,16),(12,15)),('C',(24,6),(16,12),(17,10))],True)
        circle('center',24,25,2)
