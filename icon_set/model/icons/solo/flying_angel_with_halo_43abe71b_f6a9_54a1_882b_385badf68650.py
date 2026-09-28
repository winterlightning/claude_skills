"""Flying Angel with Halo.

Plan: Diagonal robe and pointed rear wing; head center (34,20), radius4; neck at (34,32) gives exact 4 ink gap. Halo across top. Bounds (6,6)-(42,42).
Construction: human_ref/full_body_ref.png: circular detached head and coherent body; source: robe, wing and halo. No useful Lucide angel match.
Reduction: Halo is a broad open arc; wing is a separate silhouette for clearance; no feathers or face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '43abe71b-f6a9-54a1-882b-385badf68650'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/angel_43abe71b-f6a9-54a1-882b-385badf68650.svg'
AUTHOR = 'gpt-6'


class FlyingAngelWithHalo(Solo48):
    icon_id = 'flying-angel-with-halo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('flying', 'angel', 'with', 'halo')

    def build(self) -> None:

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
        path('halo',(26,8),[('A',(42,8),8,2,True)])
        circle('head',34,20,4)
        path('robe',(34,32),[('C',(26,42),(34,37),(30,42)),('C',(6,32),(18,42),(10,38)),('L',(34,32))],True)
        path('wing',(6,6),[('C',(21,20),(12,13),(17,18)),('C',(6,6),(6,28),(6,18))],True)
