"""Round-Bottom Flask.

Plan: VRECT centerlines (8,4)-(40,44); circular lower bowl of radius16, smooth curved shoulders, narrow straight neck and projecting lip. Symmetric around x24.
Construction references: Lucide flask-round: round bowl, straight neck and shared lip.
Reduction: Omitted the optional liquid line, absent from the supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '21d09b77-d7c9-47c0-ae18-a1a0e8f2931c'
SOURCE_PATH = 'pictographic-primitives/combination/bowl 1_21d09b77-d7c9-47c0-ae18-a1a0e8f2931c.svg'
SOURCE_ICON_IDS = ('21d09b77-d7c9-47c0-ae18-a1a0e8f2931c',)
SOURCE_PATHS = ('pictographic-primitives/combination/bowl 1_21d09b77-d7c9-47c0-ae18-a1a0e8f2931c.svg',)
AUTHOR = 'gpt-6'


class RoundBottomFlask(Solo48):
    icon_id = 'round-bottom-flask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'combination'
    aliases = ()
    keywords = ('round-bottom', 'flask')

    def build(self) -> None:
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

        self.add_polyline("lip",(16,4),(20,4),(28,4),(32,4))
        path("vessel",(20,4),[("L",(20,14)),("C",(8,28),(13,18),(8,20)),("A",(40,28),16,16,False),("C",(28,14),(40,20),(35,18)),("L",(28,4))])
        self.relate("connect","vessel","lip")
