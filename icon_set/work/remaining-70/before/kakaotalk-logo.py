"""An oval speech bubble with its tail at the lower left holds the word TALK in bold capitals.

Symbol plan: Oval left-tail bubble with intact TALK wordmark. Extremes (4,8)-(44,40).
Review notes: Lucide message-circle informs bubble contour; lettering retained rather than reducing to a generic bubble. This candidate documents the four-letter spacing conflict.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '341800d7-f244-43b8-9ffd-f5065af32434'
SOURCE_PATH = 'pictographic-primitives/logos/kakao talk logo_341800d7-f244-43b8-9ffd-f5065af32434.svg'
AUTHOR = 'gpt-6'

class KakaotalkLogo(Solo48):
    icon_id = 'kakaotalk-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('kakaotalk', 'kakao', 'chat', 'messenger', 'logo', 'brand', 'speech-bubble')

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

        self.add_polyline('t-top',(10,18),(13,18),(16,18))
        self.add_line('t-stem',(13,18),(13,28))
        self.relate('connect','t-stem','t-top-1');self.relate('connect','t-stem','t-top-2')
        self.add_polyline('a',(19,28),(23,18),(27,28))
        self.add_line('a-bar',(21,24),(25,24))
        self.add_polyline('l',(31,18),(31,28),(35,28))
        j=(39,23)
        self.add_polyline('k-stem',(39,18),j,(39,28))
        self.add_polyline('k-arms',(43,18),j,(43,28))
        for a in ['k-stem-1','k-stem-2']:
            for b in ['k-arms-1','k-arms-2']:self.relate('connect',a,b)
