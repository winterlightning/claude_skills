"""Suggest centered 24-unit SUB32 previews when 32 does not fit.

Run: python3 -m icon_set.scripts.suggest_container_sub_size
Select: --container heart-outline-container --sub add-sub32
Use --all-subs to check all existing SUB32 exports. Suggestions never change source artwork.
"""
from pathlib import Path
import argparse,hashlib,html,json
import xml.etree.ElementTree as ET
from collections import Counter
from shapely.geometry import shape,box
from icon_set.scripts.container_placement import Artwork,artwork_group,root_svg
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,reject_effects,check_pair,vector_zone

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist

BASE=Path(__file__).resolve().parents[1]
DEFAULT_SUBS=['check-mark','add-sub32','heart-state-63']


def transform(size,center):
    # Preserve 4-unit strokes while mapping the 28-unit centerline drafting
    # extent (2..30) into size-4. Thus the entire ink footprint stays within size.
    if size not in (24,32):raise ValueError('Supported sizes: 24 or 32 SVG units')
    scale=(size-4)/28
    return scale,center[0]-16*scale,center[1]-16*scale


def recommendation(large,small):
    if large['status']=='pass':return 'keep-32'
    if small['status']=='pass':return 'suggest-24'
    if small['status']=='fail':return 'no-fit-at-center'
    return 'review'


def measure(host,sub,center,inner,outer):
    trials={str(size):check_pair(host,VectorInk.from_art(sub,transform(size,center)),inner,outer) for size in (32,24)}
    return {'recommendation':recommendation(trials['32'],trials['24']),'center_units':center,'trials':trials}


def preview(host,sub,center,size):
    root=root_svg();root.append(artwork_group(host,'host'))
    root.append(artwork_group(sub,'content',*transform(size,center),stroke=4))
    return ET.tostring(root,encoding='unicode')


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--container',action='append',help='Container ID; repeat for multiple containers')
    parser.add_argument('--sub',action='append',help='SUB32 ID; repeat for multiple symbols')
    parser.add_argument('--all-subs',action='store_true')
    parser.add_argument('--out',type=Path,default=BASE/'work/container-size-suggestions')
    args=parser.parse_args(argv)
    if args.sub and args.all_subs:parser.error('Choose --sub or --all-subs')
    out=args.out;out.mkdir(parents=True,exist_ok=True)
    audit={r['container']:r for r in json.loads((BASE/'work/container-vector-report/results.json').read_text())['containers']}
    areas=json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
    prefs=json.loads((BASE/'data/container-placement-preferences.json').read_text())
    fixes=json.loads((BASE/'work/container-fit-repair/fit-adjustments.json').read_text())
    hosts=args.container or sorted(set(audit)|{r['variant'] for r in fixes['revisions'].values()})
    revision_by_id={r['variant']:r for r in fixes['revisions'].values()}
    names=sorted(p.stem for p in (build_dist(BASE.parent) / 'sub32').glob('*.svg')) if args.all_subs else args.sub or DEFAULT_SUBS
    subs={};blocked={}
    for name in names:
        try:
            p=build_dist(BASE.parent) / 'sub32'/f'{name}.svg';doc=p.read_text();reject_effects(doc);art=Artwork.read(doc,32)
            if min(art.bounds[:2])<2-1e-6 or max(art.bounds[2:])>30+1e-6:raise ValueError('Source centerline exceeds nominal SUB32 drafting extent')
            subs[name]=(art,sha(p))
        except (ValueError,OSError) as e:blocked[name]=str(e)
    rows=[]
    for ident in hosts:
        try:
            path=build_dist(BASE.parent) / 'container64'/f'{ident}.svg';digest=sha(path);art=read_art(path.read_text());ink=VectorInk.from_art(art)
            if ident in audit:
                c=audit[ident]
                if digest!=c['source_sha256']:raise ValueError('Stale vector interior; rebuild audit first')
                center=c.get('center_units') or areas[ident]['center']
                inner=shape(c['safe_zone_inner']) if 'safe_zone_inner' in c else None
                outer=shape(c['safe_zone_outer']) if 'safe_zone_outer' in c else None
                zone_status=c['status']
            elif ident in revision_by_id:
                c=revision_by_id[ident]
                if digest!=c['variant_sha256']:raise ValueError('Stale revision measurement')
                center=c['center'];x,y=center
                z,inner,outer=vector_zone(ink,{'kind':'safe-zone','method':'selected semantic enclosed face','polygon':[[x-1,y-1],[x+1,y-1],[x+1,y+1],[x-1,y+1]]})
                zone_status=z['status']
                if ident=='monitor-webcam-v2' and inner is None:
                    # Same explicitly bounded display region used in the verified revision audit.
                    inner=outer=box(x-17,y-17,x+17,y+17);zone_status='explicit-display-region'
            else:raise ValueError('No reviewed content center and vector area for this container')
            for name in names:
                r={'container':ident,'sub':name,'host_sha256':digest,'zone_status':zone_status}
                if name in blocked:r.update(recommendation='blocked',reason=blocked[name]);rows.append(r);continue
                sub,subsha=subs[name]
                # Keep approved optical overrides; reuse only centerline-aligned
                # corrections, never a sideways fit from the earlier clearance search.
                placement=prefs.get('optical_overrides',{}).get(ident,{}).get(name)
                if placement is None:
                    saved=fixes.get('placements',{}).get(ident,{}).get(name,{})
                    if saved.get('visual_status')=='centerline-priority' and saved.get('host_sha256')==digest and saved.get('sub_sha256')==subsha:
                        placement=saved['center']
                placement=placement or center
                r.update(measure(ink,sub,placement,inner,outer));r['sub_sha256']=subsha
                r['previews']={}
                for size in (32,24):
                    file=f'{ident}--{name}-{size}.svg';(out/file).write_text(preview(art,sub,placement,size));r['previews'][str(size)]=file
                if inner is None:
                    # A clear gap alone cannot establish the intended interior.
                    r['recommendation']='review';r['reason']='Interior is unresolved or an intentional overlay; no automatic size recommendation.'
                elif r['recommendation']=='suggest-24':
                    r['reason']='32 is not verified at this centered position; 24 passes. Visual readability still requires review.'
                rows.append(r)
        except (ValueError,OSError,KeyError) as e:
            rows.extend({'container':ident,'sub':n,'recommendation':'blocked','reason':str(e)} for n in names)
    counts=dict(Counter(r['recommendation'] for r in rows))
    payload={'counts':counts,'units':'SVG units','stroke_width':4,'padding':2,'sizes':[32,24],
             'position_policy':'Same content-centered/approved optical position for both sizes; no lateral search.',
             'scale_policy':'Preserve 4-unit strokes. Scale centerline geometry by (target size - 4) / 28 about SUB32 center (16,16). Nominal ink footprint remains within target size.',
             'limitations':'Pair-specific geometric suggestions, not visual approval. Fine internal details can become crowded when reduced. No source artwork or production selection is changed.',
             'results':rows}
    (out/'results.json').write_text(json.dumps(payload,indent=2)+'\n')
    labels={'keep-32':'Keep 32 × 32','suggest-24':'Suggest 24 × 24','no-fit-at-center':'Still too tight at this center','review':'Needs review','blocked':'Blocked'}
    cards=[]
    for r in sorted(rows,key=lambda r:(r['recommendation']!='suggest-24',r['container'],r['sub'])):
        figs=[]
        for size,file in r.get('previews',{}).items():
            trial=r['trials'][size];lo=trial['ink_gap_lower_units'];hi=trial['ink_gap_upper_units']
            figs.append(f'<figure><a href="{file}"><img loading="lazy" src="{file}" alt="{size}-unit sub-icon preview"></a><figcaption>{size} × {size} · {trial["status"].upper()}<br>Gap {lo:.4f}–{hi:.4f} u</figcaption></figure>')
        cards.append(f'<article data-name="{html.escape(r["container"]+" "+r["sub"])}" data-status="{r["recommendation"]}"><h2>{html.escape(r["container"])}</h2><p>{html.escape(r["sub"])}</p><b>{labels[r["recommendation"]]}</b><div class="pair">{"".join(figs)}</div><p>{html.escape(r.get("reason",""))}</p></article>')
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Centered sub-icon size suggestions</title><style>body{font:15px system-ui;background:#f5f7fa;color:#202630;margin:28px}header{max-width:1040px}h1{font-size:30px}p{line-height:1.5}a{color:#245f9a}nav{position:sticky;top:0;background:#f5f7fa;padding:15px 0;display:flex;gap:12px;align-items:center;z-index:1}input,select{font:inherit;padding:8px;border:1px solid #cbd3dd;border-radius:7px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(390px,1fr));gap:18px}article{background:white;border:1px solid #dce2e9;border-radius:12px;padding:20px}article[hidden]{display:none}h2{font-size:16px;overflow-wrap:anywhere}.pair{display:flex;gap:16px;margin-top:14px}figure{flex:1;margin:0;min-width:0}img{width:100%;max-width:180px}figcaption{font-size:12px;line-height:1.6}article p{font-size:13px}body.native img{width:64px}</style><header><h1>Centered sub-icon size suggestions</h1><p><a href="../container-pair-combinations/index.html"><b>Browse the defined container/sub-icon pairs on a 64 × 64 grid</b></a></p><p>Keep <b>32 × 32</b> when it passes. Suggest <b>24 × 24</b> when the smaller version clears at the <b>same centered position</b>. Both retain 4-unit strokes and require 2-unit gaps. Existing optical placements are respected; sideways clearance fallbacks are not used.</p><p>These previews shrink the path geometry around its center while retaining stroke weight: the nominal full ink footprint is 24 units. Suggestions are pair-specific, and smaller details still need a visual readability check. An unresolved interior or overlay never receives an automatic recommendation. No icon files or production choices are changed.</p>'''+f'<p><b>{html.escape(" · ".join(labels[k]+": "+str(v) for k,v in counts.items()))}</b></p>'+'''<p><a href="results.json">Download recommendations and measurements</a> · <a href="../container-fit-repair/index.html">Container revisions</a></p></header><nav><input id="q" placeholder="Find container or symbol…" aria-label="Search"><select id="status" aria-label="Recommendation"><option value="suggest-24">Suggest 24 × 24</option><option value="all">All results</option><option value="keep-32">Keep 32 × 32</option><option value="no-fit-at-center">Still too tight</option><option value="review">Needs review</option><option value="blocked">Blocked</option></select><label><input id="native" type="checkbox">Native size</label><span id="count"></span></nav><main>'''+''.join(cards)+'''</main><script>const cards=[...document.querySelectorAll('article')],q=document.querySelector('#q'),s=document.querySelector('#status');function filter(){let n=0;for(const c of cards){c.hidden=!(c.dataset.name.includes(q.value.toLowerCase())&&(s.value==='all'||c.dataset.status===s.value));if(!c.hidden)n++}document.querySelector('#count').textContent=n+' pairs'}q.oninput=filter;s.onchange=filter;document.querySelector('#native').onchange=e=>document.body.classList.toggle('native',e.target.checked);filter()</script></html>'''
    (out/'index.html').write_text(page);print(json.dumps({'counts':counts,'report':str(out/'index.html')},indent=2))

if __name__=='__main__':main()
