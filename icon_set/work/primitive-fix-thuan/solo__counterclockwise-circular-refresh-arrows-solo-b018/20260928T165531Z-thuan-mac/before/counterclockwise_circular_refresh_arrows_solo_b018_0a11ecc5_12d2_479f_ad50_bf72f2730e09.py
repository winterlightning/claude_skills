"""counterclockwise-circular-refresh-arrows-solo-b018: Two counterclockwise turns and balanced V heads are exact half-turn partners; coherent arcs replace awkward squared hooks.
Lucide construction: refresh-ccw; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-circular-refresh-arrows-solo-b018'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('counterclockwise', 'circular', 'refresh', 'arrows', 'solo', 'b018')
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

        for name,flip in [('upper',False),('lower',True)]:
            p=lambda x,y:(48-x,48-y) if flip else (x,y)
            path(name,p(36,12),[('C',p(24,6),p(33,8),p(29,6)),('A',p(12,24),12,18,False)])
            poly(name+'-head',p(6,18),p(12,24),p(18,18));join(name,name+'-head')
