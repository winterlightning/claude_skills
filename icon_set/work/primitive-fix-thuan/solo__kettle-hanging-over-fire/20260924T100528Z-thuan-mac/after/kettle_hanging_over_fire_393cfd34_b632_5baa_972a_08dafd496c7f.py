"""Hanging kettle and three flame tips, VRECT_L centerlines (8,4)-(40,44). Restore arched handle, smooth the pot and use one coherent flame contour; shorten the suspension and omit its doubled hook."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '393cfd34-b632-5baa-972a-08dafd496c7f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kettle-hanging-over-fire/20260924T100528Z-thuan-mac/reference/asian interior boiler_393cfd34-b632-5baa-972a-08dafd496c7f.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'cooking-pot'
DESIGN_PLAN = 'Hanging kettle and three flame tips, VRECT_L centerlines (8,4)-(40,44). Restore arched handle, smooth the pot and use one coherent flame contour; shorten the suspension and omit its doubled hook.'
class Drawing(Solo48):
    icon_id = 'kettle-hanging-over-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kettle', 'hanging', 'over', 'fire')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)


    def build(self):
        self.add_line('hanger',(24,4),(24,10))
        self.path('handle',(16,18),[('A',(24,10),8,8,True),('A',(32,18),8,8,True)])
        self.relate('connect','hanger','handle')
        self.path('pot',(16,18),[('L',(32,18)),('L',(40,16)),('L',(36,26)),('C',(28,30),(35,30),(32,30)),('L',(16,30)),('C',(8,26),(10,30),(8,29)),('C',(16,18),(8,22),(13,18))],True)
        self.relate('connect','pot','handle')
        self.add_polyline('fire',(12,44),(12,38),(18,42),(24,38),(30,42),(36,38),(36,44))
