"""Add the shared bounds inspector to a static side-combination collection."""
import json,shutil
from pathlib import Path

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist


def install_popup(folder, rows, results):
    template=Path(__file__).with_name('templates')/'side-combination-popup.js'
    shutil.copyfile(template,folder/template.name)
    shutil.copyfile(template.with_name('side-repair-flags.js'),folder/'side-repair-flags.js')
    pairs=json.loads((Path(__file__).resolve().parents[1]/'data/combination-pairs.json').read_text())['rows']
    wanted={r['id'] for r in rows}
    minimal=[{'id':p['id'],'concept':p['concept'],**{role:[{k:v for k,v in item.items() if k in ('icon','family','model_key','sha256')} for item in p[role]] for role in ('mains','subs')}} for p in pairs if p['id'] in wanted]
    data={r['id']:{'placements':results[r['id']]['placements'],'url':'svg/'+r['id']+'.svg','filename':r['id']+'.svg'} for r in rows}
    code='const sidePopupData='+json.dumps(data,separators=(',',':'))+';\n'
    code+='SideRepairFlags.setRows('+json.dumps(minimal,separators=(',',':'))+');\n'
    code+='const sideActionRows='+json.dumps({r['id']:r for r in minimal},separators=(',',':'))+';\n'
    code+='''for(const card of document.querySelectorAll('article')){const images=[...card.querySelectorAll('.art img')];let id;for(const image of images){id=image.getAttribute('src').split('/').pop().replace(/\\.svg$/,'');if(sidePopupData[id])SideCombinationPopup.attach(image,card.querySelector('h2').textContent,sidePopupData[id]);}const pair=sideActionRows[id];if(pair&&!card.querySelector('.side-result-actions')){const actions=document.createElement('div');actions.className='side-result-actions';const a=document.createElement('a');a.href='svg/'+id+'.svg';a.download=id+'.svg';SideRepairFlags.download(a);actions.append(a,SideRepairFlags.button('main',pair.mains[0],pair),SideRepairFlags.button('sub',pair.subs[0],pair));card.append(actions);}}'''
    (folder/'popup-data.js').write_text(code)
    page=folder/'index.html';s=page.read_text()
    if 'src="popup-data.js"' not in s:s=s.replace('</html>','<script src="side-combination-popup.js"></script><script src="popup-data.js"></script></html>')
    if 'src="side-repair-flags.js"' not in s:s=s.replace('<script src="popup-data.js">','<script src="side-repair-flags.js"></script><script src="popup-data.js">')
    if 'id="compact-side-header"' not in s:s=s.replace('</style>', '</style><style id="compact-side-header">body>header{padding:16px 20px 8px;max-width:none;display:flex;align-items:center;gap:10px 16px;flex-wrap:wrap}body>header h1{font-size:20px;margin:0}body>header>p:not(#count){display:none}body>header input{padding:8px 10px;width:min(320px,100%);font-size:13px}body>header #count{font-size:12px;margin:0}body>header details{font-size:12px}body>header details[open]{flex-basis:100%}body>header details ul{max-height:280px;overflow:auto}body>header .side-flag-summary{flex-basis:100%;font-size:12px;display:flex;gap:10px;margin:0}body>header .side-flag-summary[hidden]{display:none}body>header .side-flag-summary p{margin:0}body>main{padding-top:12px}</style>', 1)
    from icon_set.scripts.side_combination_progress import stage, compact_html
    import re
    progress=stage(development_dist() / 'gallery')
    s=re.sub(r'<!-- side-progress:start -->.*?<!-- side-progress:end -->','',s,flags=re.S)
    s=s.replace('<header>','<header>'+compact_html(progress, '../../.local/dist/gallery/sub-repair-review/index.html'),1)
    page.write_text(s)
