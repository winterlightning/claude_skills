"""Pear with a diagonal genetic mark and two crossing bars.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; coherent pear silhouette and repeated crossbars.
Omissions: Leaf omitted to preserve space for the identifying genetic mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a70afe46-73bf-42ff-8b39-ca8fceb14977'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/gmo food pear_a70afe46-73bf-42ff-8b39-ca8fceb14977.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='pear-with-two-crossbars-on-diagonal-mark'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases=()
    keywords=('pear', 'with', 'two', 'crossbars', 'on', 'diagonal', 'mark')

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
        # The pear owns symmetric shoulder transitions and two equal crossbars.
        self.path('pear',(24,8),[('A',(32,16),8,8,True),('A',(36,22),4,6,False),('A',(40,28),4,6,True),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('A',(12,22),4,6,True),('A',(16,16),4,6,False),('A',(24,8),8,8,True)],True)
        self.add_line('stem',(24,4),(24,8));self.relate('connect','stem','pear')
        self.add_polyline('mark',(21,27),(27,33))
        for i,(x,y) in enumerate([(21,27),(27,33)]):
            self.add_polyline('bar-'+str(i),(x-2,y+2),(x,y),(x+2,y-2));self.relate('connect','bar-'+str(i),'mark')
