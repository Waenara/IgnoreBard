# Ignore-Bard

Discord self bot to ignore users using google bard.

## Install
> [!NOTE]
> Make sure you have python3 installed.

1. Download project files. [Download](https://github.com/Waenara/IgnoreBard/archive/refs/heads/master.zip)
2. Extract files from archive.
3. Open and fill users.txt
```
--Enter here id of users you want to ignore!
--Example:
1125078080046768138
```
4. Open and fill config.json
```
{
  "token-discord": "Enter your discord token here", 
  "token-bard": "Enter google bard cookie here"
}
```
5. Run start.bat
6. You're done! 😃

## Getting discord token

1. Visit https://discord.com/app
2. Open developer tools in browser (if you using desktop app use Ctrl+Shift+I shortcut)
3. Switch current tab to Console
4. Write this code and press enter
```js
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
It returns your current discord account token



## Getting bard cookie


> [!WARNING]
> Do not expose the `__Secure-1PSID` 
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

## Questions
If you have any questions to me you can use:
- `Issues` on github.
- Discord: `waenara`

