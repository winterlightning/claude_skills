"""Nursery Baby Crib Furniture.

Nursery crib with rounded upper rail, broad lower board, three slim bars and short feet. Centerline extremes (4,8)-(44,40). No close local Lucide crib match. Three equal bars share attachment nodes; remove duplicated rail thickness.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '572507c3-1e24-4ac8-827b-b1ba1082ddf5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/seeder_572507c3-1e24-4ac8-827b-b1ba1082ddf5.svg'
AUTHOR = 'gpt-6'

class NurseryCribVerticalRails(Solo48):
    icon_id = 'nursery-crib-vertical-rails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('nursery', 'baby', 'crib', 'furniture')

    def build(self):
        # Symbol plan: Nursery crib with rounded upper rail, broad lower board, three slim bars and short feet. Centerline extremes (4,8)-(44,40). No close local Lucide crib match. Three equal bars share attachment nodes; remove duplicated rail thickness.

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
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
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

        path('frame',(4,40),[('L',(4,32)),('L',(4,12)),('A',(8,8),4,4,True),('L',(14,8)),('L',(24,8)),('L',(34,8)),('L',(40,8)),('A',(44,12),4,4,True),('L',(44,32)),('L',(44,40))])
        self.add_polyline('lower',(4,32),(14,32),(24,32),(34,32),(44,32));join('lower','frame')
        for x in (14,24,34):line(f'bar-{x}',(x,8),(x,32));join(f'bar-{x}','frame');join(f'bar-{x}','lower')
