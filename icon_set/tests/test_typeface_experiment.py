import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from icon_set.scripts.experiment_gallery import typeface_samples


class TypefaceExperimentTests(unittest.TestCase):
    def test_centerlines_keep_exact_paths(self):
        glyphs=json.loads((Path(__file__).resolve().parents[2]/'published/gallery/typeface.json').read_text())['glyphs']
        rows=typeface_samples(glyphs)
        self.assertEqual(len(rows),len(glyphs))
        self.assertEqual(len({r['key'] for r in rows}),len(glyphs))
        by_id={g['icon_id']:g for g in glyphs}
        for row in rows:
            with self.subTest(icon=row['icon_id']):
                original=ET.fromstring(row['outline'])
                overlay=ET.fromstring(row['result'])
                groups=list(overlay)
                self.assertEqual(len(groups),2)
                self.assertEqual(groups[0].get('stroke-width'),'4')
                self.assertEqual(groups[1].get('stroke-width'),'0.65')
                paths=by_id[row['icon_id']]['paths']
                self.assertEqual([p.get('d') for p in list(original)[0]],paths)
                for group in groups:self.assertEqual([p.get('d') for p in group],paths)

    def test_offline_page_has_all_samples_and_composer_link(self):
        root=Path(__file__).resolve().parents[2]/'published/gallery'
        html=(root/'experiment.html').read_text()
        self.assertNotIn('__TYPEFACE_',html)
        glyphs=json.loads((root/'typeface.json').read_text())['glyphs']
        payload=html.split('<script id="typefaceExperimentData" type="application/json">')[1].split('</script>')[0]
        self.assertEqual(len(json.loads(payload)['icons']),len(glyphs))
        v2=html.split('<script id="typefaceV2ExperimentData" type="application/json">')[1].split('</script>')[0]
        self.assertEqual(len(json.loads(v2)['icons']),len(json.loads((root/'typeface-v2.json').read_text())['glyphs']))
        self.assertIn('id="typefaceVersion"',html)
        js=(root/'experiment.js').read_text()
        self.assertIn("review.href='text-combine.html'+(typefaceVersion==='v2'?'?version=v2':'')",js)
        self.assertIn("'typeface-v2'",js)
        self.assertIn("type==='typeface'?Math.max(1,filtered.length):pageSize",js)

    def test_originals_use_source_files_and_uppercase_has_none(self):
        root=Path(__file__).resolve().parents[2]
        rows=json.loads((root/'published/gallery/experiment-typeface.json').read_text())['icons']
        glyphs={g['icon_id']:g for g in json.loads((root/'published/gallery/typeface.json').read_text())['glyphs']}
        originals=[r for r in rows if r['original'] is not None]
        self.assertEqual(len(originals),sum(1 for g in glyphs.values() if g.get('source_path')))
        self.assertEqual(sum(1 for r in originals if r['icon_id'].startswith(('letter-','digit-'))),37)
        for row in rows:
            with self.subTest(icon=row['icon_id']):
                source_path=glyphs[row['icon_id']].get('source_path')
                if row['icon_id'].endswith('-uppercase') or not source_path:
                    self.assertIsNone(row['original'])
                    self.assertIsNone(row['original_preview'])
                else:
                    source=root/source_path
                    if row['icon_id'].startswith(('letter-','digit-')):
                        self.assertEqual(source.parent,root/'Letters/old')
                    self.assertEqual(row['original'],source.read_text())
                    self.assertTrue(row['original_preview'].startswith('data:image/png;base64,'))
                self.assertTrue(row['outline_preview'].startswith('data:image/png;base64,'))
        self.assertEqual(next(r for r in rows if r['icon_id']=='letter-o-large')['original_name'],'o.svg')
        self.assertEqual(next(r for r in rows if r['icon_id']=='letter-o')['original_name'],'o-1.svg')

    def test_v2_samples_use_upper_and_number_originals(self):
        root=Path(__file__).resolve().parents[2]
        rows=json.loads((root/'published/gallery/experiment-typeface-v2.json').read_text())['icons']
        glyphs={g['icon_id']:g for g in json.loads((root/'published/gallery/typeface-v2.json').read_text())['glyphs']}
        self.assertEqual(len(rows),len(glyphs))
        self.assertEqual(len(rows),36)
        for row in rows:
            with self.subTest(icon=row['icon_id']):
                glyph=glyphs[row['icon_id']]
                source=root/glyph['source_path']
                expected=root/'Letters'/('UPPER' if glyph['kind']=='uppercase' else 'Numbers')
                self.assertEqual(source.parent,expected)
                self.assertEqual(row['original'],source.read_text())
                self.assertTrue(row['original_preview'].startswith('data:image/png;base64,'))
                self.assertEqual([p.get('d') for p in list(ET.fromstring(row['outline']))[0]],glyphs[row['icon_id']]['paths'])
