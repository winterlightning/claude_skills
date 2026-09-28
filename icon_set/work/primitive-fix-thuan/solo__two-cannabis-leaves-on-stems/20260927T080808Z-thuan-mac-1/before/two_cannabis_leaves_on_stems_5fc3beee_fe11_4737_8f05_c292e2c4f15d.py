"""Two Cannabis Leaves on Stems.

Plan: SQUARE centerlines (6,6)-(42,42); two staggered leaf fans on slender curved stems. Five radiating leaflet veins retain the smaller lower-left and higher right arrangement.
Construction references: Lucide cannabis: pointed fan silhouette and descending stem.
Reduction: Reduced each small leaf to five radiating leaflet veins; omitted closed outlines and the two smallest lobes to keep the two-leaf botanical subject clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5fc3beee-fe11-4737-8f05-c292e2c4f15d'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis tree_5fc3beee-fe11-4737-8f05-c292e2c4f15d.svg'
SOURCE_ICON_IDS = ('5fc3beee-fe11-4737-8f05-c292e2c4f15d',)
SOURCE_PATHS = ('pictographic-primitives/cannabis/cannabis tree_5fc3beee-fe11-4737-8f05-c292e2c4f15d.svg',)
AUTHOR = 'gpt-6'


class TwoCannabisLeavesOnStems(Solo48):
    icon_id = 'two-cannabis-leaves-on-stems'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'cannabis'
    categories = ('primitives', 'cannabis')
    aliases = ()
    keywords = ('two', 'cannabis', 'leaves', 'on', 'stems')

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

        # Five vein strokes form each small leaf fan without cramped inner pockets.
        for name,cx,base,tips in [("left",15,36,[(15,24),(6,28),(6,36),(24,28),(24,36)]),("right",33,20,[(33,6),(24,10),(24,20),(42,10),(42,20)])]:
            for i,tip in enumerate(tips):
                self.add_line(f"{name}-leaflet-{i}",(cx,base),tip)
                for j in range(i):self.relate("connect",f"{name}-leaflet-{i}",f"{name}-leaflet-{j}")
            path(name+"-stem",(cx,base),[("C",(cx+2,42),(cx,base+2),(cx+2,40))])
            for i in range(5):self.relate("connect",name+"-stem",f"{name}-leaflet-{i}")
