"""chess-rook-batch-013-07: A symmetric rook has three clean battlement strokes, a tapered upright tower and a rounded pedestal. Equal radii and shared attachment nodes keep the crown and base aligned.
Lucide construction: chess-rook; original and atomic-debug inspected.
Omissions: Battlement edges reduced to three open prongs so the tower keeps its upright proportions.
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c9ab4cd-f530-5fb6-841e-6491bc34bc58'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess rook_1c9ab4cd-f530-5fb6-841e-6491bc34bc58.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'chess-rook-batch-013-07'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('chess', 'rook', 'batch', '013', '07')
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

        path('crown',(8,4),[('L',(8,12)),('L',(8,16)),('A',(12,20),4,4,False),('L',(16,20)),('L',(32,20)),('L',(36,20)),('A',(40,16),4,4,False),('L',(40,12)),('L',(40,4))])
        poly('rim',(8,12),(24,12),(40,12));line('center-tooth',(24,4),(24,12));join('rim','crown');join('center-tooth','rim')
        line('tower-left',(16,20),(14,36));line('tower-right',(32,20),(34,36));join('tower-left','crown');join('tower-right','crown')
        path('base',(12,36),[('L',(14,36)),('L',(34,36)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True)],True)
        join('tower-left','base');join('tower-right','base')
