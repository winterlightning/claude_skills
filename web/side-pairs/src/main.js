// Progression › Side combination and the Side pair card on a combination primitive, as Svelte components. Loaded by
// primitives.html after the plain scripts they use (side-pairs-data.js as window.SideData, combine-side.js,
// side-repair-flags.js, side-combination-popup.js, side-component-editor.js).
import {mount, unmount} from 'svelte';
import App from './components/App.svelte';
import PairSection from './components/PairSection.svelte';
import {SideStore} from './lib/store.svelte.js';
import {LayoutEditor} from './lib/editor.svelte.js';
import {forms} from './lib/picker.svelte.js';
import './styles/row.css';
import './styles/part.css';
import './styles/summary.css';
import './styles/picker.css';
import './styles/editor.css';

// Read when this script loaded: the page rewrites its URL from its own state before the pairs arrive.
const params = new URLSearchParams(location.search);
let app = null, store = null;
const editor = new LayoutEditor();

// A redrawn or approved main / sub changes statuses everywhere: read everything again.
window.addEventListener('side-component-approved', () => { if (store) { store.rendered.clear();store.load(); } });
// A part marked for repair (or cleared) changes the Fix badges and states.
document.addEventListener('side-repair-flags-change', () => store?.touch());

// `page`: Progression's search text, page number and URL writer ({query, setQuery, page, setPage, writeURL}).
export function show(host, page) {
  if (app && host.contains(app.host)) return;
  if (app) unmount(app.component);
  store ??= new SideStore(params.get('grid') === '72' ? 72 : 64);
  if (!store.ready && !store.loading) store.load();
  const element = document.createElement('div');host.replaceChildren(element);
  app = {host: element, component: mount(App, {target: element, props: {store, editor, page, params}})};
}
export function hide() { if (app) { unmount(app.component);app = null; } }

// The Side pair card on a combination primitive (Progression › Review icons). The card is removed with its detail
// view; its component goes with it.
const cards = new Set();
function section(row) {
  for (const card of [...cards]) if (!card.element.isConnected) { unmount(card.component);cards.delete(card); }
  const element = document.createElement('div');element.className = 'side-pair-card';
  cards.add({element, component: mount(PairSection, {target: element, props: {row}})});
  return element;
}
window.SidePairMaker = {section, editing: () => forms.size > 0};
