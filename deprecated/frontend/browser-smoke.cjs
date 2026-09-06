'use strict';

// Read-only browser integration check. Requires a running local profile server
// and Playwright/Chromium. All PUT requests are blocked; custom profiles exist
// only in this browser's unsaved Profile Manager draft.
// PROFILE_MANAGER_URL=http://127.0.0.1:PORT/?token=... node frontend/browser-smoke.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

(async () => {
  if (!process.env.PROFILE_MANAGER_URL) throw new Error('Set PROFILE_MANAGER_URL to the running local manager URL.');
  const startURL = new URL(process.env.PROFILE_MANAGER_URL);
  if (!['127.0.0.1', 'localhost'].includes(startURL.hostname)) throw new Error('This check only targets a local server.');
  const sourcePath = path.join(__dirname, '../core/icon_profiles.json'), before = fs.readFileSync(sourcePath, 'utf8');
  const browser = await chromium.launch({ headless: true, ...(process.env.CHROMIUM_EXECUTABLE ? { executablePath: process.env.CHROMIUM_EXECUTABLE } : {}) });
  try {
    const context = await browser.newContext({ viewport: { width: 1440, height: 1100 } }), page = await context.newPage(), errors = [];
    context.setDefaultTimeout(10000);
    context.on('page', next => next.on('pageerror', error => errors.push(error.message)));
    page.on('pageerror', error => errors.push(error.message));
    page.on('dialog', dialog => dialog.accept());
    await context.route('**/api/profiles', route => route.request().method() === 'PUT' ? route.abort('blockedbyclient') : route.continue());
    await page.goto(startURL.href);
    await page.getByText('Loaded canonical configuration.', { exact: true }).waitFor();
    assert.equal(await page.locator('#profile-native').getAttribute('width'), '48');
    await page.getByLabel('New profile id', { exact: true }).fill('toolbar-test');
    await page.getByRole('button', { name: 'Add', exact: true }).click();
    await page.getByLabel('Display label', { exact: true }).fill('Toolbar test');
    await page.getByLabel('Native canvas (px)', { exact: true }).fill('80');
    await page.getByLabel('Stroke width (u = px)', { exact: true }).fill('6');
    await page.getByLabel('Grid step', { exact: true }).first().fill('2');
    await page.getByLabel('Major grid step', { exact: true }).first().fill('8');
    assert.equal(await page.locator('#profile-native').getAttribute('width'), '80');
    assert.match(await page.locator('#preview-summary').innerText(), /6u stroke · 2u grid/);
    assert.equal(await page.getByRole('button', { name: 'Save configuration', exact: true }).isEnabled(), true);
    await page.getByLabel('Stroke width (u = px)', { exact: true }).fill('0');
    assert.equal(await page.getByRole('button', { name: 'Save configuration', exact: true }).isEnabled(), false);
    assert.equal(await page.locator('#validation-errors').isVisible(), true);
    await page.getByLabel('Stroke width (u = px)', { exact: true }).fill('6');
    await page.getByRole('button', { name: 'Edit complete JSON', exact: true }).click();
    const draft = JSON.parse(await page.getByLabel('Complete profile configuration JSON', { exact: true }).inputValue());
    assert.equal(draft.profiles['toolbar-test'].canvas, 80);
    assert.equal(draft.profiles['toolbar-test'].strokeWidth, 6);
    assert.equal(draft.profiles['toolbar-test'].validation.gridStep, 2);
    const outputDir = fs.mkdtempSync(path.join(os.tmpdir(), 'icon-profile-browser-'));
    await page.getByRole('button', { name: 'Edit complete JSON', exact: true }).click();
    await page.screenshot({ path: path.join(outputDir, 'manager.png') });
    assert.equal(await page.getByRole('link', { name: /Open icon editor/ }).count(), 0);
    assert.deepEqual(errors, []); assert.equal(fs.readFileSync(sourcePath, 'utf8'), before);
    console.log('Browser checks passed: draft profile editing, invalid-save lock, raw JSON, configured stroke/native-size preview. No configuration writes.');
    console.log(`Screenshots: ${outputDir}`);
  } finally { await browser.close(); }
})().catch(error => { console.error(error.message); process.exitCode = 1; });
