const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    ignoreHTTPSErrors: true,
    args: [`--window-size=1400,1900`],
    defaultViewport: {
      width:1400,
      height:1900
    }
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:3000/', {timeout: 60000});
  await page.evaluate(async() => {
    await new Promise(function(resolve) { 
           setTimeout(resolve, 4000)
    });
    const toClick = document.querySelector('#root > div > div > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(14) > div > div:nth-child(3) > div > button:nth-child(3)');
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
    toClick.click();
    await new Promise(function(resolve) {setTimeout(resolve, 1000)});
  });
  
  await page.screenshot({ path: 'fullpage.png', fullPage: true });

  await browser.close();
})();