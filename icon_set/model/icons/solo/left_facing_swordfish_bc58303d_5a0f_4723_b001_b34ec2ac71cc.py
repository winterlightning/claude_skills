"""left-facing-swordfish: Long left-pointing bill, smooth swimming body, small swept fins and a crescent tail. Organic asymmetry preserves the reference.
Lucide construction: fish; original and atomic-debug inspected.
Omissions: Eye and fin seams omitted; bill, two fins and crescent tail retained.
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc58303d-5a0f-4723-b001-b34ec2ac71cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/swordfish_bc58303d-5a0f-4723-b001-b34ec2ac71cc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'left-facing-swordfish'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('left', 'facing', 'swordfish')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(12,24),[('C',(20,19),(15,21),(17,19)),('C',(26,8),(20,14),(23,10)),('C',(26,18),(25,12),(25,15)),('C',(36,21),(30,18),(33,20)),('C',(44,14),(38,17),(41,15)),('C',(44,36),(39,21),(39,29)),('C',(36,28),(41,34),(38,31)),('C',(24,30),(32,29),(28,30)),('C',(26,40),(24,34),(24,37)),('C',(19,30),(21,37),(19,34)),('C',(12,24),(16,29),(14,26))],True)
        line('bill',(4,24),(12,24));join('bill','body')
