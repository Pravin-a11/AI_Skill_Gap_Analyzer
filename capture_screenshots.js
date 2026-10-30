const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const mediaDir = 'C:/Users/stark/.gemini/antigravity/brain/680b47f6-1470-4262-a360-a8edb8303c79/scratch/docx_content/word/media';
const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';

async function capture() {
  console.log('Launching browser...');
  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--window-size=1600,1050']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1600, height: 1050 });

  console.log('Navigating to http://localhost:5000...');
  await page.goto('http://localhost:5000', { waitUntil: 'networkidle2' });

  // 1. Wait a moment for initial load & trigger analysis
  await new Promise(r => setTimeout(r, 1500));

  // Click Execute Skill Gap & Career Agent
  await page.evaluate(() => {
    if (typeof triggerAnalysis === 'function') {
      triggerAnalysis();
    }
  });

  await new Promise(r => setTimeout(r, 1500));

  // Capture Figure 5.4.1: Dashboard Recommendation View (image6.jpg)
  const pathImg6 = path.join(mediaDir, 'image6.jpg');
  console.log('Capturing Figure 5.4.1 (image6.jpg)...');
  await page.screenshot({ path: pathImg6, type: 'jpeg', quality: 95 });

  // 2. Switch to 2-Year Financials Tab
  await page.evaluate(() => {
    if (typeof switchTab === 'function') {
      switchTab('financial');
    }
  });
  await new Promise(r => setTimeout(r, 800));

  // Capture Figure 8.2.1: Financial Dashboard (image7.jpg)
  const pathImg7 = path.join(mediaDir, 'image7.jpg');
  console.log('Capturing Figure 8.2.1 (image7.jpg)...');
  await page.screenshot({ path: pathImg7, type: 'jpeg', quality: 95 });

  // 3. Switch to AI Counselor Tab and send a message
  await page.evaluate(() => {
    if (typeof switchTab === 'function') {
      switchTab('counselor');
      if (typeof sendQuickPrompt === 'function') {
        sendQuickPrompt('Why is RWTH Aachen marked as SAFE?');
      }
    }
  });
  await new Promise(r => setTimeout(r, 1500));

  // Capture Figure 8.2.2: AI Counselor Chatbot (image8.jpg)
  const pathImg8 = path.join(mediaDir, 'image8.jpg');
  console.log('Capturing Figure 8.2.2 (image8.jpg)...');
  await page.screenshot({ path: pathImg8, type: 'jpeg', quality: 95 });

  await browser.close();
  console.log('ALL SCREENSHOTS CAPTURED AND REPLACED SUCCESSFULLY!');
}

capture().catch(err => {
  console.error('Capture error:', err);
  process.exit(1);
});
