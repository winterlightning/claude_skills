"""Bunk Bed with Ladder.

Plan: Two bed bands share upright posts; repeated pillow divisions and optional right ladder. Bounds (6,6)-(42,42).
Construction: Lucide bed and bed-double shared rail and post construction; source bunks.
Reduction: Single rail strokes replace mattress bands; pillows become vertical divisions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1c3bec99-fe86-528e-940a-70280b9299d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/hotel bunk bed_1c3bec99-fe86-528e-940a-70280b9299d2.svg'
AUTHOR = 'gpt-6'


class IconBunkBedWithLadder(Solo48):
    icon_id = 'bunk-bed-with-ladder'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('bunk', 'bed', 'with', 'ladder')

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
        for x in [6,42]:
         path('post'+str(x),(x,6),[('L',(x,14)),('L',(x,30)),('L',(x,42))])
        for y in [14,30]:
         path('bed'+str(y),(6,y),[('L',(16,y)),('L',(32,y)),('L',(42,y))]);self.relate('connect','bed'+str(y),'post6');self.relate('connect','bed'+str(y),'post42')
         path('pillow'+str(y),(6,y-8),[('L',(12,y-8)),('A',(16,y-4),4,4,True),('L',(16,y))]);self.relate('connect','pillow'+str(y),'post6');self.relate('connect','pillow'+str(y),'bed'+str(y))

        path('ladder',(32,14),[('L',(32,22)),('L',(32,30)),('L',(32,38)),('L',(32,42))])
        for y in [14,30]:self.relate('connect','ladder','bed'+str(y))
        for y in [22,38]:self.add_line('rung'+str(y),(32,y),(42,y));self.relate('connect','rung'+str(y),'ladder');self.relate('connect','rung'+str(y),'post42')
