"""Kitchen Shelves with Dishes and Utensils.

Two kitchen shelves with an upper bowl, lower bowl and mug, and three hanging utensils. Centerline extremes (6,6)-(42,42). No close local Lucide scene match. Use single outlined dishes and three simple utensil stems; omit the mug handle and detailed utensil heads.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2b52bdd-0bae-4bae-87de-c37eb95059a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/kitchen shelf_a2b52bdd-0bae-4bae-87de-c37eb95059a1.svg'
AUTHOR = 'gpt-6'

class KitchenShelvesBowlsMugUtensils(Solo48):
    icon_id = 'kitchen-shelves-bowls-mug-utensils'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('kitchen', 'shelves', 'with', 'dishes', 'and', 'utensils')

    def build(self):
        # Symbol plan: Two kitchen shelves with an upper bowl, lower bowl and mug, and three hanging utensils. Centerline extremes (6,6)-(42,42). No close local Lucide scene match. Use single outlined dishes and three simple utensil stems; omit the mug handle and detailed utensil heads.

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

        self.add_polyline('upper',(6,14),(14,14),(24,14),(42,14))
        path('upper-bowl',(10,6),[('L',(28,6)),('C',(24,14),(28,11),(27,14)),('L',(14,14)),('C',(10,6),(11,14),(10,11))],True);join('upper-bowl','upper')
        self.add_polyline('lower',(6,30),(14,30),(18,30),(24,30),(30,30),(34,30),(38,30),(42,30))
        path('lower-bowl',(6,22),[('L',(22,22)),('C',(18,30),(22,27),(21,30)),('L',(14,30)),('C',(6,22),(9,30),(6,27))],True);join('lower-bowl','lower')
        self.add_polyline('mug',(30,30),(30,22),(38,22),(38,30));join('mug','lower')
        for i,x in enumerate((14,24,34)):line(f'utensil-{i}',(x,30),(x,42));join(f'utensil-{i}','lower')
