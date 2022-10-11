const express = require('express')
const app = express()
const port = 4000
const puppeteer = require('puppeteer');


app.get('/', (req, res) => {
	console.log('creating the file...')
	puppeteer.launch({
		headless: true,
		ignoreHTTPSErrors: true,
		args: [`--window-size=1400,1900`],
		defaultViewport: {
			width:1400,
			height:1900
		}
	}).then(async browser => {
		const page = await browser.newPage();
		await page.goto('http://localhost:3000/', {timeout: 60000});
		await page.evaluate(async() => {
			await new Promise(function(resolve) { 
				setTimeout(resolve, 3000)
			});
			const toClick = document.querySelector('#root > div > div > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(14) > div > div:nth-child(3) > div > button:nth-child(3)');
			toClick.click();
			await new Promise(function(resolve) {setTimeout(resolve, 500)});
			toClick.click();
			await new Promise(function(resolve) {setTimeout(resolve, 500)});
			toClick.click();
			await new Promise(function(resolve) {setTimeout(resolve, 500)});
			toClick.click();
			await new Promise(function(resolve) {setTimeout(resolve, 500)});
			toClick.click();
			await new Promise(function(resolve) {setTimeout(resolve, 500)});
			toClick.click();
			await new Promise(function(resolve) {setTimeout(resolve, 500)});
			toClick.click();
		});
		  
		await page.screenshot({ path: '../loopController/static/fullpage.png', fullPage: true });
		
		await browser.close();
		console.log('done');
		res.status(200).send('Done');
	}).catch(err => {
		console.log(err)
		res.status(500).send('Error');
	});
})

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})