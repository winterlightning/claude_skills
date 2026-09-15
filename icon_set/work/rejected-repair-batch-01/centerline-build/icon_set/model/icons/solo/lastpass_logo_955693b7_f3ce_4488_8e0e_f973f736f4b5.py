"""Three small rings sit in a row followed by a tall rounded vertical bar, like a masked password with a cursor.

Symbol plan: Three repeated circular password marks followed by one cursor. Extremes (4,8)-(44,40).
Review notes: Lucide circle informs exact paired semicircles. Cursor outline becomes one stroke; all three password rings retained. The tall cursor sets the prescribed envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '955693b7-f3ce-4488-8e0e-f973f736f4b5'
SOURCE_PATH = 'pictographic-primitives/logos/lastpass logo_955693b7-f3ce-4488-8e0e-f973f736f4b5.svg'
AUTHOR = 'gpt-6'

class LastpassLogo(Solo48):
    icon_id = 'lastpass-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('lastpass', 'password-manager', 'security', 'dots', 'logo', 'brand', 'login')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        for i in range(3):ring(f'password-{i}',6+i*12,24,2)
        self.add_line('cursor',(44,8),(44,40))
