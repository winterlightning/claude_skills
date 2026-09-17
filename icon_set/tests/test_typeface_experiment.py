import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from icon_set.scripts.experiment_gallery import typeface_samples


class TypefaceExperimentTests(unittest.TestCase):
    def test_centerlines_keep_exact_paths(self):
        glyphs=json.loads((Path(__file__).resolve().parents[1]/'dist/gallery/typeface.json').read_text())['glyphs']
        rows=typeface_samples(glyphs)
        self.assertEqual(len(rows),95)
        self.assertEqual(len({r['key'] for r in rows}),95)
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
        root=Path(__file__).resolve().parents[1]/'dist/gallery'
        html=(root/'experiment.html').read_text()
        self.assertNotIn('__TYPEFACE_EXPERIMENT_DATA__',html)
        payload=html.split('<script id="typefaceExperimentData" type="application/json">')[1].split('</script>')[0]
        self.assertEqual(len(json.loads(payload)['icons']),95)
        js=(root/'experiment.js').read_text()
        self.assertIn("review.href='text-combine.html'",js)
        self.assertIn("type==='typeface'?Math.max(1,filtered.length):pageSize",js)

    def test_originals_use_source_files_and_uppercase_has_none(self):
        root=Path(__file__).resolve().parents[2]
        rows=json.loads((root/'icon_set/dist/gallery/experiment-typeface.json').read_text())['icons']
        originals=[r for r in rows if r['original'] is not None]
        self.assertEqual(len(originals),37)
        for row in rows:
            with self.subTest(icon=row['icon_id']):
                if row['icon_id'].endswith('-uppercase') or row['icon_id'].startswith('symbol-'):
                    self.assertIsNone(row['original'])
                    self.assertIsNone(row['original_preview'])
                else:
                    self.assertEqual(row['original'],(root/'Letters'/row['original_name']).read_text())
                    self.assertTrue(row['original_preview'].startswith('data:image/png;base64,'))
                self.assertTrue(row['outline_preview'].startswith('data:image/png;base64,'))
        self.assertEqual(next(r for r in rows if r['icon_id']=='letter-o-large')['original_name'],'o.svg')
        self.assertEqual(next(r for r in rows if r['icon_id']=='letter-o')['original_name'],'o-1.svg')
