"""educative-toys-music: Two equal circular notes share vertical stems and two precisely parallel beams; equal radii replace traced ovals.
Lucide construction: music; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '433f063c-05d3-5f02-8814-531a9ce81f5a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__educative-toys-music/20260924T165054Z-thuan-mac/reference/educative toys music_433f063c-05d3-5f02-8814-531a9ce81f5a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'educative-toys-music'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('educative', 'toys', 'music')
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

        oval('left-note',14,38,6,6);oval('right-note',34,32,6,6)
        path('beam',(20,38),[('L',(20,20)),('L',(20,10)),('L',(40,4)),('L',(40,14)),('L',(40,32))])
        line('lower-beam',(20,20),(40,14))
        join('left-note','beam');join('right-note','beam');join('lower-beam','beam')
