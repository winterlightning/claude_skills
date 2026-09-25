"""Shabbat Candles and Open Book.

Plan: Mirrored open pages beneath two candle flames. Bounds (6,6)-(42,42).
Construction: Lucide book-open central spine and paired pages; source two candles.
Reduction: Candle bodies reduced to upright strokes, flames to small circular outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '3604fdc1-f4b2-4573-8df9-454296b27822'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/shabbat jewish the seventh day sabbath_3604fdc1-f4b2-4573-8df9-454296b27822.svg'
AUTHOR = 'gpt-6'


class IconShabbatCandlesAndOpenBook(Solo48):
    icon_id = 'shabbat-candles-and-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('shabbat', 'candles', 'and', 'open', 'book')

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
        path('book',(24,26),[('L',(6,22)),('L',(6,36)),('C',(24,42),(6,40),(18,40)),('C',(42,36),(30,40),(42,40)),('L',(42,22)),('L',(24,26))],True)
        self.add_line('spine',(24,26),(24,42));self.relate('connect','spine','book')
        for x in (14,34):
         circle('flame'+str(x),x,8,2)
         self.add_line('candle'+str(x),(x,18),(x,24));self.relate('connect','candle'+str(x),'book')
