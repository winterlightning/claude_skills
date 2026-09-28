from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4c642c9-6ad8-4f73-b9c5-8eaa2f4bc29e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/laboratory chromosome_f4c642c9-6ad8-4f73-b9c5-8eaa2f4bc29e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chromosome-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('chromosome', 'pair')

    def build(self):
        # Plan: Two unequal X chromosomes, big axis14 and small axis38; bounds (6,6)-(42,42). Paired arms share exact crossover. Reduce outlines to rounded strokes so paired identity survives. No exact Lucide match.
        self.add_polyline('large-a',(6,6),(14,24),(22,42))
        self.add_polyline('large-b',(22,6),(14,24),(6,42))
        self.relate('connect','large-a','large-b')
        self.add_polyline('small-a',(34,14),(38,24),(42,34))
        self.add_polyline('small-b',(42,14),(38,24),(34,34))
        self.relate('connect','small-a','small-b')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, command in enumerate(commands):
            tag=f"{name}-{i}"
            if len(command)==2:
                self.add_line(tag,start,command); start=command
            else:
                self.add_bezier(tag,start,command); start=command[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
