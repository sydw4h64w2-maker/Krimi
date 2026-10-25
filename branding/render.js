const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
  await p.goto('file://' + process.argv[2]); await p.screenshot({ path: process.argv[3] });
  // Vorschau als Kreis (so zeigt TikTok es an)
  await p.addStyleTag({ content: 'html{background:#fff} body{border-radius:50%;}' });
  await p.screenshot({ path: process.argv[4], omitBackground: false });
  await b.close();
})();
