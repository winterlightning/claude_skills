"""Five Star Rating Ring.

Plan: Five repeated five-ray stars surround an open center. Bounds (6,6)-(42,42).
Construction: Lucide star fivefold silhouette; supplied five-star circular rating composition.
Reduction: Open radial star strokes preserve all five stars without tiny enclosed holes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '73a68590-edb5-4416-8cc2-bfdb143a5feb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/rating five star_73a68590-edb5-4416-8cc2-bfdb143a5feb.svg'
AUTHOR = 'gpt-6'


class IconFiveStarRatingRing(Solo48):
    icon_id = 'five-star-rating-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('five', 'star', 'rating', 'ring')

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
        for j,(x,y) in enumerate([(24,10),(10,22),(38,22),(14,38),(34,38)]):
         points=[(x,y-4),(x+4,y-1),(x+3,y+4),(x-3,y+4),(x-4,y-1)]
         for k,p in enumerate(points):self.add_line(f'star{j}-{k}',(x,y),p)
         for a in range(5):
          for b in range(a+1,5):self.relate('connect',f'star{j}-{a}',f'star{j}-{b}')
