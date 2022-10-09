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
  await page.setDefaultNavigationTimeout(60000);
  await page.goto('http://localhost:3000/', {timeout: 40000});
  await page.evaluate(async() => {
    await new Promise(function(resolve) { 
           setTimeout(resolve, 4000)
    });
});
  await page.screenshot({ path: 'fullpage.png', fullPage: true });

  await browser.close();
})();