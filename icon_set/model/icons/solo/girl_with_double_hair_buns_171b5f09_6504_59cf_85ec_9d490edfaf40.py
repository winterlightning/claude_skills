"""Girl with Double Hair Buns.

Plan: Circular jaw center24,21 radius11; shoulder apex36, exact 4 centerline head/body contact. Mirrored side buns and center parted hair. Bounds (6,6)-(42,42).
Construction: human_ref/user.svg circular jaw and curved shoulders; source double buns and parted fringe.
Reduction: Omitted small ears and face details.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '171b5f09-6504-59cf-85ec-9d490edfaf40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/chinese kid girl_171b5f09-6504-59cf-85ec-9d490edfaf40.svg'
AUTHOR = 'gpt-6'


class GirlWithDoubleHairBuns(Solo48):
    icon_id = 'girl-with-double-hair-buns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('girl', 'with', 'double', 'hair', 'buns')
    human_construction = "bust"

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
        path('face',(13,21),[('A',(24,32),11,11,False),('A',(35,21),11,11,False)])
        path('hair',(13,21),[('C',(16,11),(13,16),(14,12)),('C',(24,10),(18,10),(21,10)),('C',(32,11),(27,10),(30,10)),('C',(35,21),(34,12),(35,16)),('C',(24,14),(30,21),(26,18)),('C',(13,21),(22,18),(18,21))],True)
        self.relate('connect','hair','face')
        for side in [-1,1]:
         def p(x,y): return (24+side*x,y)
         path('bun-'+str(side),p(8,11),[('A',p(18,11),5,5,side==1),('C',p(11,21),p(18,17),p(16,20))])
         self.relate('connect','bun-'+str(side),'hair');self.relate('connect','bun-'+str(side),'face')
        path('shoulders',(6,42),[('A',(24,36),18,6,True),('A',(42,42),18,6,True)])
        self.relate('connect','face','shoulders')
