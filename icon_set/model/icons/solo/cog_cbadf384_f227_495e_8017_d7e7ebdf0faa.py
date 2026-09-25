"""cog-cbadf384: Six-tooth cog with mirrored curved roots and rounded tooth corners; central circular hole is enlarged and centered.
Lucide construction: settings; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cbadf384-f227-495e-8017-d7e7ebdf0faa'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_cbadf384-f227-495e-8017-d7e7ebdf0faa.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cog-cbadf384'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'cbadf384')
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

        # One right half is mirrored to form the left half. Each smooth junction shares a tangent.
        right=[('L',(26,6)),('C',(29,11),(28,6),(28,9)),('C',(34,13),(30,13),(32,14)),('L',(38,11)),('C',(40,12),(39,10),(40,11)),('L',(42,18)),('C',(40,21),(42,19),(41,20)),('C',(40,27),(38,23),(38,25)),('C',(42,30),(41,28),(42,29)),('L',(40,36)),('C',(38,37),(40,37),(39,38)),('L',(34,35)),('C',(29,37),(32,34),(30,35)),('C',(26,42),(28,39),(28,42)),('L',(24,42))]
        # Explicit reverse traversal mirrors endpoints and reverses each cubic's controls.
        points=[(24,6)]+[c[1] for c in right]
        commands=list(right)
        for i in range(len(right)-1,-1,-1):
            kind,end,*args=right[i];target=(48-points[i][0],points[i][1])
            if kind=='L':commands.append(('L',target))
            else:commands.append(('C',target,(48-args[1][0],args[1][1]),(48-args[0][0],args[0][1])))
        path('gear',(24,6),commands,True)
        oval('hole',24,24,4,4)
