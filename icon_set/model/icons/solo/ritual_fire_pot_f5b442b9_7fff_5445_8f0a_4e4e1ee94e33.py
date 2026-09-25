"""Ritual Fire Pot.

Plan: Deep bowl beneath tall flame; bilateral rim handles. Bounds (6,6)-(42,42).
Construction: Lucide flame sweeping tongue and cooking-pot rim/body attachments.
Reduction: Handles become outward rim extensions and inner flame is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'f5b442b9-7fff-5445-8f0a-4e4e1ee94e33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/bhogi_f5b442b9-7fff-5445-8f0a-4e4e1ee94e33.svg'
AUTHOR = 'gpt-6'


class IconRitualFirePot(Solo48):
    icon_id = 'ritual-fire-pot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('ritual', 'fire', 'pot')

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
        path('pot',(6,28),[('L',(10,28)),('L',(18,28)),('L',(30,28)),('L',(38,28)),('L',(42,28))])
        path('bowl',(10,28),[('A',(24,42),14,14,False),('A',(38,28),14,14,False)]);self.relate('connect','pot','bowl')
        path('flame',(18,28),[('C',(24,6),(17,20),(23,17)),('C',(30,28),(40,19),(32,24))]);self.relate('connect','flame','pot')
