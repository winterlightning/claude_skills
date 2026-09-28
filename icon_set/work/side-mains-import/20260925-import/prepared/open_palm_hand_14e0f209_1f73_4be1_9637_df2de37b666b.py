'hand. Longer finger creases restore finger-to-palm proportions. Thumb perimeter no longer crosses itself. Four fingertip widths share radius4 and pitch8. HRECT_L remains broader than the source because four finger widths and a thumb consume the 40-unit horizontal budget; thumb is more upright than the reference. Construction reference: local Lucide hand + human_ref/user.svg.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '14e0f209-1f73-4be1-9637-df2de37b666b'
SOURCE_PATH = 'pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/open_palm_hand_14e0f209_1f73_4be1_9637_df2de37b666b.py'
class Drawing(Solo48):
    icon_id = 'open-palm-hand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hand',)

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
        # Four long fingers share eight-unit widths; thumb is a separate lobe
        # in the perimeter, without the prior self-overlapping thumb loop.
        first=12;step=8;r=4;heights=(14,12,14,20)
        cmds=[]
        for i,y in enumerate(heights):
            x=first+i*step;cmds += [('L',(x,y)),('A',(x+step,y),r,r,True)]
        cmds += [('L',(44,28)),('A',(32,40),12,12,True),('L',(20,40)),('C',(4,32),(12,40),(4,38)),('L',(4,24)),('A',(12,24),4,4,True)]
        self.path('hand',(12,24),cmds,True)
        for i in range(3):
            x=first+(i+1)*step;y=max(heights[i],heights[i+1]);self.add_line(f'crease-{i}',(x,y),(x,29));self.relate('connect','hand',f'crease-{i}')

    icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b'
    category = 'holidays'
    aliases = ()
    keywords = ('open', 'palm', 'hand')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
