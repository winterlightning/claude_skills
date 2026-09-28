"""Holly Leaves and Berries.

Plan: Two mirrored notched holly leaves over a three-berry cluster. Bounds (6,6)-(42,42).
Construction: Lucide leaf: coherent pointed leaf outline. Source provides notches and berries.
Reduction: Omitted veins and shallow notches to preserve broad pointed leaf openings; separated berries retain their count.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'b4a39a92-59f3-4333-bba3-da6c75735b50'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__holly-leaves-and-berries/20260927T151732Z-thuan-mac-1/reference/mistletoe_b4a39a92-59f3-4333-bba3-da6c75735b50.svg'
AUTHOR = 'gpt-6'


class IconHollyLeavesAndBerries(Solo48):
    icon_id = 'holly-leaves-and-berries'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('holly', 'leaves', 'and', 'berries')

    def build(self):

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
        # Wider paired leaves keep a holly silhouette without cramped tips.
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         path('leaf-'+str(side),p(18,6),[
             ('C',p(5,22),p(8,6),p(4,13)),
             ('C',p(18,6),p(15,22),p(18,14))],True)
        circle('berry-left',15,32,2);circle('berry-right',33,32,2);circle('berry-low',24,40,2)
