"""Whole Artichoke Vegetable.

Artichoke bud made from three overlapping pointed leaf groups and a short stem. Centerline extremes (8,4)-(40,44). Mirror all leaf geometry around x=24. Lucide leafy-green informs a single silhouette with restrained leaf divisions; reduce repeated tiers.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb684ff6-2756-54a8-a7a7-d29ab1ed3a1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/artichoke_fb684ff6-2756-54a8-a7a7-d29ab1ed3a1c.svg'
AUTHOR = 'gpt-6'

class ArtichokeLayeredLeaves(Solo48):
    icon_id = 'artichoke-layered-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('whole', 'artichoke', 'vegetable')

    def build(self):
        # Symbol plan: Artichoke bud made from three overlapping pointed leaf groups and a short stem. Centerline extremes (8,4)-(40,44). Mirror all leaf geometry around x=24. Lucide leafy-green informs a single silhouette with restrained leaf divisions; reduce repeated tiers.

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

        bilateral('bud',(24,4),[('L',(32,12)),('L',(40,20)),('C',(28,36),(40,30),(36,36)),('L',(24,36))])
        bilateral('inner-leaf',(24,18),[('C',(32,12),(26,16),(30,15))],False);join('inner-leaf','bud')
        bilateral('outer-leaves',(24,36),[('C',(40,20),(24,30),(32,22))],False);join('outer-leaves','bud')
        self.add_polyline('stem',(20,36),(20,44),(28,44),(28,36));join('stem','bud');join('stem','outer-leaves')
