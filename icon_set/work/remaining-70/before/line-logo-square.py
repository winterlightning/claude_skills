"""A rounded square frame holds an oval speech bubble with its tail at the lower left, containing the word LINE in bold capitals.

Symbol plan: Rounded square enclosure, smaller left-tail bubble, full LINE lettering. Extremes (6,6)-(42,42).
Review notes: Preserves intrinsic square app-logo treatment from the supplied standalone triage. Lucide square and message-circle inform construction. Nested outline and wordmark are intentionally retained for honest fit findings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9faee9a3-8ed6-4e2b-ab14-22709bddb76d'
SOURCE_PATH = 'pictographic-primitives/logos/line logo 1_9faee9a3-8ed6-4e2b-ab14-22709bddb76d.svg'
AUTHOR = 'gpt-6'

class LineLogoSquare(Solo48):
    icon_id = 'line-logo-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('line', 'messenger', 'chat', 'speech-bubble', 'logo', 'brand', 'square')

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
        rounded('frame',6,6,42,42,6)
        self.add_arc('bubble-top',(12,24),(36,24),radius_x=12,radius_y=10)
        self.add_arc('bubble-bottom',(36,24),(22,34),radius_x=12,radius_y=10)
        chain('tail',(22,34),(15,37),(17,31))
        self.add_arc('bubble-left',(17,31),(12,24),radius_x=10)
        self.add_contour('bubble','bubble-top','bubble-bottom','tail-1','tail-2','bubble-left',closed=True)
        self.add_polyline('l',(17,21),(17,27),(20,27))
        self.add_line('i',(23,21),(23,27))
        self.add_polyline('n',(26,27),(26,21),(29,27),(29,21))
        self.add_polyline('e',(34,21),(32,21),(32,27),(34,27))
