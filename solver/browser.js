try {
    const fs = require('fs'); const puppeteer = require('puppeteer-extra'); const crypto = require("crypto"); const StealthPlugin = require('puppeteer-extra-plugin-stealth'); const tmp = require('tmp'); const express = require("express"); const { execSync } = require('child_process');
} catch {
    console.log("Installing modules")
    const { execSync } = require('child_process'); execSync("npm install puppeteer-extra"); execSync("npm install crypto"); execSync("npm install puppeteer-extra-plugin-stealth"); execSync("npm install tmp");
}

const fs = require('fs'); const puppeteer = require('puppeteer-extra'); const crypto = require("crypto"); const StealthPlugin = require('puppeteer-extra-plugin-stealth'); const tmp = require('tmp'); const express = require("express"); const { execSync } = require('child_process');
puppeteer.use(StealthPlugin())
const random_int = (min, max) => { return Math.floor(Math.random() * (max - min) + min) }

let total_hsws = 0;

async function create_browser() {
    var tmpobj = tmp.dirSync();
    var tempDirPath = tmpobj.name.replace(tmpobj.name.split("\\")[tmpobj.name.split("\\").length - 1], "")
    var chrome_profil_path = tempDirPath + crypto.randomBytes(20).toString('hex');
    var startPosition = random_int(0, 50).toString() + "," + random_int(0, 50).toString();
    var fingerprint_extention_path = `${process.cwd()}\\extensions\\fingerprint_extention`
    var brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    browser_args = [];

    browser_args.push(`--user-data-dir="${chrome_profil_path}"`)
    browser_args.push('--lang=en')
    browser_args.push(`--load-extension=${fingerprint_extention_path}`)
    browser_args.push(`--window-position=${startPosition}`)
    browser_args.push('--disable-setuid-sandbox')
    browser_args.push('--disable-dev-shm-usage')
    browser_args.push('--disable-accelerated-2d-canvas')
    browser_args.push('--no-zygote')
    browser_args.push('--disable-gpu')
    browser_args.push(`--window-size=500,500`)
    browser_args.push('about:blank')
    browser_args.push('--headless')

    var browser = await puppeteer.launch({ args: browser_args, executablePath: brave_path, headless: false });
    var [page] = await browser.pages()

    await page.evaluate(fs.readFileSync('extensions/hsw.js', 'utf8'))
    console.log(`[+] Browser Started Successfully`)

    return page
}

async function start_server() {
    var server = express()
    var browser1 = await create_browser()
    var browser2 = await create_browser()
    var browser3 = await create_browser()
    var browser4 = await create_browser()
    var browser5 = await create_browser()
    var browser6 = await create_browser()
    var browser7 = await create_browser()
    var browser8 = await create_browser()
    var browser9 = await create_browser()
    var browser10 = await create_browser()
    var browsers = [browser1, browser2, browser3, browser4, browser5, browser6, browser7, browser8, browser9, browser10]

    server.get('/bypass', async (req, res) => {
        try {
            var d = new Date();
            var n = d.getHours();
            var m = d.getMinutes();
            var s = d.getSeconds();
            
            
            let query = req.query
            console.log(`(${n}:${m}:${s}) [DEBUG] ${query.hsw}`)
            brwtouse = browsers[Math.floor(Math.random()* browsers.length)]
            let tosenddata = await brwtouse.evaluate('hsw(\'' + req.query.hsw + '\')');
            total_hsws = total_hsws + 1;
            execSync(`title ^[Hsw Server ^- void.#1337^] ^- Status : Online | BrowserType : Brave ^| Flagged : false ^| Requests Received : ${total_hsws + 2} ^| Hsw(s) Solved : ${total_hsws} ^| Browsers : 10`.replace(`|`, `^|`))
            return res.send(tosenddata);
        } catch (err) {
            console.error(err);
            return res.send({ error: `${err.message}` });
        }
    });

    server.listen(2030)
    console.log(`[+] Server Started On Port 2030`)
}

(async () => {
    await start_server();
})()