"""fire-flower-batch-086: Symmetric oval flower head with two eyes, a central stem, and mirrored rounded leaves.
Lucide construction: flower-2; original and atomic-debug inspected.
Omissions: Inner face oval omitted to retain eye clearance. Leaves are open at their inner tips.
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bffa219-fc06-439d-b9cf-af6d7ca234cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/mario flower_9bffa219-fc06-439d-b9cf-af6d7ca234cc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fire-flower-batch-086'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('fire', 'flower', 'batch', '086')
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

        oval('head',24,15,16,11)
        line('eye-left',(20,13),(20,17));line('eye-right',(28,13),(28,17))
        line('stem',(24,26),(24,44));join('stem','head')
        path('leaves',(24,44),[('C',(8,34),(14,44),(8,40)),('L',(16,34))])
        path('leaves-right',(24,44),[('C',(40,34),(34,44),(40,40)),('L',(32,34))])
        join('stem','leaves');join('stem','leaves-right');join('leaves','leaves-right')
