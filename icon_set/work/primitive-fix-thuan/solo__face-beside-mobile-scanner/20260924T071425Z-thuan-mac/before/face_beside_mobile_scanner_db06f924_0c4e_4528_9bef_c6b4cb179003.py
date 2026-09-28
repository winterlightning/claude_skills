"""Mobile Face Recognition Scan.

Side face profile beside an upright phone for face recognition. Centerline extremes (4,8)-(44,40). Human reference user.svg informs a smooth uncluttered head; source profile nose and continuous neck retained, with no separate torso or detached head gap. Lucide smartphone informs rounded housing and low screen divider. Omit the small eye line.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db06f924-0c4e-4528-9bef-c6b4cb179003'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/fashion design shoes_db06f924-0c4e-4528-9bef-c6b4cb179003.svg'
AUTHOR = 'gpt-6'

class FaceBesideMobileScanner(Solo48):
    icon_id = 'face-beside-mobile-scanner'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    aliases = ()
    keywords = ('mobile', 'face', 'recognition', 'scan')

    def build(self):
        # Symbol plan: Side face profile beside an upright phone for face recognition. Centerline extremes (4,8)-(44,40). Human reference user.svg informs a smooth uncluttered head; source profile nose and continuous neck retained, with no separate torso or detached head gap. Lucide smartphone informs rounded housing and low screen divider. Omit the small eye line.

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

        path('face',(4,40),[('L',(4,8)),('C',(13,12),(8,8),(11,8)),('L',(20,21)),('C',(12,26),(18,23),(12,22)),('C',(20,31),(12,30),(16,31)),('L',(20,40)),('L',(4,40))],True)
        path('phone',(32,14),[('L',(40,14)),('A',(44,18),4,4,True),('L',(44,30)),('L',(44,36)),('A',(40,40),4,4,True),('L',(32,40)),('A',(28,36),4,4,True),('L',(28,30)),('L',(28,18)),('A',(32,14),4,4,True)],True)
        line('screen-bottom',(28,30),(44,30));join('screen-bottom','phone')
