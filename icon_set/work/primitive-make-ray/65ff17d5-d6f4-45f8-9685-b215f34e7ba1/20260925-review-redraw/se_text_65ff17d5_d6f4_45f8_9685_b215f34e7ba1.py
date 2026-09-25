'se (text). S and E now share cap-height and baseline, correcting the smaller floating S. S curves join coherently, E retains a shortened middle arm. Construction reference: local Lucide type.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '65ff17d5-d6f4-45f8-9685-b215f34e7ba1'
SOURCE_PATH = 'pictographic-primitives/symbol/se (text)_65ff17d5-d6f4-45f8-9685-b215f34e7ba1.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/se_text_65ff17d5_d6f4_45f8_9685_b215f34e7ba1.py'
class Drawing(Solo48):
    icon_id = 'se-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('se (text)',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        # Equal cap-height lettering, coherent S with horizontal tangents.
        self.path('s',(18,14),[('C',(11,8),(17,10),(14,8)),('C',(4,16),(7,8),(4,11)),('C',(11,24),(4,21),(8,23)),('C',(18,32),(15,25),(18,27)),('C',(11,40),(18,37),(15,40)),('C',(4,34),(8,40),(5,38))])
        self.add_polyline('e',(44,8),(28,8),(28,24),(28,40),(44,40))
        self.add_line('e-middle',(28,24),(40,24));self.relate('connect','e','e-middle')
