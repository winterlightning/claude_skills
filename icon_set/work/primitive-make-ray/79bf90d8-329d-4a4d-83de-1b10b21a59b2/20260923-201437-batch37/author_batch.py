from pathlib import Path
import importlib.util,json
import cairosvg
from PIL import Image,ImageDraw,ImageOps

SOURCE_ICON_ID='79bf90d8-329d-4a4d-83de-1b10b21a59b2'
SOURCE_PATH='icon_set/work/todo-references/real estate market house decrease_79bf90d8-329d-4a4d-83de-1b10b21a59b2.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'batch.json').read_text())
HELPERS='''
    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def house(self,n,x,y,w,h):
        mid=x+w//2
        self.add_polyline(n,(x,y+8),(mid,y),(x+w,y+8),(x+w,y+h),(x,y+h),closed=True)

    def bust(self,n,x,y,r,shoulder_w,shoulder_h):
        self.circle(n+'-head',x,y,r)
        body_top=y+r+8
        self.add_arc(n+'-shoulders',(x-shoulder_w,body_top+shoulder_h),(x+shoulder_w,body_top+shoulder_h),radius_x=shoulder_w,radius_y=shoulder_h)
        # Exact detached gap: (y+r+8) - (y+r) = 8 centerline / 4 ink.
'''
DESIGNS=[
('HRECT_L','chart-no-axes-column-increasing','Three descending market bars below a downward diagonal arrow.','No house added: the supplied reference contains only chart bars and arrow.', '''
        for i,(x,top) in enumerate(((4,20),(20,28),(36,32))):
            self.add_polyline('bar'+str(i),(x,40),(x,top),(x+8,top),(x+8,40),closed=True)
        self.add_line('trend',(4,8),(44,24))
        self.add_polyline('tip',(36,24),(44,24),(41,16));self.relate('connect','trend','tip')
'''),
('HRECT_L','chart-no-axes-column-increasing','Three ascending market bars under an upward diagonal arrow.','No house added: the supplied reference contains only chart bars and arrow.', '''
        for i,(x,top) in enumerate(((4,32),(20,24),(36,8))):
            self.add_polyline('bar'+str(i),(x,40),(x,top),(x+8,top),(x+8,40),closed=True)
        self.add_line('trend',(4,20),(28,8))
        self.add_polyline('tip',(20,8),(28,8),(28,16));self.relate('connect','trend','tip')
'''),
('SQUARE','house','An open-door house with a rising zigzag market arrow at lower right.','Door arch retained; right wall and right jamb shortened to leave room for the rising trend.', '''
        self.add_polyline('roof',(6,20),(20,6),(34,20))
        self.add_polyline('walls',(10,16),(10,32),(18,32),(18,26))
        self.add_arc('door',(18,26),(26,26),radius_x=4)
        self.add_line('jamb',(26,26),(26,28));self.relate('connect','walls','door');self.relate('connect','door','jamb');self.relate('connect','roof','walls')
        self.add_line('right-wall',(30,16),(30,22));self.relate('connect','right-wall','roof')
        self.add_polyline('trend',(18,42),(26,36),(32,42),(42,30))
        self.add_polyline('tip',(34,30),(42,30),(42,38));self.relate('connect','trend','tip')
'''),
('SQUARE','house','A house sits inside an open circular market ring with a thick upper-right segment.','Door retained; ring segment reduced to a clean double arc.', '''
        self.add_arc('ring',(24,6),(42,24),radius_x=18,large_arc=True,sweep=False)
        self.add_arc('segment-outer',(24,6),(42,24),radius_x=18)
        self.add_arc('segment-inner',(34,24),(24,14),radius_x=10,sweep=False)
        self.add_line('segment-end',(42,24),(34,24));self.add_line('segment-start',(24,14),(24,6))
        self.add_contour('segment','segment-outer','segment-end','segment-inner','segment-start',closed=True)
        self.house('house',15,20,18,13)
        self.add_polyline('door',(21,33),(21,27),(27,27),(27,33));self.relate('connect','door','house')
'''),
('SQUARE','house','Two people discuss a house in a speech bubble above them.','Small door omitted; paired busts use identical proportions.', '''
        self.add_polyline('bubble',(10,6),(38,6),(38,20),(26,20),(22,24),(22,20),(10,20),closed=True)
        self.house('house',18,10,12,8)
        for n,x in [('left',12),('right',36)]:self.bust(n,x,29,3,6,2)
'''),
('VRECT_L','hand','An extended index finger selects a house above the hand.','Palm creases omitted; house door retained.', '''
        self.house('house',22,4,18,14)
        self.add_polyline('door',(28,18),(28,12),(34,12),(34,18));self.relate('connect','door','house')
        self.add_bezier('hand',(16,44),((16,36),(10,35),(8,28)),((8,21),(12,27),(16,30)),((16,24),(16,18),(16,18)),((16,13),(22,13),(22,18)),((22,21),(22,25),(22,27)),((22,22),(28,23),(28,27)),((28,23),(34,24),(34,29)),((34,34),(36,36),(34,44)))
'''),
('HRECT_L',None,'Three segmented columns below a curved two-ended rearrangement arrow.','Rows reduced to two per column.', '''
        for i,x in enumerate((4,20,36)):
            self.add_polyline('column'+str(i),(x,24),(x+8,24),(x+8,40),(x,40),closed=True)
            self.add_line('rule'+str(i),(x,32),(x+8,32));self.relate('connect','rule'+str(i),'column'+str(i))
        self.add_bezier('arrow',(8,15),((8,8),(14,8),(20,8)),((26,8),(40,8),(40,15)))
        self.add_polyline('left-tip',(4,11),(8,15),(12,11));self.relate('connect','left-tip','arrow')
        self.add_polyline('right-tip',(36,11),(40,15),(44,11));self.relate('connect','right-tip','arrow')
'''),
('SQUARE','user','A receptionist behind a desk receives payment from a standing customer.','Currency mark simplified to a dollar-style S with stem; hands reduced to gestures.', '''
        self.bust('clerk',14,10,4,8,4)
        self.add_line('counter',(6,26),(22,26));self.relate('connect','counter','clerk-shoulders')
        self.add_line('desk',(10,26),(10,42));self.relate('connect','desk','counter')
        self.circle('head',36,10,4)
        self.add_line('torso',(36,22),(36,32))
        self.add_polyline('legs',(30,42),(36,32),(42,42));self.relate('connect','torso','legs')
        self.add_polyline('arms',(26,28),(36,22),(42,28));self.relate('connect','arms','torso')
        self.mark_human_figure('customer',head='head',torso='torso',torso_junction='start')
        self.add_bezier('dollar',(25,32),((15,29),(16,36),(22,36)),((28,36),(26,43),(18,40)))
        self.add_line('currency-stem',(22,30),(22,42))
'''),
('SQUARE','user','An open résumé document is overlaid by a full applicant silhouette on the right.','Document text reduced to two rows and one square photo placeholder.', '''
        self.add_polyline('document',(36,6),(6,6),(6,42),(24,42))
        self.add_polyline('photo',(14,14),(22,14),(22,22),(14,22),closed=True)
        for i,y in enumerate((30,38)):self.add_line('text'+str(i),(14,y),(22,y))
        self.circle('head',34,18,4)
        self.add_arc('shoulders',(26,36),(42,36),radius_x=8,radius_y=6)
        self.add_polyline('body',(42,36),(39,36),(38,42),(30,42),(29,36),(26,36));self.relate('connect','shoulders','body')
        # Head bottom 22; shoulders top 30: exact 4-unit visible gap.
'''),
('HRECT_L',None,'The letters AD inside a rectangular advertising panel.','No letters omitted; outlines squared to preserve spacing.', '''
        self.add_polyline('frame',(4,8),(44,8),(44,40),(4,40),closed=True)
        self.add_polyline('a',(12,31),(15,16),(18,31))
        self.add_line('a-bar',(13,26),(17,26));self.relate('connect','a','a-bar')
        self.add_line('d-stem',(27,31),(27,17));self.add_arc('d-bowl',(27,17),(27,31),radius_x=8,radius_y=7);self.add_contour('d','d-stem','d-bowl',closed=True)
'''),
('HRECT_L',None,'A rectangular barcode card with repeated vertical bars.','Seven narrow source bars reduced to four equally spaced bars.', '''
        self.add_polyline('frame',(4,8),(44,8),(44,40),(4,40),closed=True)
        for i,x in enumerate((12,20,28,36)):
            self.add_line('bar'+str(i),(x,16),(x,32 if i in (0,3) else 30))
'''),
('HRECT_M',None,'A long rounded password field containing two X masking marks.','No masking marks omitted.', '''
        self.box('field',4,10,40,28,10)
        for i,x in enumerate((17,31)):
            self.add_line('x'+str(i)+'a',(x-3,21),(x+3,27));self.add_line('x'+str(i)+'b',(x+3,21),(x-3,27));self.relate('connect','x'+str(i)+'a','x'+str(i)+'b')
'''),
('HRECT_L',None,'BUY lettering inside a purchase button.','All three letters retained; hand-built centerline glyphs.', '''
        self.box('frame',4,8,40,32,3)
        self.add_line('b-stem',(11,32),(11,16))
        self.add_arc('b-upper',(11,16),(11,24),radius_x=6,radius_y=4)
        self.add_arc('b-lower',(11,24),(11,32),radius_x=6,radius_y=4)
        self.add_contour('b','b-stem','b-upper','b-lower',closed=True)
        self.add_line('u-left',(22,16),(22,28));self.add_arc('u-bottom',(22,28),(28,28),radius_x=3,sweep=False);self.add_line('u-right',(28,28),(28,16));self.add_contour('u','u-left','u-bottom','u-right')
        self.add_polyline('y-top',(33,16),(37,24),(41,16));self.add_line('y-stem',(37,24),(37,32));self.relate('connect','y-top','y-stem')
'''),
('HRECT_M','check','A wide rectangle contains a checkmark left of centre.','No defining features omitted.', '''
        self.add_polyline('frame',(4,10),(44,10),(44,38),(4,38),closed=True)
        self.add_polyline('check',(13,24),(19,30),(30,18))
'''),
('SQUARE','scan-qr-code','A QR-code card with three square finder marks and a broken lower-right mark.','Small code strokes reduced to a corner and a dash.', '''
        self.box('frame',6,6,36,36,4)
        for n,x,y in [('tl',14,14),('tr',28,14),('bl',14,28)]:self.add_polyline(n,(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        self.add_polyline('corner',(28,34),(28,28),(34,28))
        self.add_line('dash',(32,38),(36,38))
'''),
('VRECT_L','user','An employee résumé with a portrait above two long text rows.','Detached portrait head uses exact 4-unit visible clearance to shoulders.', '''
        self.add_polyline('frame',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.bust('person',22,13,3,6,2)
        for i,y in enumerate((32,38)):self.add_line('text'+str(i),(16,y),(32,y))
'''),
('VRECT_L','user','A résumé portrait has two short text lines beside it and two below.','All four text rows retained; repeated line definitions.', '''
        self.add_polyline('frame',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.bust('person',21,13,3,6,2)
        for i,y in enumerate((23,31)):self.add_line('side'+str(i),(31,y),(35,y))
        for i,y in enumerate((32,38)):self.add_line('bottom'+str(i),(16,y),(27,y))
'''),
('HRECT_L','move-diagonal-2','A diagonal two-headed expand arrow inside a rectangular card.','No defining features omitted.', '''
        self.box('frame',4,8,40,32,4)
        self.add_line('diagonal',(14,18),(32,30))
        self.add_polyline('upper',(14,26),(14,18),(22,18));self.relate('connect','upper','diagonal')
        self.add_polyline('lower',(24,30),(32,30),(32,22));self.relate('connect','lower','diagonal')
'''),
('VRECT_L','file-clock','A clipped-corner history document with a clock and bottom text rule.','Clock face ticks omitted, retaining both hands.', '''
        self.add_polyline('document',(8,4),(32,4),(40,12),(40,44),(8,44),closed=True)
        self.circle('clock',24,22,9)
        self.add_polyline('hands',(24,18),(24,22),(27,22))
        self.add_line('rule',(16,36),(32,36))
'''),
('HRECT_L',None,'LIKE lettering inside a rectangular social button.','All four letters retained; hand-built centerline glyphs.', '''
        self.box('frame',4,8,40,32,3)
        self.add_polyline('l',(10,18),(10,30),(15,30))
        self.add_line('i',(20,18),(20,30))
        self.add_line('k-stem',(26,18),(26,30));self.add_polyline('k-arms',(31,18),(26,24),(31,30));self.relate('connect','k-stem','k-arms')
        self.add_polyline('e',(40,18),(35,18),(35,30),(40,30));self.add_line('e-middle',(35,24),(39,24));self.relate('connect','e','e-middle')
'''),
]

def run():
    for r,(key,lucide,plan,omit,body) in zip(ROWS,DESIGNS):
        out=Path(r['out']);ident=r['icon_id'];source=out/(ident.replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py')
        source.write_text(f'''from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID={r['source_uuid']!r}
SOURCE_PATH={r['reference_path']!r}
AUTHOR={AUTHOR!r}
PLAN={plan!r}
OMISSIONS={omit!r}
LUCIDE_REFERENCE={lucide!r}
HUMAN_REFERENCE={'icon_set/references/human_ref/user.svg' if r['order'] in (5,6,8,9,16,17) else None!r}
FULL_BODY_REFERENCE={'icon_set/references/human_ref/full_body_ref.png' if r['order']==8 else None!r}
class Drawing(Solo48):
    icon_id={ident!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(r['concept'].split())!r}
{HELPERS}
    def build(self):
        # {plan}
{body}
''')
        r.update(source=source.name,keyshape=key,lucide=lucide,subject=plan,omissions=omit)
        try:
            spec=importlib.util.spec_from_file_location('candidate',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();r['validation_status']=report.status;(out/'validation.txt').write_text(report.describe());svg=icon.to_svg();(out/(ident+'.svg')).write_text(svg)
            for size in (48,192):
                p=out/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(out/f'dark-{size}.png')
        except Exception as e:
            r['validation_status']='error';r['error']=str(e);(out/'error.txt').write_text(str(e))
        print(r['order'],ident,r['validation_status'],r.get('error',''),flush=True)
    (ROOT/'attempts.json').write_text(json.dumps(ROWS,indent=2))
    for start in (0,10):
        sheet=Image.new('RGB',(1000,550),'#ccc');d=ImageDraw.Draw(sheet)
        for j,r in enumerate(ROWS[start:start+10]):
            x=j%5*200;y=j//5*275;out=Path(r['out'])
            for theme,dx in [('light',0),('dark',100)]:
                if (out/f'{theme}-192.png').exists():
                    sheet.paste(Image.open(out/f'{theme}-192.png').resize((96,96)),(x+dx,y+20));sheet.paste(Image.open(out/f'{theme}-48.png'),(x+dx+24,y+135))
            d.text((x+3,y+205),f"{r['order']}. {r['concept'][:25]}",fill='black');d.text((x+3,y+225),r['validation_status'],fill='black')
        sheet.save(ROOT/f'review-{start}.png')

if __name__=='__main__':run()
