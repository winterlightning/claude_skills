"""Kiwi bird with rounded body, small head, long downcurved beak and two feet. Lucide bird informs simple legs and smooth body. Omit tiny eye and lower beak outline; retain distinctive long bill and directional profile.
Keyshape HRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e7f198e2-850a-485d-8d8d-49ce1c496222'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_e7f198e2-850a-485d-8d8d-49ce1c496222.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='kiwi-bird'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases=()
    keywords=('kiwi', 'bird')

    def build(self):
        self.path('bird',(26,8),[('A',(34,16),8,8,True),('C',(28,26),(34,20),(28,20)),('C',(24,32),(28,29),(26,32)),('C',(16,32),(22,32),(18,32)),('C',(4,24),(8,32),(4,30)),('C',(18,14),(4,18),(10,14)),('C',(26,8),(22,14),(22,8))],True)
        self.add_bezier('beak',(34,16),((38,18),(42,23),(44,28)));self.relate('connect','bird','beak')
        self.add_polyline('left-foot',(16,32),(14,40),(8,40));self.relate('connect','bird','left-foot')
        self.add_polyline('right-foot',(24,32),(28,40),(34,40));self.relate('connect','bird','right-foot')

    def path(self,name,start,commands,closed=False):
        members=[];here=start
        for j,(kind,end,*args) in enumerate(commands):
            eid=f'{name}-{j}'
            if kind=='L':self.add_line(eid,here,end)
            elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
