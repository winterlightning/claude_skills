"""An Easter egg beside its diagonal paintbrush. Square bounds 6,6–42,42. Source supplies egg/brush arrangement. Lucide egg supplies coherent curved shell. Omit the decorative wave to preserve shell/brush clearance; simplify handle to a stroke and bristles to a pointed leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14ffe934-fb74-40f3-8849-221ae70a4c45'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/easter egg decoration_14ffe934-fb74-40f3-8849-221ae70a4c45.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'paintbrush-across-decorated-easter-egg'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Easter Egg and Paintbrush',)
    keywords = ('easter', 'egg', 'and', 'paintbrush')
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
        path("egg",(26,11),[("C",(20,6),(24,8),(23,6)),("C",(6,28),(12,6),(6,19)),("C",(20,42),(6,37),(11,42)),("C",(34,37),(27,42),(31,40))])
        path("brush",(28,22),[("C",(15,30),(19,20),(24,29)),("C",(28,22),(24,34),(30,30))],True)
        self.add_line("handle",(28,22),(42,6))
        self.relate("connect","handle","brush")
