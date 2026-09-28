"""An open padlock with a thick ring body and a small ring at its centre, its tall shackle raised and swung open at the left.

Symbol plan: Open shackle above a broad ring body with central hole; extremes (8,4)-(40,44).
Review notes: Keeps open shackle and central ring. Body becomes slightly wider than circular to fit the tall shackle. Earlier circle construction informs the keyhole; the right side truly attaches to the body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '076d2fbc-9ca3-4943-8e51-d01ba5c49ac2'
SOURCE_PATH = 'pictographic-primitives/logos/open access logo_076d2fbc-9ca3-4943-8e51-d01ba5c49ac2.svg'
AUTHOR = 'gpt-6'

class OpenAccessLogo(Solo48):
    icon_id = 'open-access-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('open-access', 'padlock', 'unlocked', 'research', 'logo', 'brand', 'open')

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
        self.add_arc('body-top',(8,32),(40,32),radius_x=16,radius_y=12)
        self.add_arc('body-bottom',(40,32),(8,32),radius_x=16,radius_y=12)
        self.add_contour('body','body-top','body-bottom',closed=True)
        ring('keyhole',24,32,3)
        self.add_arc('shackle',(16,16),(40,16),radius_x=12)
        self.add_line('shackle-side',(40,16),(40,32));self.add_contour('open-shackle','shackle','shackle-side')
        for b in ['body-top','body-bottom']:self.relate('connect','shackle-side',b)
