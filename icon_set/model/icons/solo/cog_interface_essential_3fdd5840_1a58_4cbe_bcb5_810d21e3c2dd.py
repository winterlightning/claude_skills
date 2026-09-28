'Enlarged the hub from radius3 to5 and widened the root recesses to preserve clearance. Six deliberate teeth and paired notches mirror across both axes. SQUARE preserves a balanced gear; no parts omitted. Construction references: settings (repeated teeth and centered hub).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd'
SOURCE_PATH='pictographic-primitives/interface-essential/cog_3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/cog_interface_essential_3fdd5840_1a58_4cbe_bcb5_810d21e3c2dd.py'
class Drawing(Solo48):
    icon_id='cog-interface-essential'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases=()
    keywords=('cog',)

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
        # Six repeated teeth and root recesses mirror around both axes.
        self.add_polyline('gear',(20,6),(28,6),(31,12),(38,10),(42,18),(38,24),(42,30),(38,38),(31,36),(28,42),(20,42),(17,36),(10,38),(6,30),(10,24),(6,18),(10,10),(17,12),closed=True)
        self.circle('hub',24,24,5)

    icon_id = 'cog-interface-essential'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('cog', 'interface-essential')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
