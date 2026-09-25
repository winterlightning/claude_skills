"""Symmetric pointed shield with concave top edges and long smooth sides.
Symbol plan: shared parameters and coherent contours.
Construction: shield: coherent symmetric outline.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ba7b0c51-fe87-48cd-a5c0-eea81086a3a9'
SOURCE_PATH = 'pictographic-primitives/protection/shield_ba7b0c51-fe87-48cd-a5c0-eea81086a3a9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='shield-ba7b0c51'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases=()
    keywords=('shield', 'ba7b0c51')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Shared axis x=24, mirrored circular sides; extremes (8,4)-(40,44).
        self.path('shield',(24,4),[('A',(40,12),40,40,False),('A',(24,44),40,40,True),('A',(8,12),40,40,True),('A',(24,4),40,40,False)],True)
