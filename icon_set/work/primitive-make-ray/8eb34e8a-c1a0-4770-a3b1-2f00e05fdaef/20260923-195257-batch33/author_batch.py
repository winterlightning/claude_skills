from pathlib import Path
import importlib.util,json
import cairosvg
from PIL import Image,ImageDraw,ImageOps

SOURCE_ICON_ID='8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef'
SOURCE_PATH='icon_set/work/todo-references/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg'
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

    def handset(self):
        # One coherent side-profile receiver: round outer sweep and two ear pads.
        self.add_bezier('receiver',(9,6),((6,6),(6,12),(6,15)),((6,26),(22,42),(33,42)),((37,42),(42,40),(42,37)),((42,35),(36,30),(34,30)),((32,30),(30,34),(28,32)),((22,28),(19,25),(16,20)),((14,17),(19,15),(19,12)),((19,10),(12,6),(9,6)))
'''
# Explicit symbol plans and dimensions own each drawing; the source SVG is not traced.
DESIGNS=[
('SQUARE','star','Passover star on a round plate behind a segmented matzo tile.','Tile rows reduced to one split; plate hidden behind foreground tile.', '''
        self.add_arc('plate',(22,38),(38,22),radius_x=16,large_arc=True)
        self.add_polyline('star',(22,12),(25,19),(32,20),(27,25),(28,32),(22,28),(16,32),(17,25),(12,20),(19,19),closed=True)
        self.box('tile',26,26,16,16,2)
        self.add_line('row',(26,34),(42,34));self.relate('connect','row','tile')
'''),
('SQUARE','bug','A six-legged insect crossed by a diagonal pest-control slash.','Thorax split and small head details omitted.', '''
        self.circle('head',24,10,4)
        self.circle('body',24,28,10,14)
        self.relate('connect','head','body')
        for sign,label in [(-1,'left'),(1,'right')]:
            self.add_polyline(label+'-antenna',(24+sign*4,10),(24+sign*8,6));self.relate('connect',label+'-antenna','head')
            for j,y in enumerate((20,28,36)):
                self.add_polyline(label+str(j),(24+sign*9,y),(24+sign*15,y-2),(24+sign*18,y-6 if j==0 else y+2))
        self.add_line('slash',(6,42),(42,6))
'''),
('SQUARE',None,'A horizontal wireless phone controller with two equal round buttons.','Narrow right seam and second wireless arc omitted to preserve clearance.', '''
        self.box('controller',6,18,36,24,4)
        for i,x in enumerate((17,31)):self.circle('button'+str(i),x,30,2)
        self.add_arc('wireless',(18,8),(30,8),radius_x=6,radius_y=2)
'''),
('SQUARE','phone','A telephone handset below a speech bubble for intercom conversation.','Speech-bubble inner text omitted as in the reference.', '''
        self.handset()
        self.add_polyline('speech',(28,6),(42,6),(42,18),(33,18),(28,22),(28,6),closed=True)
'''),
('SQUARE','phone','A telephone handset with a diagonal missed-call arrow.','No defining parts omitted.', '''
        self.handset()
        self.add_line('arrow',(42,6),(28,20))
        self.add_polyline('arrowhead',(28,10),(28,20),(38,20));self.relate('connect','arrow','arrowhead')
'''),
('VRECT_L',None,'A phone with Latin A and Chinese translation strokes across its screen.','Glyphs reduced to their essential strokes, preserving the bilingual layout.', '''
        self.add_polyline('phone-top',(12,8),(12,4),(36,4),(36,8))
        self.add_polyline('phone-bottom',(12,40),(12,44),(36,44),(36,40))
        self.add_polyline('a',(8,33),(13,18),(18,33));self.add_line('a-bar',(10,27),(16,27));self.relate('connect','a','a-bar')
        self.add_line('wen-top',(26,20),(40,20));self.add_line('wen-stem',(33,16),(33,20));self.relate('connect','wen-top','wen-stem')
        self.add_polyline('wen-left',(28,20),(30,25),(32,27),(34,29),(40,32))
        self.add_polyline('wen-right',(38,20),(34,25),(32,27),(30,29),(26,32));self.relate('connect','wen-left','wen-right')
        self.relate('connect','wen-left','wen-top');self.relate('connect','wen-right','wen-top')
'''),
('SQUARE','audio-lines','An audio-player picture with a waveform above a playback track.','Waveform amplitude reduced; tiny slider handle omitted to keep playback track clear.', '''
        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_polyline('wave',(14,18),(18,14),(23,18),(28,14),(34,18))
        self.add_line('division',(6,26),(42,26));self.relate('connect','division','frame')
        self.add_line('track',(15,34),(33,34))
'''),
('SQUARE','crop','Crop corners surrounded by two curved rotation arrows.','Rotation arcs simplified to quarter circles.', '''
        self.add_polyline('crop-left',(15,10),(15,33),(38,33))
        self.add_polyline('crop-right',(10,15),(33,15),(33,38))
        self.relate('connect','crop-left','crop-right')
        self.add_arc('rotate-top',(26,6),(42,22),radius_x=16)
        self.add_polyline('top-head',(32,6),(26,6),(26,12));self.relate('connect','rotate-top','top-head')
        self.add_arc('rotate-bottom',(22,42),(6,26),radius_x=16)
        self.add_polyline('bottom-head',(16,42),(22,42),(22,36));self.relate('connect','rotate-bottom','bottom-head')
'''),
('SQUARE','image','A hanging double frame contains a tower and stepped buildings.','Tower crossbeam omitted; two building steps retained.', '''
        self.add_polyline('hanger',(15,14),(24,6),(33,14))
        self.add_polyline('frame',(6,14),(15,14),(33,14),(42,14),(42,42),(6,42),closed=True)
        self.relate('connect','hanger','frame')
        self.add_polyline('inner',(13,21),(35,21),(35,35),(13,35),closed=True)
        self.add_polyline('tower',(15,35),(21,23),(27,35));self.relate('connect','tower','inner')
        self.add_polyline('buildings',(28,35),(28,30),(31,30),(31,26),(35,26));self.relate('connect','buildings','inner')
'''),
('SQUARE','image','A hanging picture shows a central tower flanked by two trees.','Tower crossbar retained; leaf interiors omitted.', '''
        self.add_polyline('hanger',(15,15),(24,6),(33,15))
        self.box('frame',6,15,36,27,4);self.relate('connect','hanger','frame')
        self.add_polyline('tower',(17,34),(24,21),(31,34))
        self.add_line('beam',(21,27),(27,27))
        for name,x in [('left',12),('right',36)]:
            self.add_bezier(name,(x,27),((x-5,32),(x-3,35),(x,35)),((x+3,35),(x+5,32),(x,27)))
'''),
('VRECT_L',None,'A framed abstract human profile with an eye above a nose and chin.','Eyelashes reduced to a central brow tick; nested frame retained.', '''
        self.box('frame',8,4,32,40,2)
        self.add_polyline('inner',(16,12),(32,12),(32,36),(16,36),closed=True)
        self.add_bezier('eye',(19,20),((22,16),(27,16),(30,20)),((27,23),(22,23),(19,20)))
        self.add_line('pupil',(25,18),(25,22))
        self.add_polyline('profile',(21,26),(18,30),(23,30),(22,33),(26,33),(27,36));self.relate('connect','profile','inner')
'''),
('SQUARE','image','A broad photo frame surrounds a sun and two mountain ridges.','No defining parts omitted.', '''
        self.box('frame',6,6,36,36,3)
        self.add_polyline('inner',(15,15),(33,15),(33,33),(15,33),closed=True)
        self.circle('sun',21,21,2)
        self.add_polyline('mountains',(15,29),(21,25),(25,29),(29,23),(33,27));self.relate('connect','mountains','inner')
'''),
('SQUARE','audio-lines','A photo window contains two smooth sound waves below a header.','Tiny header dot omitted; two complete waves retained.', '''
        self.box('frame',6,6,36,36,3)
        self.add_line('header',(6,15),(42,15));self.relate('connect','header','frame')
        for n,y in [('upper',25),('lower',35)]:
            self.add_bezier(n,(6,y),((12,y),(12,y-2),(18,y-2)),((24,y-2),(24,y+1),(30,y+1)),((36,y+1),(36,y-2),(42,y)))
            self.relate('connect',n,'frame')
'''),
('SQUARE',None,'A video preview bubble with play triangle above timeline trim controls.','Timeline ticks reduced to two handles.', '''
        self.add_polyline('preview',(6,6),(42,6),(42,30),(29,30),(24,34),(19,30),(6,30),closed=True)
        self.add_polyline('play',(19,14),(19,22),(28,18),closed=True)
        self.add_line('timeline',(6,42),(42,42))
        for i,x in enumerate((14,34)):
            self.add_line('handle'+str(i),(x,38),(x,42));self.relate('connect','handle'+str(i),'timeline')
'''),
('HRECT_L','image','A photographic landscape print with large left peak, smaller right peak and upper-right sun.','No defining features omitted.', '''
        self.box('print',4,8,40,32,3)
        self.circle('sun',32,19,2)
        self.add_polyline('mountains',(4,33),(17,21),(29,33),(36,29),(44,34));self.relate('connect','mountains','print')
'''),
('SQUARE','gallery-vertical-end','Two overlapping landscape cards with mountains in the foreground.','Rear card content is hidden; mountain baseline omitted and slopes extended to the frame edges to enlarge both peaks.', '''
        self.add_polyline('rear',(6,33),(6,6),(33,6))
        self.box('front',15,15,27,27,3)
        self.add_polyline('mountains',(15,34),(25,24),(31,31),(35,27),(42,34));self.relate('connect','mountains','front')
'''),
('HRECT_L','image','A landscape card contains two overlapping open mountain shapes.','No defining features omitted.', '''
        self.box('frame',4,8,40,32,4)
        self.add_polyline('near',(13,30),(21,22),(28,29))
        self.add_polyline('far',(25,26),(31,17),(35,30));self.relate('connect','near','far')
'''),
('SQUARE','image','A landscape print with cloud, two mountains and a lower caption band.','Cloud reduced to two rounded lobes; caption band left blank as in reference.', '''
        self.box('frame',6,6,36,36,3)
        self.add_bezier('cloud',(16,21),((15,21),(15,16),(18,16)),((18,14),(24,15),(24,17)),((27,22),(20,21),(16,21)))
        self.add_polyline('mountains',(6,33),(18,30),(25,33),(33,24),(42,33))
        self.add_line('caption',(6,33),(42,33));self.relate('connect','mountains','frame');self.relate('connect','caption','frame');self.relate('connect','mountains','caption')
'''),
('SQUARE','gallery-vertical-end','A photo album page with a two-by-two array of square image slots.','No defining features omitted.', '''
        self.box('page',6,6,36,36,3)
        # One square definition, repeated on a shared two-axis grid.
        for row,y in enumerate((15,27)):
            for col,x in enumerate((15,27)):
                self.add_polyline(f'slot-{row}-{col}',(x,y),(x+6,y),(x+6,y+6),(x,y+6),closed=True)
'''),
('SQUARE','user','A portrait Polaroid in front of a tilted second print.','Bust uses a circular detached head and broad shoulder arc; blank caption retained.', '''
        self.box('front',6,6,28,36,3)
        self.add_polyline('rear',(34,13),(42,16),(37,42));self.relate('connect','rear','front')
        self.circle('head',20,18,3)
        self.add_arc('shoulders',(13,34),(27,34),radius_x=7,radius_y=5,sweep=True)
        self.add_line('caption',(6,34),(34,34));self.relate('connect','caption','front');self.relate('connect','shoulders','caption')
        # head bottom 21; shoulder top 29: 8 centerline / 4 ink gap.
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
HUMAN_REFERENCE={'icon_set/references/human_ref/user.svg' if r['order'] in (11,20) else None!r}
class Drawing(Solo48):
    icon_id={ident!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
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
