"""Wine Glass and Matzah.

Plan: Stemmed wine glass left and tilted matzah sheet behind right. Bounds (6,6)-(42,42).
Construction: Lucide wine rounded bowl, stem and foot; supplied tilted bread sheet.
Reduction: Liquid level and matzah perforations omitted to preserve openings; tilted bread sheet remains behind stemmed glass.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5a8e99e3-f78c-4e3f-8e7f-585fa02af13f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/chag hamatzot feast of unleavened bread_5a8e99e3-f78c-4e3f-8e7f-585fa02af13f.svg'
AUTHOR = 'gpt-6'


class IconWineGlassAndMatzah(Solo48):
    icon_id = 'wine-glass-and-matzah'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('wine', 'glass', 'and', 'matzah')

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
        path('glass',(8,6),[('L',(20,6)),('L',(22,22)),('A',(14,30),8,8,True),('A',(6,22),8,8,True),('L',(8,6))],True)
        self.add_line('stem',(14,30),(14,42));self.relate('connect','stem','glass');path('foot',(6,42),[('L',(14,42)),('L',(22,42))]);self.relate('connect','stem','foot')
        path('matzah',(30,8),[('L',(42,14)),('L',(34,34)),('L',(22,28))]);self.relate('connect','matzah','glass')
        # Fine perforations removed for clearance.
