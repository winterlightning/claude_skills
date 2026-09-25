"""Three equal outlined circles on one horizontal axis. CIRCLE radial envelope reaches x4 and44 without distorting the horizontal mark. Shared radius4, x centers8,24,40, y24. Source supplies hollow dots; Lucide ellipsis informs equal centers. No details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b9abab4b-6339-4d72-928b-1753794b5128'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/ellipsis_b9abab4b-6339-4d72-928b-1753794b5128.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'ellipsis-horizontal'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Three horizontal circles more options',)
    keywords = ('three', 'horizontal', 'circles', 'more', 'options')
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
        for i,x in enumerate((8,24,40)):circle(f"dot-{i}",x,24,4)

