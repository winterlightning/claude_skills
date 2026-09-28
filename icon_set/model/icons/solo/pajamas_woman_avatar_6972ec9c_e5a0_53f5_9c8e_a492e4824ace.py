"""A center-parted bob with a circular jaw above a rounded pajama top and one clear button.
References: Human user.svg and supplied bob/pajama top.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6972ec9c-e5a0-53f5-9c8e-a492e4824ace'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avatar-pajamas-woman/20260926T085631Z-thuan-mac/reference/avatar pajamas woman_6972ec9c-e5a0-53f5-9c8e-a492e4824ace.svg'
AUTHOR = "claude-opus-5-5"

class AvatarPajamasWoman(Solo48):
    icon_id = 'pajamas-woman-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'pajamas', 'woman')

    def build(self):
        # Symbol plan: A center-parted bob with a circular jaw above a rounded pajama top and one clear button.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('hair',(8,26),[('L',(8,16)),('A',(24,4),16,12,True),('A',(40,16),16,12,True),('L',(40,26))])
        path('fringe',(16,16),[('C',(24,8),(20,16),(24,12)),('C',(32,16),(24,12),(28,16))])
        self.add_arc('face',(32,16),(16,16),radius_x=8);join('face','fringe')
        # Fringe meets the crown at an actual common point through this short part line.
        line('part',(24,4),(24,8));join('part','hair');join('part','fringe')
        bottom=24

        top=bottom+4
        # Review: curved body + V neck. Shoulders are quarter ellipses (rx10, ry16)
        # rising from the open bottom to the collar corners; the top edge meets the
        # jaw (avatar contact, 4 on centerlines) and a V collar hangs from the
        # collar corners to (24,38); the button is dropped to keep the V open.
        self.add_arc('body-left', (8, 44), (18, top), radius_x=10, radius_y=44 - top, sweep=True)
        line('body-top', (18, top), (24, top))
        line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right', (30, top), (40, 44), radius_x=10, radius_y=44 - top, sweep=True)
        self.add_contour('body', 'body-left', 'body-top', 'body-top-right', 'body-right')
        join('face','body')
        path('collar',(18,top),[('L',(24,38)),('L',(30,top))])
        join('collar','body')
