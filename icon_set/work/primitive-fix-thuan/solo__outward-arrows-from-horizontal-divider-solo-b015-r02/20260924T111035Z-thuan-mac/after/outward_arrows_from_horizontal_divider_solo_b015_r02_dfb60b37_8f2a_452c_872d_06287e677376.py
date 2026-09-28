"""Shorten oversized chevrons, restore distinct shafts and maintain balanced clearance around the divider.
Construction: Lucide move-horizontal / move-vertical: 45-degree chevrons and separate straight shafts.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dfb60b37-8f2a-452c-872d-06287e677376'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__outward-arrows-from-horizontal-divider-solo-b015-r02/20260924T111035Z-thuan-mac/reference/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'outward-arrows-from-horizontal-divider-solo-b015-r02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('outward', 'arrows', 'from', 'horizontal', 'divider', 'solo', 'b015', 'r02')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        def point(x,y):return (y,x) if True else (x,y)
        line('divider',point(24,6),point(24,42))
        for side in (-1,1):
            tip=24+side*18; shoulder=24+side*10; inner=24+side*8
            name='left' if side==-1 else 'right'
            poly(name+'-head',point(shoulder,16),point(tip,24),point(shoulder,32))
            line(name+'-shaft',point(tip,24),point(inner,24));join(name+'-head',name+'-shaft')
