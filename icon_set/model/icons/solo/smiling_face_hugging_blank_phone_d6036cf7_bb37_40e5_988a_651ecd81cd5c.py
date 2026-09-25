"""A happy round emoji holds a blank upright phone against its lower left. Square 6,6–42,42. Source supplies hugging gesture, blank device and closed eyes. No local Lucide smile atomic reference was available. Paired eyes are reduced to round dots; one continuous cheek-hand contour owns the hug. Omit screen controls and simplify device tilt."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6036cf7-bb37-40e5-988a-651ecd81cd5c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji gaming lover hug iphone_d6036cf7-bb37-40e5-988a-651ecd81cd5c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-face-hugging-blank-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Emoji Hugging Smartphone',)
    keywords = ('emoji', 'hugging', 'smartphone')
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
        path("face-hand",(8,16),[("C",(24,6),(11,9),(17,6)),("C",(42,24),(34,6),(42,14)),("C",(30,42),(42,34),(38,42)),("L",(24,42)),("C",(18,38),(20,42),(18,41)),("C",(26,34),(18,34),(22,34))])
        self.add_polyline("phone",(6,24),(18,24),(18,38),(18,42),(6,42),closed=True)
        self.relate("connect","phone","face-hand")
        for i,x in enumerate((20,30)):
            self.add_dot(f"eye-{i}",(x,16))
        path("smile",(27,25),[("C",(33,24),(29,27),(31,27))])

