"""An oval speech bubble with its tail at the lower left holds the word LINE in bold capitals.

Symbol plan: Left-tail bubble enclosing four line-built letters. Extremes (4,8)-(44,40).
Review notes: Full LINE spelling retained. Lucide message-circle informs the outline; no useful local wordmark match. Four-letter spacing cannot be sacrificed merely for a numeric pass.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c9dc674-34a7-47b7-96cb-bfd7ab11cb60'
SOURCE_PATH = 'pictographic-primitives/logos/line logo_9c9dc674-34a7-47b7-96cb-bfd7ab11cb60.svg'
AUTHOR = 'gpt-6'

class LineLogo(Solo48):
    icon_id = 'line-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('line', 'messenger', 'chat', 'speech-bubble', 'logo', 'brand', 'messaging')

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
        self.add_arc('bubble-top',(44,22),(4,22),radius_x=20,radius_y=14,sweep=False)
        self.add_arc('bubble-right',(4,22),(8,30),radius_x=10,sweep=False)
        chain('bubble-tail',(8,30),(6,40),(18,36),(30,36))
        self.add_arc('bubble-left',(30,36),(44,22),radius_x=14,sweep=False)
        self.add_contour('bubble','bubble-top','bubble-right','bubble-tail-1','bubble-tail-2','bubble-tail-3','bubble-left',closed=True)

        self.add_polyline('letter-l',(11,18),(11,28),(16,28))
        self.add_line('letter-i',(21,18),(21,28))
        self.add_polyline('letter-n',(26,28),(26,18),(32,28),(32,18))
        self.add_polyline('letter-e',(41,18),(37,18),(37,28),(41,28))
        self.add_line('e-middle',(37,23),(41,23))
