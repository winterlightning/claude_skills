"""Batch 54: twenty complete, ordered, standalone SOLO48 candidates."""
from pathlib import Path
import ast, importlib.util, json, io, traceback
import cairosvg
from PIL import Image, ImageDraw
SOURCE_ICON_ID='171ff3c8-7724-4935-ac18-b58d43e05931'
SOURCE_PATH='icon_set/work/todo-references/video game control directions_171ff3c8-7724-4935-ac18-b58d43e05931.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).resolve().parent
ROWS=json.loads((ROOT/'batch-inputs.json').read_text())
prior=Path('icon_set/work/primitive-make-ray/4a473edf-a356-4eca-8cfd-195e95d6bc62/20260923-210743-batch50-gpt6/author_batch.py')
HELPERS=next(ast.literal_eval(n.value) for n in ast.parse(prior.read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
BOUNDS={'SQUARE':{'ink':[4,4,44,44],'centerline':[6,6,42,42]},'CIRCLE':{'center':[24,24],'ink_radius':22,'centerline_radius':20}}
SPECS=[
('SQUARE','Circular A and B buttons accompany a directional pad.','Two circular letter buttons and an outlined four-way pad retain the diagonal arrangement.',[],'gamepad-2','''
        self.circle('button-a',12,25,6);self.circle('button-b',27,13,7)
        self.letter_a('a',(12,21),(9,28),(15,28),(10,25),(14,25))
        self.path('b',(25,9),[('L',(25,13)),('L',(25,17)),('L',(28,17)),('C',(32,17),(32,13),(28,13)),('L',(25,13))])
        self.path('b-top',(25,9),[('L',(28,9)),('C',(32,9),(32,13),(28,13))]);self.join('b','b-top')
        self.add_polyline('pad',(30,26),(38,26),(38,30),(42,30),(42,38),(38,38),(38,42),(30,42),(30,38),(26,38),(26,30),(30,30),closed=True)
        self.circle('pad-center',34,34,2)
'''),
('SQUARE','A game monitor showing a mouth-shaped character connects to a controller.','Upper-left screen, short stand and wire; lower-right slanted controller silhouette.',[],'gamepad-2;video','''
        self.rect('monitor',6,6,28,20,3,split_x=(20,))
        self.add_line('stand',(20,26),(20,30));self.add_polyline('stand-foot',(16,30),(20,30),(24,30));self.join('monitor','stand');self.join('stand','stand-foot')
        self.add_arc('character',(19,11),(19,21),radius_x=6,large_arc=True,sweep=False)
        self.add_polyline('mouth',(19,11),(15,16),(19,21));self.join('character','mouth');self.add_dot('pellet',(25,16))
        self.add_bezier('cable',(34,20),((40,20),(40,26),(36,28)));self.join('monitor','cable')
        self.path('controller',(23,33),[('L',(35,28)),('C',(39,26),(42,30),(42,33)),('C',(42,38),(38,39),(35,37)),('L',(28,40)),('C',(24,44),(19,42),(19,38)),('C',(19,36),(20,34),(23,33))],True)
'''),
('SQUARE','Three teammates stand above a game controller.','Repeated circular heads and shallow shoulder curves precede a shared controller outline.',[],'gamepad-2;human','TEAM'),
('SQUARE','Three wireless waves rise above a game controller.','Centered nested waves and a symmetric controller retain the source hierarchy.',[],'gamepad-2;wifi','WIFI'),
('SQUARE','A companion cube face has four corner blocks and a central heart medallion.','Four identical corner blocks, four narrow connector blocks and a circular heart center form a square assembly.',[],'none','''
        for i,(x,y) in enumerate(((6,6),(32,6),(6,32),(32,32))):self.rect(f'corner-{i}',x,y,10,10,2)
        self.rect('top-connector',20,8,8,4,1);self.rect('bottom-connector',20,36,8,4,1)
        self.rect('left-connector',8,20,4,8,1);self.rect('right-connector',36,20,4,8,1)
        for name,a,b in [('top-left',(16,10),(20,10)),('top-right',(28,10),(32,10)),('bottom-left',(16,38),(20,38)),('bottom-right',(28,38),(32,38)),('left-top',(10,16),(10,20)),('left-bottom',(10,28),(10,32)),('right-top',(38,16),(38,20)),('right-bottom',(38,28),(38,32))]:self.add_line(name,a,b)
        self.circle('medallion',24,24,9)
        self.path('heart',(24,29),[('L',(20,25)),('C',(17,22),(21,19),(24,22)),('C',(27,19),(31,22),(28,25)),('L',(24,29))],True)
'''),
('SQUARE','The Twitch speech-bubble logo contains two upright bars.','Rounded upper frame, clipped lower-right corner and lower-left tail contain evenly spaced bars.',[],'none','''
        self.path('bubble',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,28)),('L',(34,36)),('L',(22,36)),('L',(14,42)),('L',(14,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        for i,x in enumerate((20,30)):self.add_line(f'bar-{i}',(x,16),(x,24))
'''),
('SQUARE','A camera is crossed by a diagonal video-off slash.','Two open camera-body strokes leave the slash visible; an attached trapezoidal lens remains on the right.',[],'video','''
        self.path('body-upper',(16,12),[('L',(30,12)),('A',(34,16),4,4,True),('L',(34,20)),('L',(34,26)),('L',(34,30))])
        self.path('body-lower',(10,18),[('L',(10,30)),('A',(14,34),4,4,False),('L',(24,34))])
        self.add_polyline('lens',(34,20),(42,14),(42,32),(34,26));self.join('body-upper','lens')
        self.add_line('slash',(6,6),(38,42))
'''),
('CIRCLE','A 0x coin contains an outlined X and a rising diagonal segment.','Coin ring encloses the complete outlined X; exposed diagonal pieces remain at opposite corners.',[],'none','''
        self.circle('coin',24,24,20)
        self.add_polyline('x-outline',(18,14),(24,20),(30,14),(34,18),(28,24),(34,30),(30,34),(24,28),(18,34),(14,30),(20,24),(14,18),closed=True)
        self.add_line('diagonal-low',(10,38),(16,32));self.add_line('diagonal-high',(32,16),(38,10))
'''),
('CIRCLE','An Algorand coin contains an angular A-like logo.','A circular coin owns an open apex and a separate short interior diagonal.',[],'none','''
        self.circle('coin',24,24,20)
        self.add_polyline('logo',(15,31),(24,14),(33,31))
        self.add_line('inner-stroke',(20,31),(24,24))
'''),
('CIRCLE','A KuCoin token contains a vertical stem and open angular K mark.','The K uses a shared central junction and paired open angular branches.',['The near-adjacent vertical stem and chevron meet at one shared K junction.'],'none','''
        self.circle('coin',24,24,20)
        self.add_polyline('stem',(17,15),(17,24),(17,33))
        self.add_polyline('k-top',(17,24),(26,15),(32,21))
        self.add_polyline('k-bottom',(17,24),(26,33),(32,27));self.join('stem','k-top','k-bottom')
'''),
('CIRCLE','A Monero coin contains a simple angular M.','The circular coin encloses a symmetric five-node M stroke.',[],'none','''
        self.circle('coin',24,24,20)
        self.add_polyline('m',(16,32),(16,16),(24,24),(32,16),(32,32))
'''),
('SQUARE','A panoramic virtual environment is represented by a curved wraparound wall.','Elliptical top and bottom edges frame the two narrow side panels.',[],'none','ENV_CLOSED'),
('SQUARE','A wraparound virtual environment has a detached curved upper rim.','The floating top arc remains separate from the curved wall and its side panels.',[],'none','ENV_OPEN'),
('SQUARE','A visibility mark shows a left-facing triangle, three dashes and the number 100.','The geometric direction marker sits above hand-authored digits; all three dashes remain.',[],'none','''
        self.add_polyline('triangle',(6,18),(18,6),(18,30),closed=True)
        self.add_line('dash-0',(24,16),(28,16));self.add_line('dash-1',(34,16),(38,16));self.add_dot('dash-2',(42,16))
        self.add_polyline('one',(18,36),(20,34),(20,42));self.add_polyline('one-base',(18,42),(20,42),(22,42));self.join('one','one-base')
        for i,x in enumerate((26,36)):self.rect(f'zero-{i}',x,32,6,10,3)
'''),
('SQUARE','A speaker horn is muted by an X to its right.','Rounded speaker housing transitions to a tall horn; a detached symmetric X occupies the right band.',[],'volume-x','''
        self.path('speaker',(25,6),[('L',(14,16)),('L',(10,16)),('A',(6,20),4,4,False),('L',(6,28)),('A',(10,32),4,4,False),('L',(14,32)),('L',(25,42))],True)
        self.cross('mute',38,24,4,True)
'''),
('SQUARE','A stylus and wireframe box accompany a VR headset.','Upper-left stylus and open cube lead into the lower-right headset with paired lens circles.',[],'box','''
        self.add_polyline('stylus',(8,6),(14,12),(16,18),(10,16),(6,10),closed=True)
        self.add_polyline('cube-left',(6,22),(18,26),(18,36),(6,32),closed=True)
        self.add_polyline('cube-top',(24,20),(30,22),(18,26));self.join('cube-left','cube-top')
        self.add_line('cube-right',(30,22),(30,27));self.join('cube-top','cube-right')
        self.path('headset',(22,30),[('C',(22,27),(25,27),(27,30)),('L',(37,30)),('C',(39,27),(42,27),(42,30)),('L',(42,38)),('A',(38,42),4,4,True),('L',(35,42)),('C',(33,42),(34,39),(32,39)),('C',(30,39),(31,42),(29,42)),('L',(26,42)),('A',(22,38),4,4,True),('L',(22,30))],True)
        self.add_line('headset-rim',(22,33),(42,33))
        for i,x in enumerate((27,37)):self.circle(f'lens-{i}',x,37,2)
'''),
('SQUARE','Two seated people wait beneath a clock.','Paired circular heads align with their torso starts; two distinct seated leg arrangements preserve the scene.',[],'human','''
        self.circle('clock',12,12,6);self.add_polyline('clock-hands',(12,9),(12,12),(15,12))
        for i,x in enumerate((24,36)):
            self.circle(f'head-{i}',x,16,3)
            self.add_line(f'torso-{i}',(x,27),(x,34))
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
        self.add_polyline('legs-left',(24,34),(20,34),(18,34),(14,42));self.join('torso-0','legs-left')
        self.add_line('lower-left',(20,34),(20,42));self.join('legs-left','lower-left')
        self.add_polyline('legs-right',(36,34),(42,34),(42,42));self.join('torso-1','legs-right')
'''),
('CIRCLE','A walking figure is crossed by a prohibition slash inside a circle.','A circular sign owns its diagonal slash; the figure uses an aligned circular head and segmented torso.',[],'human','''
        self.path('sign',(12,8),[('A',(36,40),20,20,True),('A',(12,8),20,20,True)],True)
        self.add_line('slash',(12,8),(36,40));self.join('sign','slash')
        self.circle('head',24,12,3)
        self.add_line('torso',(24,23),(24,27))
        self.add_line('hip',(24,27),(22,30));self.join('torso','hip')
        self.add_polyline('arms',(18,25),(20,22),(24,23),(30,26),(34,26));self.join('arms','torso')
        self.add_polyline('legs',(18,36),(22,30),(28,32),(30,38));self.join('hip','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
('SQUARE','A notched faction banner hangs from a crossbar beside a vertical pole.','Ball finial, crossbar and header share real nodes; the swallowtail is centered in the hanging cloth.',[],'flag','''
        self.circle('finial',9,10,3)
        self.add_polyline('crossbar',(12,10),(18,10),(34,10),(42,10));self.join('finial','crossbar')
        self.add_polyline('pole',(42,6),(42,10),(42,42));self.join('pole','crossbar')
        self.add_polyline('banner',(18,10),(18,18),(18,38),(26,30),(34,38),(34,18),(34,10));self.join('banner','crossbar')
        self.add_line('header',(18,18),(34,18));self.join('banner','header')
'''),
('SQUARE','A blank rounded watch face sits in front of a curved perspective strap.','Rounded face and an interrupted outer strap share exact attachment nodes; two inner strap seams preserve depth.',[],'watch','''
        self.rect('face',6,14,24,20,4,split_x=(24,))
        self.path('strap-upper',(10,14),[('C',(14,6),(18,6),(26,6)),('L',(30,6)),('C',(38,6),(42,14),(42,22))]);self.join('face','strap-upper')
        self.path('strap-lower',(42,30),[('C',(42,38),(36,42),(30,42)),('L',(22,42)),('C',(16,42),(12,39),(10,34))]);self.join('face','strap-lower')
        self.add_line('seam-upper',(30,6),(24,14));self.join('strap-upper','seam-upper');self.join('face','seam-upper')
        self.add_line('seam-lower',(24,34),(30,42));self.join('strap-lower','seam-lower');self.join('face','seam-lower')
'''),
]

def controller():
    return '''
        self.path('controller',(14,28),[('L',(34,28)),('A',(42,36),8,8,True),('L',(42,38)),('C',(42,42),(38,42),(35,39)),('L',(31,36)),('L',(17,36)),('L',(13,39)),('C',(10,42),(6,42),(6,38)),('L',(6,36)),('A',(14,28),8,8,True)],True)
        self.cross('d-pad',14,33,3)
        self.add_dot('button',(34,32))
'''

def environment(open_top):
    lower=[('L',(42,34)),('C',(42,37),(38,39),(34,40)),('C',(30,41),(27,42),(24,42)),('C',(21,42),(18,41),(14,40)),('C',(10,39),(6,37),(6,34))]
    if not open_top:
        return '''
        self.path('wall',(6,14),[('C',(6,10),(14,6),(24,6)),('C',(34,6),(42,10),(42,14)),
'''+repr(lower)[1:-1]+''',('L',(6,14))],True)
        self.add_polyline('left-panel',(6,14),(14,18),(14,40));self.join('wall','left-panel')
        self.add_polyline('right-panel',(42,14),(34,18),(34,40));self.join('wall','right-panel')
'''
    return '''
        self.add_bezier('top-rim',(6,12),((10,8),(17,6),(24,6)),((31,6),(38,8),(42,12)))
        self.path('wall',(42,20),
'''+repr(lower+ [('L',(6,20))])+''')
        self.add_polyline('left-panel',(6,20),(14,24),(14,40));self.join('wall','left-panel')
        self.add_polyline('right-panel',(42,20),(34,24),(34,40));self.join('wall','right-panel')
'''

def main():
    for i,(row,spec) in enumerate(zip(ROWS,SPECS)):
        out=Path(row['result_dir'])
        if (out/'result.json').exists():continue
        key,subject,plan,omissions,refs,body=spec
        if body=='TEAM':
            body='''
        for i,x in enumerate((12,24,36)):
            self.circle(f'head-{i}',x,9,3)
            self.add_bezier(f'shoulders-{i}',(x-6,23),((x-4,20),(x-2,20),(x,20)),((x+2,20),(x+4,20),(x+6,23)))
'''+controller()
        if body=='WIFI':
            body='''
        self.add_bezier('wifi-outer',(10,12),((14,8),(20,6),(24,6)),((28,6),(34,8),(38,12)))
        self.add_bezier('wifi-middle',(16,20),((19,17),(22,15),(24,15)),((26,15),(29,17),(32,20)))
        self.add_bezier('wifi-inner',(21,24),((22,23),(23,23),(24,23)),((25,23),(26,23),(27,24)))
'''+controller()
        if body.startswith('ENV_'):body=environment(body=='ENV_OPEN')
        ref_list=['Supplied SVG rendered and inspected.']
        for ref in refs.split(';'):
            if ref=='human':ref_list.append('human-reference.md, human_ref/user.svg and full_body_ref.png: circular heads, consistent limbs, aligned torso and exact 4-unit detached-head ink gap.')
            elif ref=='none':ref_list.append('No useful local Lucide subject match used; geometric reconstruction follows the supplied drawing.')
            else:ref_list.append(f'Lucide original/{ref}.svg and atomic-debug/{ref}.svg: coherent contours, repeated radii and explicit shared junctions, freshly authored for SOLO48.')
        module_name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
        source=f'''"""{subject}
Plan: {plan}
Keyshape {key}: {BOUNDS[key]!r}.
References: {' '.join(ref_list)}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
'''+HELPERS+'\n    def build(self):\n'+body
        (out/module_name).write_text(source)
        data=dict(row,keyshape=key,keyshape_bounds=BOUNDS[key],subject=subject,construction_plan=plan,omissions=omissions,references=ref_list,python=module_name)
        try:
            s=importlib.util.spec_from_file_location(f'batch54_{i}',out/module_name);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
            icon=m.Drawing();report=icon.validate_icon();data['validation_status']=report.status;(out/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(out/(row['icon_id']+'.svg')).write_text(svg);data['export_status']='success'
            for size in (48,192):
                alpha=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size))).convert('RGBA').getchannel('A')
                for theme,bg,ink in [('light','white','black'),('dark','#16191d','#f4f5f6')]:
                    im=Image.new('RGB',(size,size),bg);im.paste(ink,(0,0,size,size),alpha);im.save(out/f'{theme}-{size}.png')
        except Exception:
            data.setdefault('validation_status','error');data['export_status']='error';data['error']=traceback.format_exc();(out/'error.txt').write_text(data['error'])
        (out/'attempt-findings.json').write_text(json.dumps(data,indent=2)+'\n');print(i+1,row['concept'],data['validation_status'],data['export_status'],flush=True)
    sheet=Image.new('RGB',(1080,7*270),'#dadde0');d=ImageDraw.Draw(sheet)
    for i,row in enumerate(ROWS):
        out=Path(row['result_dir']);x=i%3*360;y=i//3*270;d.text((x+4,y+4),f"{i+1}. {row['concept'][:36]}",fill='black')
        for j,theme in enumerate(('light','dark')):
            if (out/f'{theme}-192.png').exists():
                sheet.paste(Image.open(out/f'{theme}-192.png').resize((160,160)),(x+j*180,y+26));sheet.paste(Image.open(out/f'{theme}-48.png'),(x+j*180+56,y+198))
    sheet.save(ROOT/'authored-review.png')
if __name__=='__main__':main()
