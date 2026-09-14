from pathlib import Path
import ast,json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.queue_brief import main
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/dist/gallery/failures.html#rule=bounds&kind=Ink+box+too+tall'
AUTHOR='gpt-6'
W=Path(__file__).parent/'splits';W.mkdir(exist_ok=True)
ids={'left-click-mouse','right-click-mouse','wireless-mouse-with-signal','tarot-card-eye','tarot-card-moon'}
for r in json.load(open('/tmp/too-tall-targets.json')):
 if r['id'] not in ids:continue
 tree=ast.parse(Path(r['file']).read_text());meta={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('SOURCE_PATH','SOURCE_ICON_ID')}
 if r['id'].startswith('tarot'):
  glyph='Almond eye' if r['id'].endswith('eye') else 'Crescent moon'
  comps=[{'name':'Tarot card frame','family':'container','description':'The rounded rectangular tarot card enclosure alone, without its central glyph.'},{'name':glyph,'family':'sub','description':f'The {glyph.lower()} alone, without the surrounding tarot card.'}];kind='container'
 else:
  side='left' if r['id'].startswith('left') else 'right'
  wireless=r['id'].startswith('wireless')
  comps=[{'name':'Wireless mouse' if wireless else f'{side.title()} button mouse','family':'solo','description':'The mouse alone, retaining its scroll wheel.' if wireless else f'The mouse body and its {side} button division, without the external click arc.'},{'name':'Wireless signal' if wireless else f'{side.title()} click arc','family':'sub','description':'The wireless signal waves alone, without the mouse.' if wireless else f'The external {side} click arc alone, without the mouse.'}];kind='side'
 data={'reference_path':meta['SOURCE_PATH'],'source_icon_id':meta['SOURCE_ICON_ID'],'reviewed_icon':r['id'],'combination_type':kind,'reason':'A separate reusable glyph is hosted in an enclosure.' if kind=='container' else 'A separate reusable action or signal mark accompanies the mouse.','components':comps}
 p=W/(r['id']+'.json');p.write_text(json.dumps(data,indent=2));main(['--file',str(p)])
