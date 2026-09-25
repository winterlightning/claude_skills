"""Shofar Horn with Sound.

Plan: Broad left bell and deep curved horn tapering toward right mouthpiece. Bounds (6,6)-(42,42).
Construction: Source horn; no useful exact local Lucide shofar match.
Reduction: Bell rim reduced to edge; two straight sound strokes replace three tiny waves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '4f082a54-6814-536d-bc23-2e2c1cc34d2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/rosh hashanah feast of trumpets_4f082a54-6814-536d-bc23-2e2c1cc34d2f.svg'
AUTHOR = 'gpt-6'


class IconShofarHornWithSound(Solo48):
    icon_id = 'shofar-horn-with-sound'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('shofar', 'horn', 'with', 'sound')

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
        path('horn',(6,14),[('L',(20,20)),('C',(32,24),(18,34),(25,34)),('L',(36,18)),('L',(42,24)),('C',(24,42),(35,36),(34,42)),('C',(6,14),(7,42),(6,28))],True)
        self.add_line('sound-a',(28,6),(27,10));self.add_line('sound-b',(42,6),(38,10))
