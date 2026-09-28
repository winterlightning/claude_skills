"""A happy emoji holds a pizza slice. SQUARE 6,6–42,42. Repair existing draft: curved pizza base and a rounded supporting hand restore the held-food scene. Equal closed-eye arcs convey happiness; omit the mouth and crust band for clearance. Source supplies closed eyes and hand; no useful exact local Lucide smile reference was available."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ebd59bc7-f7b1-408d-92b4-1e3c198ffc2c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji food eating lover hug_ebd59bc7-f7b1-408d-92b4-1e3c198ffc2c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-face-holding-pizza-slice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Happy Emoji Eating Pizza Slice',)
    keywords = ('happy', 'emoji', 'eating', 'pizza', 'slice')
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
        path("face",(6,24),[("C",(24,6),(6,10),(11,6)),("C",(42,24),(37,6),(42,10))])
        for i,x in enumerate((18,30)):self.add_arc(f"eye-{i}",(x-2,18),(x+2,18),radius_x=2,sweep=True)
        path("pizza",(14,32),[("L",(33,28)),("L",(29,42)),("C",(14,32),(23,42),(17,36))],True)
        path("hand",(14,32),[("C",(6,36),(10,30),(6,32)),("C",(14,42),(6,40),(10,42)),("L",(20,42))])
        self.relate("connect","hand","pizza")

