"""Whole Onion Bulb.

Onion bulb with three sprouting tips and one continuous central layer. Centerline extremes (8,4)-(40,44). Body is mirrored about x=24; the shoots share an exact junction. Lucide sprout informs the stem junction, apple the coherent body outline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c78b8def-1b7f-4ffe-9d6a-207e5edd5ad8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__onion-bulb-vertical-layers/20260927T133654Z-thuan-mac-1/reference/onion_c78b8def-1b7f-4ffe-9d6a-207e5edd5ad8.svg'
AUTHOR = "gpt-6"

class OnionBulbVerticalLayers(Solo48):
    icon_id = 'onion-bulb-vertical-layers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'onion', 'bulb')

    def build(self):
        # Symbol plan: Onion bulb with three sprouting tips and two vertical layer marks. Centerline extremes (8,4)-(40,44). Body is mirrored about x=24; the shoots share an exact junction. Lucide sprout informs the stem junction, apple the coherent body outline.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        bilateral('bulb',(24,12),[('C',(40,30),(30,18),(40,20)),('C',(24,44),(40,39),(32,44))])
        for i,x in enumerate((16,24,32)):
            line(f'shoot-{i}',(24,12),(x,4));join(f'shoot-{i}','bulb')
        for a,b in ((0,1),(1,2),(0,2)): join(f'shoot-{a}',f'shoot-{b}')
        # A continuous centre layer restores the sliced-onion reading. The
        # side layers are kept in the outer silhouette at this stroke weight.
        line('central-layer',(24,12),(24,44))
        join('central-layer','bulb')
