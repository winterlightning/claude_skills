"""A right-facing deer head with a long muzzle, pointed ear and branching antlers. VRECT_L 8,4–40,44. Natural asymmetry preserves the profile. Source supplies silhouette. No useful Lucide deer match. Omit the eye and small antler tines to protect open spaces."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5c7fb84-213d-4a0d-bc5e-256f8ca2072f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/elk_e5c7fb84-213d-4a0d-bc5e-256f8ca2072f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'deer-head-with-branching-antlers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Deer Head With Antlers',)
    keywords = ('deer', 'head', 'with', 'antlers')
    def build(self):
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
        path("head",(10,44),[("L",(18,28)),("C",(8,20),(11,28),(9,25)),("L",(16,20)),("C",(24,24),(20,20),(22,22)),("C",(32,25),(27,22),(29,23)),("L",(37,28)),("C",(40,32),(40,29),(40,29)),("C",(35,36),(40,35),(38,36)),("L",(29,36)),("C",(26,44),(26,36),(26,40))])
        self.add_polyline("antler-main",(12,4),(12,10),(24,12),(24,24))
        self.add_polyline("antler-fork",(24,12),(36,10),(36,4))
        self.relate("connect","antler-main","antler-fork")
        self.relate("connect","antler-main","head")

