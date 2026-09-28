"""An egg tied with a large bow. VRECT_L extremes 8,4–40,44, symmetric about x24. Source contributes shell and tied loops; Lucide egg informs the shell. Bow moved to top to retain readable loops. Omit band thickness, knot polygon and notched tails at native size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ec0f499f-1e04-4366-8584-5678287d169a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/easter egg ribbon_ec0f499f-1e04-4366-8584-5678287d169a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'easter-egg-wrapped-with-ribbon-bow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Easter Egg with Ribbon Bow',)
    keywords = ('easter', 'egg', 'with', 'ribbon', 'bow')
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
        axis=24
        def mirror(point):return (2*axis-point[0],point[1])
        lower_left=[("C",(8,31),(10,25),(8,28)),("C",(24,44),(8,39),(14,44))]
        lower_right=[("C",mirror((8,31)),mirror((14,44)),mirror((8,39))),
                     ("C",mirror((14,20)),mirror((8,28)),mirror((10,25)))]
        path("egg",(14,20),lower_left+lower_right)
        loop=[("C",(16,4),(22,9),(20,4)),("C",(8,10),(10,4),(8,6)),
              ("C",(14,20),(8,16),(10,20)),("C",(24,16),(18,20),(22,18))]
        mirrored=[(kind,mirror(end),mirror(c1),mirror(c2)) for kind,end,c1,c2 in loop]
        path("bow",(axis,16),loop+mirrored,True)
        self.relate("connect","egg","bow")
