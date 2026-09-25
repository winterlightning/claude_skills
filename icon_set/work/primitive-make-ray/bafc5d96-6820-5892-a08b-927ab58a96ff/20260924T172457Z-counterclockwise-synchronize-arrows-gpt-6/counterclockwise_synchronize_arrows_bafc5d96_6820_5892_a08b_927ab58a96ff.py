"""counterclockwise-synchronize-arrows: Two counterclockwise turns and balanced V heads are exact half-turn partners; coherent arcs replace awkward squared hooks.
Lucide construction: refresh-ccw; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bafc5d96-6820-5892-a08b-927ab58a96ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__counterclockwise-synchronize-arrows/20260924T172457Z-thuan-mac/reference/synchronize arrows_bafc5d96-6820-5892-a08b-927ab58a96ff.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-synchronize-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('counterclockwise', 'synchronize', 'arrows')
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
