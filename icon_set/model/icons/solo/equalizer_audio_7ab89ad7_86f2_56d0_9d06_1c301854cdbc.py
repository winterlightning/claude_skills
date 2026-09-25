"""equalizer-audio: Three equally sized circular controls on perfectly straight columns; same radius and shared cardinal joins.
Lucide construction: sliders-vertical; original and atomic-debug inspected.
Omissions: None
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7ab89ad7-86f2-56d0-9d06-1c301854cdbc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__equalizer-audio/20260924T165054Z-thuan-mac/reference/equalizer_7ab89ad7-86f2-56d0-9d06-1c301854cdbc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'equalizer-audio-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('equalizer', 'audio')
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

        for name,x,y in [('left',8,22),('middle',24,32),('right',40,16)]:
            oval(name,x,y,4,4)
            line(name+'-top',(x,8),(x,y-4));line(name+'-bottom',(x,y+4),(x,40))
            join(name,name+'-top');join(name,name+'-bottom')
