"""A fire with a rising plume: one coherent flame outline and one separate smoke curve. The damaged source is a lone stroke; reconstruct the named subject.
References: Lucide flame and cloud: coherent curved silhouette; source is incomplete.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bab5b5ab-20b1-4dd5-9adc-c0506955e155'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/air pollution fire_bab5b5ab-20b1-4dd5-9adc-c0506955e155.svg'
AUTHOR = 'gpt-6'

class AirPollutionFireVariant2(Solo48):
    icon_id = 'air-pollution-fire-v2'
    variant_of = 'air-pollution-fire'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('air', 'pollution', 'fire')

    def build(self):
        # Symbol plan: A fire with a rising plume: one coherent flame outline and one separate smoke curve. The damaged source is a lone stroke; reconstruct the named subject.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=f'{n}-{j}'
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
        path('flame',(24,18),[('C',(40,32),(24,25),(40,23)),('A',(8,32),16,12,True),('C',(14,22),(8,27),(10,24)),('C',(24,18),(16,33),(26,29))],True)
        path('smoke',(20,10),[('C',(30,4),(14,4),(27,4))])
