import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf8')


headers = {'User-Agent': 'Mozilla/5.0'}
main_url = 'https://www.ldoceonline.com/dictionary/english-japanese/'
word = input('\r\n')
url = requests.get(main_url + word, headers=headers).text
soup = BeautifulSoup(url, 'lxml')


css = """<style type="text/css">


/*!
 * # Semantic UI 2.2.11 - Dropdown
 * http://github.com/semantic-org/semantic-ui/
 *
 *
 * Released under the MIT license
 * http://opensource.org/licenses/MIT
 *
 */.ui.dropdown{cursor:pointer;position:relative;display:inline-block;outline:0;text-align:left;-webkit-transition:box-shadow .1s ease,width .1s ease;transition:box-shadow .1s ease,width .1s ease;-webkit-tap-highlight-color:transparent}.ui.dropdown .menu{cursor:auto;position:absolute;display:none;outline:0;top:100%;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;margin:0;padding:0 0;background:#fff;font-size:1em;text-shadow:none;text-align:left;box-shadow:0 2px 3px 0 rgba(34,36,38,.15);border:1px solid rgba(34,36,38,.15);border-radius:.28571429rem;-webkit-transition:opacity .1s ease;transition:opacity .1s ease;z-index:11;will-change:transform,opacity}.ui.dropdown .menu>*{white-space:nowrap}.ui.dropdown>input:not(.search):first-child,.ui.dropdown>select{display:none!important}.ui.dropdown>.dropdown.icon{position:relative;width:auto;font-size:.85714286em;margin:0 0 0 1em}.ui.dropdown .menu>.item .dropdown.icon{width:auto;float:right;margin:0 0 0 1em}.ui.dropdown .menu>.item .dropdown.icon+.text{margin-right:1em}.ui.dropdown>.text{display:inline-block;-webkit-transition:none;transition:none}.ui.dropdown .menu>.item{position:relative;cursor:pointer;display:block;border:none;height:auto;text-align:left;border-top:none;line-height:1em;color:rgba(0,0,0,.87);padding:.78571429rem 1.14285714rem!important;font-size:1rem;text-transform:none;font-weight:400;box-shadow:none;-webkit-touch-callout:none}.ui.dropdown .menu>.item:first-child{border-top-width:0}.ui.dropdown .menu .item>[class*="right floated"],.ui.dropdown>.text>[class*="right floated"]{float:right!important;margin-right:0!important;margin-left:1em!important}.ui.dropdown .menu .item>[class*="left floated"],.ui.dropdown>.text>[class*="left floated"]{float:left!important;margin-left:0!important;margin-right:1em!important}.ui.dropdown .menu .item>.flag.floated,.ui.dropdown .menu .item>.icon.floated,.ui.dropdown .menu .item>.image.floated,.ui.dropdown .menu .item>img.floated{margin-top:0}.ui.dropdown .menu>.header{margin:1rem 0 .75rem;padding:0 1.14285714rem;color:rgba(0,0,0,.85);font-size:.78571429em;font-weight:700;text-transform:uppercase}.ui.dropdown .menu>.divider{border-top:1px solid rgba(34,36,38,.1);height:0;margin:.5em 0}.ui.dropdown .menu>.input{width:auto;display:-webkit-box;display:-ms-flexbox;display:flex;margin:1.14285714rem .78571429rem;min-width:10rem}.ui.dropdown .menu>.header+.input{margin-top:0}.ui.dropdown .menu>.input:not(.transparent) input{padding:.5em 1em}.ui.dropdown .menu>.input:not(.transparent) .button,.ui.dropdown .menu>.input:not(.transparent) .icon,.ui.dropdown .menu>.input:not(.transparent) .label{padding-top:.5em;padding-bottom:.5em}.ui.dropdown .menu>.item>.description,.ui.dropdown>.text>.description{float:right;margin:0 0 0 1em;color:rgba(0,0,0,.4)}.ui.dropdown .menu>.message{padding:.78571429rem 1.14285714rem;font-weight:400}.ui.dropdown .menu>.message:not(.ui){color:rgba(0,0,0,.4)}.ui.dropdown .menu .menu{top:0!important;left:100%;right:auto;margin:0 0 0 -.5em!important;border-radius:.28571429rem!important;z-index:21!important}.ui.dropdown .menu .menu:after{display:none}.ui.dropdown>.text>.flag,.ui.dropdown>.text>.icon,.ui.dropdown>.text>.image,.ui.dropdown>.text>.label,.ui.dropdown>.text>img{margin-top:0}.ui.dropdown .menu>.item>.flag,.ui.dropdown .menu>.item>.icon,.ui.dropdown .menu>.item>.image,.ui.dropdown .menu>.item>.label,.ui.dropdown .menu>.item>img{margin-top:0}.ui.dropdown .menu>.item>.flag,.ui.dropdown .menu>.item>.icon,.ui.dropdown .menu>.item>.image,.ui.dropdown .menu>.item>.label,.ui.dropdown .menu>.item>img,.ui.dropdown>.text>.flag,.ui.dropdown>.text>.icon,.ui.dropdown>.text>.image,.ui.dropdown>.text>.label,.ui.dropdown>.text>img{margin-left:0;float:none;margin-right:.78571429rem}.ui.dropdown .menu>.item>.image,.ui.dropdown .menu>.item>img,.ui.dropdown>.text>.image,.ui.dropdown>.text>img{display:inline-block;vertical-align:top;width:auto;margin-top:-.5em;margin-bottom:-.5em;max-height:2em}.ui.dropdown .ui.menu>.item:before,.ui.menu .ui.dropdown .menu>.item:before{display:none}.ui.menu .ui.dropdown .menu .active.item{border-left:none}.ui.buttons>.ui.dropdown:last-child .menu,.ui.menu .right.dropdown.item .menu,.ui.menu .right.menu .dropdown:last-child .menu{left:auto;right:0}.ui.label.dropdown .menu{min-width:100%}.ui.dropdown.icon.button>.dropdown.icon{margin:0}.ui.button.dropdown .menu{min-width:100%}.ui.selection.dropdown{cursor:pointer;word-wrap:break-word;line-height:1em;white-space:normal;outline:0;-webkit-transform:rotateZ(0);transform:rotateZ(0);min-width:14em;min-height:2.71428571em;background:#fff;display:inline-block;padding:.78571429em 2.1em .78571429em 1em;color:rgba(0,0,0,.87);box-shadow:none;border:1px solid rgba(34,36,38,.15);border-radius:.28571429rem;-webkit-transition:box-shadow .1s ease,width .1s ease;transition:box-shadow .1s ease,width .1s ease}.ui.selection.dropdown.active,.ui.selection.dropdown.visible{z-index:10}select.ui.dropdown{height:38px;padding:.5em;border:1px solid rgba(34,36,38,.15);visibility:visible}.ui.selection.dropdown>.delete.icon,.ui.selection.dropdown>.dropdown.icon,.ui.selection.dropdown>.search.icon{cursor:pointer;position:absolute;width:auto;height:auto;line-height:1.21428571em;top:.78571429em;right:1em;z-index:3;margin:-.78571429em;padding:.91666667em;opacity:.8;-webkit-transition:opacity .1s ease;transition:opacity .1s ease}.ui.compact.selection.dropdown{min-width:0}.ui.selection.dropdown .menu{overflow-x:hidden;overflow-y:auto;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-overflow-scrolling:touch;border-top-width:0!important;width:auto;outline:0;margin:0 -1px;min-width:calc(100% + 2px);width:calc(100% + 2px);border-radius:0 0 .28571429rem .28571429rem;box-shadow:0 2px 3px 0 rgba(34,36,38,.15);-webkit-transition:opacity .1s ease;transition:opacity .1s ease}.ui.selection.dropdown .menu:after,.ui.selection.dropdown .menu:before{display:none}.ui.selection.dropdown .menu>.message{padding:.78571429rem 1.14285714rem}@media only screen and (max-width:767px){.ui.selection.dropdown .menu{max-height:8.01428571rem}}@media only screen and (min-width:768px){.ui.selection.dropdown .menu{max-height:10.68571429rem}}@media only screen and (min-width:992px){.ui.selection.dropdown .menu{max-height:16.02857143rem}}@media only screen and (min-width:1920px){.ui.selection.dropdown .menu{max-height:21.37142857rem}}.ui.selection.dropdown .menu>.item{border-top:1px solid #fafafa;padding:.78571429rem 1.14285714rem!important;white-space:normal;word-wrap:normal}.ui.selection.dropdown .menu>.hidden.addition.item{display:none}.ui.selection.dropdown:hover{border-color:rgba(34,36,38,.35);box-shadow:none}.ui.selection.active.dropdown{border-color:#96c8da;box-shadow:0 2px 3px 0 rgba(34,36,38,.15)}.ui.selection.active.dropdown .menu{border-color:#96c8da;box-shadow:0 2px 3px 0 rgba(34,36,38,.15)}.ui.selection.dropdown:focus{border-color:#96c8da;box-shadow:none}.ui.selection.dropdown:focus .menu{border-color:#96c8da;box-shadow:0 2px 3px 0 rgba(34,36,38,.15)}.ui.selection.visible.dropdown>.text:not(.default){font-weight:400;color:rgba(0,0,0,.8)}.ui.selection.active.dropdown:hover{border-color:#96c8da;box-shadow:0 2px 3px 0 rgba(34,36,38,.15)}.ui.selection.active.dropdown:hover .menu{border-color:#96c8da;box-shadow:0 2px 3px 0 rgba(34,36,38,.15)}.ui.active.selection.dropdown>.dropdown.icon,.ui.visible.selection.dropdown>.dropdown.icon{opacity:1;z-index:3}.ui.active.selection.dropdown{border-bottom-left-radius:0!important;border-bottom-right-radius:0!important}.ui.active.empty.selection.dropdown{border-radius:.28571429rem!important;box-shadow:none!important}.ui.active.empty.selection.dropdown .menu{border:none!important;box-shadow:none!important}.ui.search.dropdown{min-width:''}.ui.search.dropdown>input.search{background:none transparent!important;border:none!important;box-shadow:none!important;cursor:text;top:0;left:1px;width:100%;outline:0;-webkit-tap-highlight-color:rgba(255,255,255,0);padding:inherit}.ui.search.dropdown>input.search{position:absolute;z-index:2}.ui.search.dropdown>.text{cursor:text;position:relative;left:1px;z-index:3}.ui.search.selection.dropdown>input.search{line-height:1.21428571em;padding:.67857143em 2.1em .67857143em 1em}.ui.search.selection.dropdown>span.sizer{line-height:1.21428571em;padding:.67857143em 2.1em .67857143em 1em;display:none;white-space:pre}.ui.search.dropdown.active>input.search,.ui.search.dropdown.visible>input.search{cursor:auto}.ui.search.dropdown.active>.text,.ui.search.dropdown.visible>.text{pointer-events:none}.ui.active.search.dropdown input.search:focus+.text .flag,.ui.active.search.dropdown input.search:focus+.text .icon{opacity:.45}.ui.active.search.dropdown input.search:focus+.text{color:rgba(115,115,115,.87)!important}.ui.search.dropdown .menu{overflow-x:hidden;overflow-y:auto;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-overflow-scrolling:touch}@media only screen and (max-width:767px){.ui.search.dropdown .menu{max-height:8.01428571rem}}@media only screen and (min-width:768px){.ui.search.dropdown .menu{max-height:10.68571429rem}}@media only screen and (min-width:992px){.ui.search.dropdown .menu{max-height:16.02857143rem}}@media only screen and (min-width:1920px){.ui.search.dropdown .menu{max-height:21.37142857rem}}.ui.multiple.dropdown{padding:.22619048em 2.1em .22619048em .35714286em}.ui.multiple.dropdown .menu{cursor:auto}.ui.multiple.search.dropdown,.ui.multiple.search.dropdown>input.search{cursor:text}.ui.multiple.dropdown>.label{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;display:inline-block;vertical-align:top;white-space:normal;font-size:1em;padding:.35714286em .78571429em;margin:.14285714rem .28571429rem .14285714rem 0;box-shadow:0 0 0 1px rgba(34,36,38,.15) inset}.ui.multiple.dropdown .dropdown.icon{margin:'';padding:''}.ui.multiple.dropdown>.text{position:static;padding:0;max-width:100%;margin:.45238095em 0 .45238095em .64285714em;line-height:1.21428571em}.ui.multiple.dropdown>.label~input.search{margin-left:.14285714em!important}.ui.multiple.dropdown>.label~.text{display:none}.ui.multiple.search.dropdown>.text{display:inline-block;position:absolute;top:0;left:0;padding:inherit;margin:.45238095em 0 .45238095em .64285714em;line-height:1.21428571em}.ui.multiple.search.dropdown>.label~.text{display:none}.ui.multiple.search.dropdown>input.search{position:static;padding:0;max-width:100%;margin:.45238095em 0 .45238095em .64285714em;width:2.2em;line-height:1.21428571em}.ui.inline.dropdown{cursor:pointer;display:inline-block;color:inherit}.ui.inline.dropdown .dropdown.icon{margin:0 .5em 0 .21428571em;vertical-align:baseline}.ui.inline.dropdown>.text{font-weight:700}.ui.inline.dropdown .menu{cursor:auto;margin-top:.21428571em;border-radius:.28571429rem}.ui.dropdown .menu .active.item{background:0 0;font-weight:700;color:rgba(0,0,0,.95);box-shadow:none;z-index:12}.ui.dropdown .menu>.item:hover{background:rgba(0,0,0,.05);color:rgba(0,0,0,.95);z-index:13}.ui.loading.dropdown>i.icon{height:1em!important}.ui.loading.selection.dropdown>i.icon{padding:1.5em 1.28571429em!important}.ui.loading.dropdown>i.icon:before{position:absolute;content:'';top:50%;left:50%;margin:-.64285714em 0 0 -.64285714em;width:1.28571429em;height:1.28571429em;border-radius:500rem;border:.2em solid rgba(0,0,0,.1)}.ui.loading.dropdown>i.icon:after{position:absolute;content:'';top:50%;left:50%;box-shadow:0 0 0 1px transparent;margin:-.64285714em 0 0 -.64285714em;width:1.28571429em;height:1.28571429em;-webkit-animation:dropdown-spin .6s linear;animation:dropdown-spin .6s linear;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;border-radius:500rem;border-color:#767676 transparent transparent;border-style:solid;border-width:.2em}.ui.loading.dropdown.button>i.icon:after,.ui.loading.dropdown.button>i.icon:before{display:none}@-webkit-keyframes dropdown-spin{from{-webkit-transform:rotate(0);transform:rotate(0)}to{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes dropdown-spin{from{-webkit-transform:rotate(0);transform:rotate(0)}to{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.ui.default.dropdown:not(.button)>.text,.ui.dropdown:not(.button)>.default.text{color:rgba(191,191,191,.87)}.ui.default.dropdown:not(.button)>input:focus+.text,.ui.dropdown:not(.button)>input:focus+.default.text{color:rgba(115,115,115,.87)}.ui.loading.dropdown>.text{-webkit-transition:none;transition:none}.ui.dropdown .loading.menu{display:block;visibility:hidden;z-index:-1}.ui.dropdown>.loading.menu{left:0!important;right:auto!important}.ui.dropdown>.menu .loading.menu{left:100%!important;right:auto!important}.ui.dropdown .menu .selected.item,.ui.dropdown.selected{background:rgba(0,0,0,.03);color:rgba(0,0,0,.95)}.ui.dropdown>.filtered.text{visibility:hidden}.ui.dropdown .filtered.item{display:none!important}.ui.dropdown.error,.ui.dropdown.error>.default.text,.ui.dropdown.error>.text{color:#9f3a38}.ui.selection.dropdown.error{background:#fff6f6;border-color:#e0b4b4}.ui.selection.dropdown.error:hover{border-color:#e0b4b4}.ui.dropdown.error>.menu,.ui.dropdown.error>.menu .menu{border-color:#e0b4b4}.ui.dropdown.error>.menu>.item{color:#9f3a38}.ui.multiple.selection.error.dropdown>.label{border-color:#e0b4b4}.ui.dropdown.error>.menu>.item:hover{background-color:#fff2f2}.ui.dropdown.error>.menu .active.item{background-color:#fdcfcf}.ui.disabled.dropdown,.ui.dropdown .menu>.disabled.item{cursor:default;pointer-events:none;opacity:.45}.ui.dropdown .menu{left:0}.ui.dropdown .menu .right.menu,.ui.dropdown .right.menu>.menu{left:100%!important;right:auto!important;border-radius:.28571429rem!important}.ui.dropdown>.left.menu{left:auto!important;right:0!important}.ui.dropdown .menu .left.menu,.ui.dropdown>.left.menu .menu{left:auto;right:100%;margin:0 -.5em 0 0!important;border-radius:.28571429rem!important}.ui.dropdown .item .left.dropdown.icon,.ui.dropdown .left.menu .item .dropdown.icon{width:auto;float:left;margin:0}.ui.dropdown .item .left.dropdown.icon,.ui.dropdown .left.menu .item .dropdown.icon{width:auto;float:left;margin:0}.ui.dropdown .item .left.dropdown.icon+.text,.ui.dropdown .left.menu .item .dropdown.icon+.text{margin-left:1em;margin-right:0}.ui.upward.dropdown>.menu{top:auto;bottom:100%;box-shadow:0 0 3px 0 rgba(0,0,0,.08);border-radius:.28571429rem .28571429rem 0 0}.ui.dropdown .upward.menu{top:auto!important;bottom:0!important}.ui.simple.upward.active.dropdown,.ui.simple.upward.dropdown:hover{border-radius:.28571429rem .28571429rem 0 0!important}.ui.upward.dropdown.button:not(.pointing):not(.floating).active{border-radius:.28571429rem .28571429rem 0 0}.ui.upward.selection.dropdown .menu{border-top-width:1px!important;border-bottom-width:0!important;box-shadow:0 -2px 3px 0 rgba(0,0,0,.08)}.ui.upward.selection.dropdown:hover{box-shadow:0 0 2px 0 rgba(0,0,0,.05)}.ui.active.upward.selection.dropdown{border-radius:0 0 .28571429rem .28571429rem!important}.ui.upward.selection.dropdown.visible{box-shadow:0 0 3px 0 rgba(0,0,0,.08);border-radius:0 0 .28571429rem .28571429rem!important}.ui.upward.active.selection.dropdown:hover{box-shadow:0 0 3px 0 rgba(0,0,0,.05)}.ui.upward.active.selection.dropdown:hover .menu{box-shadow:0 -2px 3px 0 rgba(0,0,0,.08)}.ui.dropdown .scrolling.menu,.ui.scrolling.dropdown .menu{overflow-x:hidden;overflow-y:auto}.ui.scrolling.dropdown .menu{overflow-x:hidden;overflow-y:auto;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-overflow-scrolling:touch;min-width:100%!important;width:auto!important}.ui.dropdown .scrolling.menu{position:static;overflow-y:auto;border:none;box-shadow:none!important;border-radius:0!important;margin:0!important;min-width:100%!important;width:auto!important;border-top:1px solid rgba(34,36,38,.15)}.ui.dropdown .scrolling.menu>.item.item.item,.ui.scrolling.dropdown .menu .item.item.item{border-top:none}.ui.dropdown .scrolling.menu .item:first-child,.ui.scrolling.dropdown .menu .item:first-child{border-top:none}.ui.dropdown>.animating.menu .scrolling.menu,.ui.dropdown>.visible.menu .scrolling.menu{display:block}@media all and (-ms-high-contrast:none){.ui.dropdown .scrolling.menu,.ui.scrolling.dropdown .menu{min-width:calc(100% - 17px)}}@media only screen and (max-width:767px){.ui.dropdown .scrolling.menu,.ui.scrolling.dropdown .menu{max-height:10.28571429rem}}@media only screen and (min-width:768px){.ui.dropdown .scrolling.menu,.ui.scrolling.dropdown .menu{max-height:15.42857143rem}}@media only screen and (min-width:992px){.ui.dropdown .scrolling.menu,.ui.scrolling.dropdown .menu{max-height:20.57142857rem}}@media only screen and (min-width:1920px){.ui.dropdown .scrolling.menu,.ui.scrolling.dropdown .menu{max-height:20.57142857rem}}.ui.simple.dropdown .menu:after,.ui.simple.dropdown .menu:before{display:none}.ui.simple.dropdown .menu{position:absolute;display:block;overflow:hidden;top:-9999px!important;opacity:0;width:0;height:0;-webkit-transition:opacity .1s ease;transition:opacity .1s ease}.ui.simple.active.dropdown,.ui.simple.dropdown:hover{border-bottom-left-radius:0!important;border-bottom-right-radius:0!important}.ui.simple.active.dropdown>.menu,.ui.simple.dropdown:hover>.menu{overflow:visible;width:auto;height:auto;top:100%!important;opacity:1}.ui.simple.dropdown:hover>.menu>.item:hover>.menu,.ui.simple.dropdown>.menu>.item:active>.menu{overflow:visible;width:auto;height:auto;top:0!important;left:100%!important;opacity:1}.ui.simple.disabled.dropdown:hover .menu{display:none;height:0;width:0;overflow:hidden}.ui.simple.visible.dropdown>.menu{display:block}.ui.fluid.dropdown{display:block;width:100%;min-width:0}.ui.fluid.dropdown>.dropdown.icon{float:right}.ui.floating.dropdown .menu{left:0;right:auto;box-shadow:0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.15)!important;border-radius:.28571429rem!important}.ui.floating.dropdown>.menu{margin-top:.5em!important;border-radius:.28571429rem!important}.ui.pointing.dropdown>.menu{top:100%;margin-top:.78571429rem;border-radius:.28571429rem}.ui.pointing.dropdown>.menu:after{display:block;position:absolute;pointer-events:none;content:'';visibility:visible;-webkit-transform:rotate(45deg);transform:rotate(45deg);width:.5em;height:.5em;box-shadow:-1px -1px 0 0 rgba(34,36,38,.15);background:#fff;z-index:2}.ui.pointing.dropdown>.menu:after{top:-.25em;left:50%;margin:0 0 0 -.25em}.ui.top.left.pointing.dropdown>.menu{top:100%;bottom:auto;left:0;right:auto;margin:1em 0 0}.ui.top.left.pointing.dropdown>.menu{top:100%;bottom:auto;left:0;right:auto;margin:1em 0 0}.ui.top.left.pointing.dropdown>.menu:after{top:-.25em;left:1em;right:auto;margin:0;-webkit-transform:rotate(45deg);transform:rotate(45deg)}.ui.top.right.pointing.dropdown>.menu{top:100%;bottom:auto;right:0;left:auto;margin:1em 0 0}.ui.top.pointing.dropdown>.left.menu:after,.ui.top.right.pointing.dropdown>.menu:after{top:-.25em;left:auto!important;right:1em!important;margin:0;-webkit-transform:rotate(45deg);transform:rotate(45deg)}.ui.left.pointing.dropdown>.menu{top:0;left:100%;right:auto;margin:0 0 0 1em}.ui.left.pointing.dropdown>.menu:after{top:1em;left:-.25em;margin:0;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.ui.left:not(.top):not(.bottom).pointing.dropdown>.left.menu{left:auto!important;right:100%!important;margin:0 1em 0 0}.ui.left:not(.top):not(.bottom).pointing.dropdown>.left.menu:after{top:1em;left:auto;right:-.25em;margin:0;-webkit-transform:rotate(135deg);transform:rotate(135deg)}.ui.right.pointing.dropdown>.menu{top:0;left:auto;right:100%;margin:0 1em 0 0}.ui.right.pointing.dropdown>.menu:after{top:1em;left:auto;right:-.25em;margin:0;-webkit-transform:rotate(135deg);transform:rotate(135deg)}.ui.bottom.pointing.dropdown>.menu{top:auto;bottom:100%;left:0;right:auto;margin:0 0 1em}.ui.bottom.pointing.dropdown>.menu:after{top:auto;bottom:-.25em;right:auto;margin:0;-webkit-transform:rotate(-135deg);transform:rotate(-135deg)}.ui.bottom.pointing.dropdown>.menu .menu{top:auto!important;bottom:0!important}.ui.bottom.left.pointing.dropdown>.menu{left:0;right:auto}.ui.bottom.left.pointing.dropdown>.menu:after{left:1em;right:auto}.ui.bottom.right.pointing.dropdown>.menu{right:0;left:auto}.ui.bottom.right.pointing.dropdown>.menu:after{left:auto;right:1em}.ui.pointing.upward.dropdown .menu,.ui.top.pointing.upward.dropdown .menu{top:auto!important;bottom:100%!important;margin:0 0 .78571429rem;border-radius:.28571429rem}.ui.pointing.upward.dropdown .menu:after,.ui.top.pointing.upward.dropdown .menu:after{top:100%!important;bottom:auto!important;box-shadow:1px 1px 0 0 rgba(34,36,38,.15);margin:-.25em 0 0}.ui.right.pointing.upward.dropdown:not(.top):not(.bottom) .menu{top:auto!important;bottom:0!important;margin:0 1em 0 0}.ui.right.pointing.upward.dropdown:not(.top):not(.bottom) .menu:after{top:auto!important;bottom:0!important;margin:0 0 1em 0;box-shadow:-1px -1px 0 0 rgba(34,36,38,.15)}.ui.left.pointing.upward.dropdown:not(.top):not(.bottom) .menu{top:auto!important;bottom:0!important;margin:0 0 0 1em}.ui.left.pointing.upward.dropdown:not(.top):not(.bottom) .menu:after{top:auto!important;bottom:0!important;margin:0 0 1em 0;box-shadow:-1px -1px 0 0 rgba(34,36,38,.15)}@font-face{font-family:Dropdown;src:url(data:application/x-font-ttf;charset=utf-8;base64,AAEAAAALAIAAAwAwT1MvMggjB5AAAAC8AAAAYGNtYXAPfuIIAAABHAAAAExnYXNwAAAAEAAAAWgAAAAIZ2x5Zjo82LgAAAFwAAABVGhlYWQAQ88bAAACxAAAADZoaGVhAwcB6QAAAvwAAAAkaG10eAS4ABIAAAMgAAAAIGxvY2EBNgDeAAADQAAAABJtYXhwAAoAFgAAA1QAAAAgbmFtZVcZpu4AAAN0AAABRXBvc3QAAwAAAAAEvAAAACAAAwIAAZAABQAAAUwBZgAAAEcBTAFmAAAA9QAZAIQAAAAAAAAAAAAAAAAAAAABEAAAAAAAAAAAAAAAAAAAAABAAADw2gHg/+D/4AHgACAAAAABAAAAAAAAAAAAAAAgAAAAAAACAAAAAwAAABQAAwABAAAAFAAEADgAAAAKAAgAAgACAAEAIPDa//3//wAAAAAAIPDX//3//wAB/+MPLQADAAEAAAAAAAAAAAAAAAEAAf//AA8AAQAAAAAAAAAAAAIAADc5AQAAAAABAAAAAAAAAAAAAgAANzkBAAAAAAEAAAAAAAAAAAACAAA3OQEAAAAAAQAAAIABJQElABMAABM0NzY3BTYXFhUUDwEGJwYvASY1AAUGBwEACAUGBoAFCAcGgAUBEgcGBQEBAQcECQYHfwYBAQZ/BwYAAQAAAG4BJQESABMAADc0PwE2MzIfARYVFAcGIyEiJyY1AAWABgcIBYAGBgUI/wAHBgWABwaABQWABgcHBgUFBgcAAAABABIASQC3AW4AEwAANzQ/ATYXNhcWHQEUBwYnBi8BJjUSBoAFCAcFBgYFBwgFgAbbBwZ/BwEBBwQJ/wgEBwEBB38GBgAAAAABAAAASQClAW4AEwAANxE0NzYzMh8BFhUUDwEGIyInJjUABQYHCAWABgaABQgHBgVbAQAIBQYGgAUIBwWABgYFBwAAAAEAAAABAADZuaKOXw889QALAgAAAAAA0ABHWAAAAADQAEdYAAAAAAElAW4AAAAIAAIAAAAAAAAAAQAAAeD/4AAAAgAAAAAAASUAAQAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAABAAAAASUAAAElAAAAtwASALcAAAAAAAAACgAUAB4AQgBkAIgAqgAAAAEAAAAIABQAAQAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAOAK4AAQAAAAAAAQAOAAAAAQAAAAAAAgAOAEcAAQAAAAAAAwAOACQAAQAAAAAABAAOAFUAAQAAAAAABQAWAA4AAQAAAAAABgAHADIAAQAAAAAACgA0AGMAAwABBAkAAQAOAAAAAwABBAkAAgAOAEcAAwABBAkAAwAOACQAAwABBAkABAAOAFUAAwABBAkABQAWAA4AAwABBAkABgAOADkAAwABBAkACgA0AGMAaQBjAG8AbQBvAG8AbgBWAGUAcgBzAGkAbwBuACAAMQAuADAAaQBjAG8AbQBvAG8Abmljb21vb24AaQBjAG8AbQBvAG8AbgBSAGUAZwB1AGwAYQByAGkAYwBvAG0AbwBvAG4ARgBvAG4AdAAgAGcAZQBuAGUAcgBhAHQAZQBkACAAYgB5ACAASQBjAG8ATQBvAG8AbgAuAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=) format('truetype'),url(data:application/font-woff;charset=utf-8;base64,d09GRk9UVE8AAAVwAAoAAAAABSgAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABDRkYgAAAA9AAAAdkAAAHZLDXE/09TLzIAAALQAAAAYAAAAGAIIweQY21hcAAAAzAAAABMAAAATA9+4ghnYXNwAAADfAAAAAgAAAAIAAAAEGhlYWQAAAOEAAAANgAAADYAQ88baGhlYQAAA7wAAAAkAAAAJAMHAelobXR4AAAD4AAAACAAAAAgBLgAEm1heHAAAAQAAAAABgAAAAYACFAAbmFtZQAABAgAAAFFAAABRVcZpu5wb3N0AAAFUAAAACAAAAAgAAMAAAEABAQAAQEBCGljb21vb24AAQIAAQA6+BwC+BsD+BgEHgoAGVP/i4seCgAZU/+LiwwHi2v4lPh0BR0AAACIDx0AAACNER0AAAAJHQAAAdASAAkBAQgPERMWGyAlKmljb21vb25pY29tb29udTB1MXUyMHVGMEQ3dUYwRDh1RjBEOXVGMERBAAACAYkABgAIAgABAAQABwAKAA0AVgCfAOgBL/yUDvyUDvyUDvuUDvtvi/emFYuQjZCOjo+Pj42Qiwj3lIsFkIuQiY6Hj4iNhouGi4aJh4eHCPsU+xQFiIiGiYaLhouHjYeOCPsU9xQFiI+Jj4uQCA77b4v3FBWLkI2Pjo8I9xT3FAWPjo+NkIuQi5CJjogI9xT7FAWPh42Hi4aLhomHh4eIiIaJhosI+5SLBYaLh42HjoiPiY+LkAgO+92d928Vi5CNkI+OCPcU9xQFjo+QjZCLkIuPiY6Hj4iNhouGCIv7lAWLhomHh4iIh4eJhouGi4aNiI8I+xT3FAWHjomPi5AIDvvdi+YVi/eUBYuQjZCOjo+Pj42Qi5CLkImOhwj3FPsUBY+IjYaLhouGiYeHiAj7FPsUBYiHhomGi4aLh42Hj4iOiY+LkAgO+JQU+JQViwwKAAAAAAMCAAGQAAUAAAFMAWYAAABHAUwBZgAAAPUAGQCEAAAAAAAAAAAAAAAAAAAAARAAAAAAAAAAAAAAAAAAAAAAQAAA8NoB4P/g/+AB4AAgAAAAAQAAAAAAAAAAAAAAIAAAAAAAAgAAAAMAAAAUAAMAAQAAABQABAA4AAAACgAIAAIAAgABACDw2v/9//8AAAAAACDw1//9//8AAf/jDy0AAwABAAAAAAAAAAAAAAABAAH//wAPAAEAAAABAAA5emozXw889QALAgAAAAAA0ABHWAAAAADQAEdYAAAAAAElAW4AAAAIAAIAAAAAAAAAAQAAAeD/4AAAAgAAAAAAASUAAQAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAABAAAAASUAAAElAAAAtwASALcAAAAAUAAACAAAAAAADgCuAAEAAAAAAAEADgAAAAEAAAAAAAIADgBHAAEAAAAAAAMADgAkAAEAAAAAAAQADgBVAAEAAAAAAAUAFgAOAAEAAAAAAAYABwAyAAEAAAAAAAoANABjAAMAAQQJAAEADgAAAAMAAQQJAAIADgBHAAMAAQQJAAMADgAkAAMAAQQJAAQADgBVAAMAAQQJAAUAFgAOAAMAAQQJAAYADgA5AAMAAQQJAAoANABjAGkAYwBvAG0AbwBvAG4AVgBlAHIAcwBpAG8AbgAgADEALgAwAGkAYwBvAG0AbwBvAG5pY29tb29uAGkAYwBvAG0AbwBvAG4AUgBlAGcAdQBsAGEAcgBpAGMAbwBtAG8AbwBuAEYAbwBuAHQAIABnAGUAbgBlAHIAYQB0AGUAZAAgAGIAeQAgAEkAYwBvAE0AbwBvAG4ALgAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) format('woff');font-weight:400;font-style:normal}.ui.dropdown>.dropdown.icon{font-family:Dropdown;line-height:1;height:1em;width:1.23em;-webkit-backface-visibility:hidden;backface-visibility:hidden;font-weight:400;font-style:normal;text-align:center}.ui.dropdown>.dropdown.icon{width:auto}.ui.dropdown>.dropdown.icon:before{content:'\f0d7'}.ui.dropdown .menu .item .dropdown.icon:before{content:'\f0da'}.ui.dropdown .item .left.dropdown.icon:before,.ui.dropdown .left.menu .item .dropdown.icon:before{content:"\f0d9"}.ui.vertical.menu .dropdown.item>.dropdown.icon:before{content:"\f0da"}/*!
 * # Semantic UI 2.2.11 - Transition
 * http://github.com/semantic-org/semantic-ui/
 *
 *
 * Released under the MIT license
 * http://opensource.org/licenses/MIT
 *
 */.transition{-webkit-animation-iteration-count:1;animation-iteration-count:1;-webkit-animation-duration:.3s;animation-duration:.3s;-webkit-animation-timing-function:ease;animation-timing-function:ease;-webkit-animation-fill-mode:both;animation-fill-mode:both}.animating.transition{-webkit-backface-visibility:hidden;backface-visibility:hidden;visibility:visible!important}.loading.transition{position:absolute;top:-99999px;left:-99999px}.hidden.transition{display:none;visibility:hidden}.visible.transition{display:block!important;visibility:visible!important}.disabled.transition{-webkit-animation-play-state:paused;animation-play-state:paused}.looping.transition{-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}.transition.browse{-webkit-animation-duration:.5s;animation-duration:.5s}.transition.browse.in{-webkit-animation-name:browseIn;animation-name:browseIn}.transition.browse.left.out,.transition.browse.out{-webkit-animation-name:browseOutLeft;animation-name:browseOutLeft}.transition.browse.right.out{-webkit-animation-name:browseOutRight;animation-name:browseOutRight}@-webkit-keyframes browseIn{0%{-webkit-transform:scale(.8) translateZ(0);transform:scale(.8) translateZ(0);z-index:-1}10%{-webkit-transform:scale(.8) translateZ(0);transform:scale(.8) translateZ(0);z-index:-1;opacity:.7}80%{-webkit-transform:scale(1.05) translateZ(0);transform:scale(1.05) translateZ(0);opacity:1;z-index:999}100%{-webkit-transform:scale(1) translateZ(0);transform:scale(1) translateZ(0);z-index:999}}@keyframes browseIn{0%{-webkit-transform:scale(.8) translateZ(0);transform:scale(.8) translateZ(0);z-index:-1}10%{-webkit-transform:scale(.8) translateZ(0);transform:scale(.8) translateZ(0);z-index:-1;opacity:.7}80%{-webkit-transform:scale(1.05) translateZ(0);transform:scale(1.05) translateZ(0);opacity:1;z-index:999}100%{-webkit-transform:scale(1) translateZ(0);transform:scale(1) translateZ(0);z-index:999}}@-webkit-keyframes browseOutLeft{0%{z-index:999;-webkit-transform:translateX(0) rotateY(0) rotateX(0);transform:translateX(0) rotateY(0) rotateX(0)}50%{z-index:-1;-webkit-transform:translateX(-105%) rotateY(35deg) rotateX(10deg) translateZ(-10px);transform:translateX(-105%) rotateY(35deg) rotateX(10deg) translateZ(-10px)}80%{opacity:1}100%{z-index:-1;-webkit-transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);opacity:0}}@keyframes browseOutLeft{0%{z-index:999;-webkit-transform:translateX(0) rotateY(0) rotateX(0);transform:translateX(0) rotateY(0) rotateX(0)}50%{z-index:-1;-webkit-transform:translateX(-105%) rotateY(35deg) rotateX(10deg) translateZ(-10px);transform:translateX(-105%) rotateY(35deg) rotateX(10deg) translateZ(-10px)}80%{opacity:1}100%{z-index:-1;-webkit-transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);opacity:0}}@-webkit-keyframes browseOutRight{0%{z-index:999;-webkit-transform:translateX(0) rotateY(0) rotateX(0);transform:translateX(0) rotateY(0) rotateX(0)}50%{z-index:1;-webkit-transform:translateX(105%) rotateY(35deg) rotateX(10deg) translateZ(-10px);transform:translateX(105%) rotateY(35deg) rotateX(10deg) translateZ(-10px)}80%{opacity:1}100%{z-index:1;-webkit-transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);opacity:0}}@keyframes browseOutRight{0%{z-index:999;-webkit-transform:translateX(0) rotateY(0) rotateX(0);transform:translateX(0) rotateY(0) rotateX(0)}50%{z-index:1;-webkit-transform:translateX(105%) rotateY(35deg) rotateX(10deg) translateZ(-10px);transform:translateX(105%) rotateY(35deg) rotateX(10deg) translateZ(-10px)}80%{opacity:1}100%{z-index:1;-webkit-transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);transform:translateX(0) rotateY(0) rotateX(0) translateZ(-10px);opacity:0}}.drop.transition{-webkit-transform-origin:top center;transform-origin:top center;-webkit-animation-duration:.4s;animation-duration:.4s;-webkit-animation-timing-function:cubic-bezier(.34,1.61,.7,1);animation-timing-function:cubic-bezier(.34,1.61,.7,1)}.drop.transition.in{-webkit-animation-name:dropIn;animation-name:dropIn}.drop.transition.out{-webkit-animation-name:dropOut;animation-name:dropOut}@-webkit-keyframes dropIn{0%{opacity:0;-webkit-transform:scale(0);transform:scale(0)}100%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}}@keyframes dropIn{0%{opacity:0;-webkit-transform:scale(0);transform:scale(0)}100%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}}@-webkit-keyframes dropOut{0%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}100%{opacity:0;-webkit-transform:scale(0);transform:scale(0)}}@keyframes dropOut{0%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}100%{opacity:0;-webkit-transform:scale(0);transform:scale(0)}}.transition.fade.in{-webkit-animation-name:fadeIn;animation-name:fadeIn}.transition[class*="fade up"].in{-webkit-animation-name:fadeInUp;animation-name:fadeInUp}.transition[class*="fade down"].in{-webkit-animation-name:fadeInDown;animation-name:fadeInDown}.transition[class*="fade left"].in{-webkit-animation-name:fadeInLeft;animation-name:fadeInLeft}.transition[class*="fade right"].in{-webkit-animation-name:fadeInRight;animation-name:fadeInRight}.transition.fade.out{-webkit-animation-name:fadeOut;animation-name:fadeOut}.transition[class*="fade up"].out{-webkit-animation-name:fadeOutUp;animation-name:fadeOutUp}.transition[class*="fade down"].out{-webkit-animation-name:fadeOutDown;animation-name:fadeOutDown}.transition[class*="fade left"].out{-webkit-animation-name:fadeOutLeft;animation-name:fadeOutLeft}.transition[class*="fade right"].out{-webkit-animation-name:fadeOutRight;animation-name:fadeOutRight}@-webkit-keyframes fadeIn{0%{opacity:0}100%{opacity:1}}@keyframes fadeIn{0%{opacity:0}100%{opacity:1}}@-webkit-keyframes fadeInUp{0%{opacity:0;-webkit-transform:translateY(10%);transform:translateY(10%)}100%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}}@keyframes fadeInUp{0%{opacity:0;-webkit-transform:translateY(10%);transform:translateY(10%)}100%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}}@-webkit-keyframes fadeInDown{0%{opacity:0;-webkit-transform:translateY(-10%);transform:translateY(-10%)}100%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}}@keyframes fadeInDown{0%{opacity:0;-webkit-transform:translateY(-10%);transform:translateY(-10%)}100%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}}@-webkit-keyframes fadeInLeft{0%{opacity:0;-webkit-transform:translateX(10%);transform:translateX(10%)}100%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@keyframes fadeInLeft{0%{opacity:0;-webkit-transform:translateX(10%);transform:translateX(10%)}100%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@-webkit-keyframes fadeInRight{0%{opacity:0;-webkit-transform:translateX(-10%);transform:translateX(-10%)}100%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@keyframes fadeInRight{0%{opacity:0;-webkit-transform:translateX(-10%);transform:translateX(-10%)}100%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@-webkit-keyframes fadeOut{0%{opacity:1}100%{opacity:0}}@keyframes fadeOut{0%{opacity:1}100%{opacity:0}}@-webkit-keyframes fadeOutUp{0%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}100%{opacity:0;-webkit-transform:translateY(5%);transform:translateY(5%)}}@keyframes fadeOutUp{0%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}100%{opacity:0;-webkit-transform:translateY(5%);transform:translateY(5%)}}@-webkit-keyframes fadeOutDown{0%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}100%{opacity:0;-webkit-transform:translateY(-5%);transform:translateY(-5%)}}@keyframes fadeOutDown{0%{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}100%{opacity:0;-webkit-transform:translateY(-5%);transform:translateY(-5%)}}@-webkit-keyframes fadeOutLeft{0%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}100%{opacity:0;-webkit-transform:translateX(5%);transform:translateX(5%)}}@keyframes fadeOutLeft{0%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}100%{opacity:0;-webkit-transform:translateX(5%);transform:translateX(5%)}}@-webkit-keyframes fadeOutRight{0%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}100%{opacity:0;-webkit-transform:translateX(-5%);transform:translateX(-5%)}}@keyframes fadeOutRight{0%{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}100%{opacity:0;-webkit-transform:translateX(-5%);transform:translateX(-5%)}}.flip.transition.in,.flip.transition.out{-webkit-animation-duration:.6s;animation-duration:.6s}.horizontal.flip.transition.in{-webkit-animation-name:horizontalFlipIn;animation-name:horizontalFlipIn}.horizontal.flip.transition.out{-webkit-animation-name:horizontalFlipOut;animation-name:horizontalFlipOut}.vertical.flip.transition.in{-webkit-animation-name:verticalFlipIn;animation-name:verticalFlipIn}.vertical.flip.transition.out{-webkit-animation-name:verticalFlipOut;animation-name:verticalFlipOut}@-webkit-keyframes horizontalFlipIn{0%{-webkit-transform:perspective(2000px) rotateY(-90deg);transform:perspective(2000px) rotateY(-90deg);opacity:0}100%{-webkit-transform:perspective(2000px) rotateY(0);transform:perspective(2000px) rotateY(0);opacity:1}}@keyframes horizontalFlipIn{0%{-webkit-transform:perspective(2000px) rotateY(-90deg);transform:perspective(2000px) rotateY(-90deg);opacity:0}100%{-webkit-transform:perspective(2000px) rotateY(0);transform:perspective(2000px) rotateY(0);opacity:1}}@-webkit-keyframes verticalFlipIn{0%{-webkit-transform:perspective(2000px) rotateX(-90deg);transform:perspective(2000px) rotateX(-90deg);opacity:0}100%{-webkit-transform:perspective(2000px) rotateX(0);transform:perspective(2000px) rotateX(0);opacity:1}}@keyframes verticalFlipIn{0%{-webkit-transform:perspective(2000px) rotateX(-90deg);transform:perspective(2000px) rotateX(-90deg);opacity:0}100%{-webkit-transform:perspective(2000px) rotateX(0);transform:perspective(2000px) rotateX(0);opacity:1}}@-webkit-keyframes horizontalFlipOut{0%{-webkit-transform:perspective(2000px) rotateY(0);transform:perspective(2000px) rotateY(0);opacity:1}100%{-webkit-transform:perspective(2000px) rotateY(90deg);transform:perspective(2000px) rotateY(90deg);opacity:0}}@keyframes horizontalFlipOut{0%{-webkit-transform:perspective(2000px) rotateY(0);transform:perspective(2000px) rotateY(0);opacity:1}100%{-webkit-transform:perspective(2000px) rotateY(90deg);transform:perspective(2000px) rotateY(90deg);opacity:0}}@-webkit-keyframes verticalFlipOut{0%{-webkit-transform:perspective(2000px) rotateX(0);transform:perspective(2000px) rotateX(0);opacity:1}100%{-webkit-transform:perspective(2000px) rotateX(-90deg);transform:perspective(2000px) rotateX(-90deg);opacity:0}}@keyframes verticalFlipOut{0%{-webkit-transform:perspective(2000px) rotateX(0);transform:perspective(2000px) rotateX(0);opacity:1}100%{-webkit-transform:perspective(2000px) rotateX(-90deg);transform:perspective(2000px) rotateX(-90deg);opacity:0}}.scale.transition.in{-webkit-animation-name:scaleIn;animation-name:scaleIn}.scale.transition.out{-webkit-animation-name:scaleOut;animation-name:scaleOut}@-webkit-keyframes scaleIn{0%{opacity:0;-webkit-transform:scale(.8);transform:scale(.8)}100%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}}@keyframes scaleIn{0%{opacity:0;-webkit-transform:scale(.8);transform:scale(.8)}100%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}}@-webkit-keyframes scaleOut{0%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}100%{opacity:0;-webkit-transform:scale(.9);transform:scale(.9)}}@keyframes scaleOut{0%{opacity:1;-webkit-transform:scale(1);transform:scale(1)}100%{opacity:0;-webkit-transform:scale(.9);transform:scale(.9)}}.transition.fly{-webkit-animation-duration:.6s;animation-duration:.6s;-webkit-transition-timing-function:cubic-bezier(.215,.61,.355,1);transition-timing-function:cubic-bezier(.215,.61,.355,1)}.transition.fly.in{-webkit-animation-name:flyIn;animation-name:flyIn}.transition[class*="fly up"].in{-webkit-animation-name:flyInUp;animation-name:flyInUp}.transition[class*="fly down"].in{-webkit-animation-name:flyInDown;animation-name:flyInDown}.transition[class*="fly left"].in{-webkit-animation-name:flyInLeft;animation-name:flyInLeft}.transition[class*="fly right"].in{-webkit-animation-name:flyInRight;animation-name:flyInRight}.transition.fly.out{-webkit-animation-name:flyOut;animation-name:flyOut}.transition[class*="fly up"].out{-webkit-animation-name:flyOutUp;animation-name:flyOutUp}.transition[class*="fly down"].out{-webkit-animation-name:flyOutDown;animation-name:flyOutDown}.transition[class*="fly left"].out{-webkit-animation-name:flyOutLeft;animation-name:flyOutLeft}.transition[class*="fly right"].out{-webkit-animation-name:flyOutRight;animation-name:flyOutRight}@-webkit-keyframes flyIn{0%{opacity:0;-webkit-transform:scale3d(.3,.3,.3);transform:scale3d(.3,.3,.3)}20%{-webkit-transform:scale3d(1.1,1.1,1.1);transform:scale3d(1.1,1.1,1.1)}40%{-webkit-transform:scale3d(.9,.9,.9);transform:scale3d(.9,.9,.9)}60%{opacity:1;-webkit-transform:scale3d(1.03,1.03,1.03);transform:scale3d(1.03,1.03,1.03)}80%{-webkit-transform:scale3d(.97,.97,.97);transform:scale3d(.97,.97,.97)}100%{opacity:1;-webkit-transform:scale3d(1,1,1);transform:scale3d(1,1,1)}}@keyframes flyIn{0%{opacity:0;-webkit-transform:scale3d(.3,.3,.3);transform:scale3d(.3,.3,.3)}20%{-webkit-transform:scale3d(1.1,1.1,1.1);transform:scale3d(1.1,1.1,1.1)}40%{-webkit-transform:scale3d(.9,.9,.9);transform:scale3d(.9,.9,.9)}60%{opacity:1;-webkit-transform:scale3d(1.03,1.03,1.03);transform:scale3d(1.03,1.03,1.03)}80%{-webkit-transform:scale3d(.97,.97,.97);transform:scale3d(.97,.97,.97)}100%{opacity:1;-webkit-transform:scale3d(1,1,1);transform:scale3d(1,1,1)}}@-webkit-keyframes flyInUp{0%{opacity:0;-webkit-transform:translate3d(0,1500px,0);transform:translate3d(0,1500px,0)}60%{opacity:1;-webkit-transform:translate3d(0,-20px,0);transform:translate3d(0,-20px,0)}75%{-webkit-transform:translate3d(0,10px,0);transform:translate3d(0,10px,0)}90%{-webkit-transform:translate3d(0,-5px,0);transform:translate3d(0,-5px,0)}100%{-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0)}}@keyframes flyInUp{0%{opacity:0;-webkit-transform:translate3d(0,1500px,0);transform:translate3d(0,1500px,0)}60%{opacity:1;-webkit-transform:translate3d(0,-20px,0);transform:translate3d(0,-20px,0)}75%{-webkit-transform:translate3d(0,10px,0);transform:translate3d(0,10px,0)}90%{-webkit-transform:translate3d(0,-5px,0);transform:translate3d(0,-5px,0)}100%{-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0)}}@-webkit-keyframes flyInDown{0%{opacity:0;-webkit-transform:translate3d(0,-1500px,0);transform:translate3d(0,-1500px,0)}60%{opacity:1;-webkit-transform:translate3d(0,25px,0);transform:translate3d(0,25px,0)}75%{-webkit-transform:translate3d(0,-10px,0);transform:translate3d(0,-10px,0)}90%{-webkit-transform:translate3d(0,5px,0);transform:translate3d(0,5px,0)}100%{-webkit-transform:none;transform:none}}@keyframes flyInDown{0%{opacity:0;-webkit-transform:translate3d(0,-1500px,0);transform:translate3d(0,-1500px,0)}60%{opacity:1;-webkit-transform:translate3d(0,25px,0);transform:translate3d(0,25px,0)}75%{-webkit-transform:translate3d(0,-10px,0);transform:translate3d(0,-10px,0)}90%{-webkit-transform:translate3d(0,5px,0);transform:translate3d(0,5px,0)}100%{-webkit-transform:none;transform:none}}@-webkit-keyframes flyInLeft{0%{opacity:0;-webkit-transform:translate3d(1500px,0,0);transform:translate3d(1500px,0,0)}60%{opacity:1;-webkit-transform:translate3d(-25px,0,0);transform:translate3d(-25px,0,0)}75%{-webkit-transform:translate3d(10px,0,0);transform:translate3d(10px,0,0)}90%{-webkit-transform:translate3d(-5px,0,0);transform:translate3d(-5px,0,0)}100%{-webkit-transform:none;transform:none}}@keyframes flyInLeft{0%{opacity:0;-webkit-transform:translate3d(1500px,0,0);transform:translate3d(1500px,0,0)}60%{opacity:1;-webkit-transform:translate3d(-25px,0,0);transform:translate3d(-25px,0,0)}75%{-webkit-transform:translate3d(10px,0,0);transform:translate3d(10px,0,0)}90%{-webkit-transform:translate3d(-5px,0,0);transform:translate3d(-5px,0,0)}100%{-webkit-transform:none;transform:none}}@-webkit-keyframes flyInRight{0%{opacity:0;-webkit-transform:translate3d(-1500px,0,0);transform:translate3d(-1500px,0,0)}60%{opacity:1;-webkit-transform:translate3d(25px,0,0);transform:translate3d(25px,0,0)}75%{-webkit-transform:translate3d(-10px,0,0);transform:translate3d(-10px,0,0)}90%{-webkit-transform:translate3d(5px,0,0);transform:translate3d(5px,0,0)}100%{-webkit-transform:none;transform:none}}@keyframes flyInRight{0%{opacity:0;-webkit-transform:translate3d(-1500px,0,0);transform:translate3d(-1500px,0,0)}60%{opacity:1;-webkit-transform:translate3d(25px,0,0);transform:translate3d(25px,0,0)}75%{-webkit-transform:translate3d(-10px,0,0);transform:translate3d(-10px,0,0)}90%{-webkit-transform:translate3d(5px,0,0);transform:translate3d(5px,0,0)}100%{-webkit-transform:none;transform:none}}@-webkit-keyframes flyOut{20%{-webkit-transform:scale3d(.9,.9,.9);transform:scale3d(.9,.9,.9)}50%,55%{opacity:1;-webkit-transform:scale3d(1.1,1.1,1.1);transform:scale3d(1.1,1.1,1.1)}100%{opacity:0;-webkit-transform:scale3d(.3,.3,.3);transform:scale3d(.3,.3,.3)}}@keyframes flyOut{20%{-webkit-transform:scale3d(.9,.9,.9);transform:scale3d(.9,.9,.9)}50%,55%{opacity:1;-webkit-transform:scale3d(1.1,1.1,1.1);transform:scale3d(1.1,1.1,1.1)}100%{opacity:0;-webkit-transform:scale3d(.3,.3,.3);transform:scale3d(.3,.3,.3)}}@-webkit-keyframes flyOutUp{20%{-webkit-transform:translate3d(0,10px,0);transform:translate3d(0,10px,0)}40%,45%{opacity:1;-webkit-transform:translate3d(0,-20px,0);transform:translate3d(0,-20px,0)}100%{opacity:0;-webkit-transform:translate3d(0,2000px,0);transform:translate3d(0,2000px,0)}}@keyframes flyOutUp{20%{-webkit-transform:translate3d(0,10px,0);transform:translate3d(0,10px,0)}40%,45%{opacity:1;-webkit-transform:translate3d(0,-20px,0);transform:translate3d(0,-20px,0)}100%{opacity:0;-webkit-transform:translate3d(0,2000px,0);transform:translate3d(0,2000px,0)}}@-webkit-keyframes flyOutDown{20%{-webkit-transform:translate3d(0,-10px,0);transform:translate3d(0,-10px,0)}40%,45%{opacity:1;-webkit-transform:translate3d(0,20px,0);transform:translate3d(0,20px,0)}100%{opacity:0;-webkit-transform:translate3d(0,-2000px,0);transform:translate3d(0,-2000px,0)}}@keyframes flyOutDown{20%{-webkit-transform:translate3d(0,-10px,0);transform:translate3d(0,-10px,0)}40%,45%{opacity:1;-webkit-transform:translate3d(0,20px,0);transform:translate3d(0,20px,0)}100%{opacity:0;-webkit-transform:translate3d(0,-2000px,0);transform:translate3d(0,-2000px,0)}}@-webkit-keyframes flyOutRight{20%{opacity:1;-webkit-transform:translate3d(20px,0,0);transform:translate3d(20px,0,0)}100%{opacity:0;-webkit-transform:translate3d(-2000px,0,0);transform:translate3d(-2000px,0,0)}}@keyframes flyOutRight{20%{opacity:1;-webkit-transform:translate3d(20px,0,0);transform:translate3d(20px,0,0)}100%{opacity:0;-webkit-transform:translate3d(-2000px,0,0);transform:translate3d(-2000px,0,0)}}@-webkit-keyframes flyOutLeft{20%{opacity:1;-webkit-transform:translate3d(-20px,0,0);transform:translate3d(-20px,0,0)}100%{opacity:0;-webkit-transform:translate3d(2000px,0,0);transform:translate3d(2000px,0,0)}}@keyframes flyOutLeft{20%{opacity:1;-webkit-transform:translate3d(-20px,0,0);transform:translate3d(-20px,0,0)}100%{opacity:0;-webkit-transform:translate3d(2000px,0,0);transform:translate3d(2000px,0,0)}}.transition.slide.in,.transition[class*="slide down"].in{-webkit-animation-name:slideInY;animation-name:slideInY;-webkit-transform-origin:top center;transform-origin:top center}.transition[class*="slide up"].in{-webkit-animation-name:slideInY;animation-name:slideInY;-webkit-transform-origin:bottom center;transform-origin:bottom center}.transition[class*="slide left"].in{-webkit-animation-name:slideInX;animation-name:slideInX;-webkit-transform-origin:center right;transform-origin:center right}.transition[class*="slide right"].in{-webkit-animation-name:slideInX;animation-name:slideInX;-webkit-transform-origin:center left;transform-origin:center left}.transition.slide.out,.transition[class*="slide down"].out{-webkit-animation-name:slideOutY;animation-name:slideOutY;-webkit-transform-origin:top center;transform-origin:top center}.transition[class*="slide up"].out{-webkit-animation-name:slideOutY;animation-name:slideOutY;-webkit-transform-origin:bottom center;transform-origin:bottom center}.transition[class*="slide left"].out{-webkit-animation-name:slideOutX;animation-name:slideOutX;-webkit-transform-origin:center right;transform-origin:center right}.transition[class*="slide right"].out{-webkit-animation-name:slideOutX;animation-name:slideOutX;-webkit-transform-origin:center left;transform-origin:center left}@-webkit-keyframes slideInY{0%{opacity:0;-webkit-transform:scaleY(0);transform:scaleY(0)}100%{opacity:1;-webkit-transform:scaleY(1);transform:scaleY(1)}}@keyframes slideInY{0%{opacity:0;-webkit-transform:scaleY(0);transform:scaleY(0)}100%{opacity:1;-webkit-transform:scaleY(1);transform:scaleY(1)}}@-webkit-keyframes slideInX{0%{opacity:0;-webkit-transform:scaleX(0);transform:scaleX(0)}100%{opacity:1;-webkit-transform:scaleX(1);transform:scaleX(1)}}@keyframes slideInX{0%{opacity:0;-webkit-transform:scaleX(0);transform:scaleX(0)}100%{opacity:1;-webkit-transform:scaleX(1);transform:scaleX(1)}}@-webkit-keyframes slideOutY{0%{opacity:1;-webkit-transform:scaleY(1);transform:scaleY(1)}100%{opacity:0;-webkit-transform:scaleY(0);transform:scaleY(0)}}@keyframes slideOutY{0%{opacity:1;-webkit-transform:scaleY(1);transform:scaleY(1)}100%{opacity:0;-webkit-transform:scaleY(0);transform:scaleY(0)}}@-webkit-keyframes slideOutX{0%{opacity:1;-webkit-transform:scaleX(1);transform:scaleX(1)}100%{opacity:0;-webkit-transform:scaleX(0);transform:scaleX(0)}}@keyframes slideOutX{0%{opacity:1;-webkit-transform:scaleX(1);transform:scaleX(1)}100%{opacity:0;-webkit-transform:scaleX(0);transform:scaleX(0)}}.transition.swing{-webkit-animation-duration:.8s;animation-duration:.8s}.transition[class*="swing down"].in{-webkit-animation-name:swingInX;animation-name:swingInX;-webkit-transform-origin:top center;transform-origin:top center}.transition[class*="swing up"].in{-webkit-animation-name:swingInX;animation-name:swingInX;-webkit-transform-origin:bottom center;transform-origin:bottom center}.transition[class*="swing left"].in{-webkit-animation-name:swingInY;animation-name:swingInY;-webkit-transform-origin:center right;transform-origin:center right}.transition[class*="swing right"].in{-webkit-animation-name:swingInY;animation-name:swingInY;-webkit-transform-origin:center left;transform-origin:center left}.transition.swing.out,.transition[class*="swing down"].out{-webkit-animation-name:swingOutX;animation-name:swingOutX;-webkit-transform-origin:top center;transform-origin:top center}.transition[class*="swing up"].out{-webkit-animation-name:swingOutX;animation-name:swingOutX;-webkit-transform-origin:bottom center;transform-origin:bottom center}.transition[class*="swing left"].out{-webkit-animation-name:swingOutY;animation-name:swingOutY;-webkit-transform-origin:center right;transform-origin:center right}.transition[class*="swing right"].out{-webkit-animation-name:swingOutY;animation-name:swingOutY;-webkit-transform-origin:center left;transform-origin:center left}@-webkit-keyframes swingInX{0%{-webkit-transform:perspective(1000px) rotateX(90deg);transform:perspective(1000px) rotateX(90deg);opacity:0}40%{-webkit-transform:perspective(1000px) rotateX(-30deg);transform:perspective(1000px) rotateX(-30deg);opacity:1}60%{-webkit-transform:perspective(1000px) rotateX(15deg);transform:perspective(1000px) rotateX(15deg)}80%{-webkit-transform:perspective(1000px) rotateX(-7.5deg);transform:perspective(1000px) rotateX(-7.5deg)}100%{-webkit-transform:perspective(1000px) rotateX(0);transform:perspective(1000px) rotateX(0)}}@keyframes swingInX{0%{-webkit-transform:perspective(1000px) rotateX(90deg);transform:perspective(1000px) rotateX(90deg);opacity:0}40%{-webkit-transform:perspective(1000px) rotateX(-30deg);transform:perspective(1000px) rotateX(-30deg);opacity:1}60%{-webkit-transform:perspective(1000px) rotateX(15deg);transform:perspective(1000px) rotateX(15deg)}80%{-webkit-transform:perspective(1000px) rotateX(-7.5deg);transform:perspective(1000px) rotateX(-7.5deg)}100%{-webkit-transform:perspective(1000px) rotateX(0);transform:perspective(1000px) rotateX(0)}}@-webkit-keyframes swingInY{0%{-webkit-transform:perspective(1000px) rotateY(-90deg);transform:perspective(1000px) rotateY(-90deg);opacity:0}40%{-webkit-transform:perspective(1000px) rotateY(30deg);transform:perspective(1000px) rotateY(30deg);opacity:1}60%{-webkit-transform:perspective(1000px) rotateY(-17.5deg);transform:perspective(1000px) rotateY(-17.5deg)}80%{-webkit-transform:perspective(1000px) rotateY(7.5deg);transform:perspective(1000px) rotateY(7.5deg)}100%{-webkit-transform:perspective(1000px) rotateY(0);transform:perspective(1000px) rotateY(0)}}@keyframes swingInY{0%{-webkit-transform:perspective(1000px) rotateY(-90deg);transform:perspective(1000px) rotateY(-90deg);opacity:0}40%{-webkit-transform:perspective(1000px) rotateY(30deg);transform:perspective(1000px) rotateY(30deg);opacity:1}60%{-webkit-transform:perspective(1000px) rotateY(-17.5deg);transform:perspective(1000px) rotateY(-17.5deg)}80%{-webkit-transform:perspective(1000px) rotateY(7.5deg);transform:perspective(1000px) rotateY(7.5deg)}100%{-webkit-transform:perspective(1000px) rotateY(0);transform:perspective(1000px) rotateY(0)}}@-webkit-keyframes swingOutX{0%{-webkit-transform:perspective(1000px) rotateX(0);transform:perspective(1000px) rotateX(0)}40%{-webkit-transform:perspective(1000px) rotateX(-7.5deg);transform:perspective(1000px) rotateX(-7.5deg)}60%{-webkit-transform:perspective(1000px) rotateX(17.5deg);transform:perspective(1000px) rotateX(17.5deg)}80%{-webkit-transform:perspective(1000px) rotateX(-30deg);transform:perspective(1000px) rotateX(-30deg);opacity:1}100%{-webkit-transform:perspective(1000px) rotateX(90deg);transform:perspective(1000px) rotateX(90deg);opacity:0}}@keyframes swingOutX{0%{-webkit-transform:perspective(1000px) rotateX(0);transform:perspective(1000px) rotateX(0)}40%{-webkit-transform:perspective(1000px) rotateX(-7.5deg);transform:perspective(1000px) rotateX(-7.5deg)}60%{-webkit-transform:perspective(1000px) rotateX(17.5deg);transform:perspective(1000px) rotateX(17.5deg)}80%{-webkit-transform:perspective(1000px) rotateX(-30deg);transform:perspective(1000px) rotateX(-30deg);opacity:1}100%{-webkit-transform:perspective(1000px) rotateX(90deg);transform:perspective(1000px) rotateX(90deg);opacity:0}}@-webkit-keyframes swingOutY{0%{-webkit-transform:perspective(1000px) rotateY(0);transform:perspective(1000px) rotateY(0)}40%{-webkit-transform:perspective(1000px) rotateY(7.5deg);transform:perspective(1000px) rotateY(7.5deg)}60%{-webkit-transform:perspective(1000px) rotateY(-10deg);transform:perspective(1000px) rotateY(-10deg)}80%{-webkit-transform:perspective(1000px) rotateY(30deg);transform:perspective(1000px) rotateY(30deg);opacity:1}100%{-webkit-transform:perspective(1000px) rotateY(-90deg);transform:perspective(1000px) rotateY(-90deg);opacity:0}}@keyframes swingOutY{0%{-webkit-transform:perspective(1000px) rotateY(0);transform:perspective(1000px) rotateY(0)}40%{-webkit-transform:perspective(1000px) rotateY(7.5deg);transform:perspective(1000px) rotateY(7.5deg)}60%{-webkit-transform:perspective(1000px) rotateY(-10deg);transform:perspective(1000px) rotateY(-10deg)}80%{-webkit-transform:perspective(1000px) rotateY(30deg);transform:perspective(1000px) rotateY(30deg);opacity:1}100%{-webkit-transform:perspective(1000px) rotateY(-90deg);transform:perspective(1000px) rotateY(-90deg);opacity:0}}.flash.transition{-webkit-animation-duration:750ms;animation-duration:750ms;-webkit-animation-name:flash;animation-name:flash}.shake.transition{-webkit-animation-duration:750ms;animation-duration:750ms;-webkit-animation-name:shake;animation-name:shake}.bounce.transition{-webkit-animation-duration:750ms;animation-duration:750ms;-webkit-animation-name:bounce;animation-name:bounce}.tada.transition{-webkit-animation-duration:750ms;animation-duration:750ms;-webkit-animation-name:tada;animation-name:tada}.pulse.transition{-webkit-animation-duration:.5s;animation-duration:.5s;-webkit-animation-name:pulse;animation-name:pulse}.jiggle.transition{-webkit-animation-duration:750ms;animation-duration:750ms;-webkit-animation-name:jiggle;animation-name:jiggle}@-webkit-keyframes flash{0%,100%,50%{opacity:1}25%,75%{opacity:0}}@keyframes flash{0%,100%,50%{opacity:1}25%,75%{opacity:0}}@-webkit-keyframes shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}10%,30%,50%,70%,90%{-webkit-transform:translateX(-10px);transform:translateX(-10px)}20%,40%,60%,80%{-webkit-transform:translateX(10px);transform:translateX(10px)}}@keyframes shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}10%,30%,50%,70%,90%{-webkit-transform:translateX(-10px);transform:translateX(-10px)}20%,40%,60%,80%{-webkit-transform:translateX(10px);transform:translateX(10px)}}@-webkit-keyframes bounce{0%,100%,20%,50%,80%{-webkit-transform:translateY(0);transform:translateY(0)}40%{-webkit-transform:translateY(-30px);transform:translateY(-30px)}60%{-webkit-transform:translateY(-15px);transform:translateY(-15px)}}@keyframes bounce{0%,100%,20%,50%,80%{-webkit-transform:translateY(0);transform:translateY(0)}40%{-webkit-transform:translateY(-30px);transform:translateY(-30px)}60%{-webkit-transform:translateY(-15px);transform:translateY(-15px)}}@-webkit-keyframes tada{0%{-webkit-transform:scale(1);transform:scale(1)}10%,20%{-webkit-transform:scale(.9) rotate(-3deg);transform:scale(.9) rotate(-3deg)}30%,50%,70%,90%{-webkit-transform:scale(1.1) rotate(3deg);transform:scale(1.1) rotate(3deg)}40%,60%,80%{-webkit-transform:scale(1.1) rotate(-3deg);transform:scale(1.1) rotate(-3deg)}100%{-webkit-transform:scale(1) rotate(0);transform:scale(1) rotate(0)}}@keyframes tada{0%{-webkit-transform:scale(1);transform:scale(1)}10%,20%{-webkit-transform:scale(.9) rotate(-3deg);transform:scale(.9) rotate(-3deg)}30%,50%,70%,90%{-webkit-transform:scale(1.1) rotate(3deg);transform:scale(1.1) rotate(3deg)}40%,60%,80%{-webkit-transform:scale(1.1) rotate(-3deg);transform:scale(1.1) rotate(-3deg)}100%{-webkit-transform:scale(1) rotate(0);transform:scale(1) rotate(0)}}@-webkit-keyframes pulse{0%{-webkit-transform:scale(1);transform:scale(1);opacity:1}50%{-webkit-transform:scale(.9);transform:scale(.9);opacity:.7}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}@keyframes pulse{0%{-webkit-transform:scale(1);transform:scale(1);opacity:1}50%{-webkit-transform:scale(.9);transform:scale(.9);opacity:.7}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}@-webkit-keyframes jiggle{0%{-webkit-transform:scale3d(1,1,1);transform:scale3d(1,1,1)}30%{-webkit-transform:scale3d(1.25,.75,1);transform:scale3d(1.25,.75,1)}40%{-webkit-transform:scale3d(.75,1.25,1);transform:scale3d(.75,1.25,1)}50%{-webkit-transform:scale3d(1.15,.85,1);transform:scale3d(1.15,.85,1)}65%{-webkit-transform:scale3d(.95,1.05,1);transform:scale3d(.95,1.05,1)}75%{-webkit-transform:scale3d(1.05,.95,1);transform:scale3d(1.05,.95,1)}100%{-webkit-transform:scale3d(1,1,1);transform:scale3d(1,1,1)}}@keyframes jiggle{0%{-webkit-transform:scale3d(1,1,1);transform:scale3d(1,1,1)}30%{-webkit-transform:scale3d(1.25,.75,1);transform:scale3d(1.25,.75,1)}40%{-webkit-transform:scale3d(.75,1.25,1);transform:scale3d(.75,1.25,1)}50%{-webkit-transform:scale3d(1.15,.85,1);transform:scale3d(1.15,.85,1)}65%{-webkit-transform:scale3d(.95,1.05,1);transform:scale3d(.95,1.05,1)}75%{-webkit-transform:scale3d(1.05,.95,1);transform:scale3d(1.05,.95,1)}100%{-webkit-transform:scale3d(1,1,1);transform:scale3d(1,1,1)}}/*
* 
*   CMP UI
* 
*/
/*----------------------------------------------------------------------------------------------------------------- */
#cmp-container-id {
    z-index: 100000000!important;
    top: auto!important;
    height: 0px;
}
#cmp-container-id>iframe {
    bottom: 5px;
    left: 50%;
    height: 120px;
    margin: auto !important;
    width: 100%;
    max-width: 980px;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

.qc-cmp-persistent-link {
    display: none !important;
}

.qc-cmp-main-messaging {
  text-align: justify;
}

/* Applying to the mobile layout of the CMP */

.qc-cmp-ui > .qc-cmp-publisher-logo {
  display: none;
}

.qc-cmp-ui-content > .qc-cmp-title {
  font-size: 24px;
  line-height: normal;
}

*{
    box-sizing: border-box;
    -o-box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    border: none;
    margin: 0;
    padding: 0;
    line-height:1.5em;
}

html, body{
    height:100%;
}

body{
    background:#fff;
    font-family: arial, helvetica, sans-serif;
    color:#333333;
    flex-direction:column;
    min-height:100%;
    overflow-y:scroll;
}

input, submit, select, textarea, button{
    font-size:inherit;
}

ul, ol{
    list-style-type:none;
}

a{
    color:inherit;
    text-decoration:inherit;
}

a:hover{
    cursor:pointer;
}

h1{
    display:block;
    font-size:1.6em;
    margin-bottom: 20px;
}

/* transition */

a{
    -webkit-transition: color 0.5s, background-color 0.5s;
    transition: color 0.5s, background-color 0.5s;
}

/* end */

/* shadow */

.csm,
.inputSuggestions{
    -webkit-box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
    -moz-box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
}

/* end */

/* header */

div.header{
    background:#314089; 
    position: relative;
}

.home .logo {
    width: 100%;
}

.logo{
    opacity:1;
    vertical-align:middle;
}

.home .logo_link {
    vertical-align:middle;
    width: 25%;
}


.logo_link{
    display:inline-block;
    margin-left: 40px;
}

.search-input-container{
    overflow: hidden;
    vertical-align: middle;
}

.csl,
.search_input{
    vertical-align:middle;
    outline: none;
}

.search_input{
    font-size: 16px;
    background:none;
    color:#000;
    padding: 1em 0em 1em 0.5em;
    width: 100%;
    -webkit-appearance: none; /*Safari*/
}

.search_input::-webkit-input-placeholder{
    color: #333333;
    font-size: 1.05em;
}

.search_form{
    display: inline-block;
    border-radius:5px;
    background: rgba(255, 255, 255, 1);
    margin: 30px 50px;
    vertical-align:middle;
    width: 45%;
    height: 56px;
}

.header_version {
    color: white;
    display: inline-block;
    font-size: 13px;
    margin-top: 30px;
    font-weight: 300;
    position: absolute;
    right: 45px;
    text-align: right;
}

/* Override Semantic UI Lib */
.ui.selection.dropdown.custom-select-label-container {
    border: none;
    border-radius: 0;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
    min-width: initial;
    background: #dedddd;
    padding: 16px 8px;
    height: 56px;
    cursor: pointer;
    float: left;
    width: 181px;
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
}

.ui.selection.dropdown .menu {
    min-width: 0;
    width: 181px;
    border: 0;
    margin: 0;
}

.dropdown-icon {
    vertical-align: middle;
    width: 1em;
    text-align: center;
}

.search_dictionary_selector.custom-select {
    display : none;
}

.res_hos {
    padding-left: 5px;
}

.custom-select-menu {
    display: none;
    z-index: 2;
    position: absolute;
    background: #fff;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.1);
    border: solid 1px #ddd;
    border-top: none;
    left: 0;
    max-height: none;
}

.custom-select-menu a{
    display: block;
    padding: 5px 19px;
}

.custom-select-menu a:hover{
    background: #ddd;
}

.header_version .fa-globe {
    font-size: 1.5em;
    vertical-align: middle;
    margin-right: 5px;
}

.version_selector {
    cursor: pointer;
}

.version_selector .curr_version {
    margin-right: 5px;
}

.version_selector .other_versions {
    display: none;
    border: thin solid white;
    padding: 5px;
    text-align: center;
    color: black;
    background: #fff;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.1);
    border: solid 1px #ddd;
    z-index: 10;
}

.version_selector .other_versions a{
    padding: 3px;
}
/* end */

/* footer */
.footer .responsive_row div {
    float: none;
    margin-left: auto;
    margin-right: auto;
}

.footer .responsive_row .grey_part {
    background-color: #333333;
    text-align: center;
    padding: 70px 0;
}

.footer .share_links,
.footer .links,
.footer .responsive_row .blue_part div {
    display: inline-block;
    vertical-align: middle;
}

.footer .share_panel {
    margin: 0;
}

.footer .share_panel a{
    color: #333333;
    background-color: white;
}

.footer .links {
    color: white;
    font-size: 13px;
    text-align: left;
    font-weight: 300;
    padding-left: 200px;
}

.footer .links a {
    padding: 4px 0;
    display: table;
}

.footer .responsive_row .blue_part {
    background-color: #314089;
    text-align: center;
    padding: 8px 0;
}

.footer .responsive_row .blue_part div.always_learning,
.footer .responsive_row .blue_part div.pearson {
    width: 40%;
}

.footer .responsive_row .blue_part div.pearson {
    padding-left: 195px;
    text-align: left;
}

.footer .responsive_row .blue_part img.always_learning,
.footer .responsive_row .blue_part img.pearson {
    vertical-align: middle;
}

/* end */

/* browse */
.browse_letters,
.browse_dictionaries {
    margin-bottom: 20px;
}

.browse_dictionaries li{
    margin: 16px 2px;
}

.browse_dictionaries li a{
    padding: 8px 20px;
}

.browse_letters li{
    display:inline-block;
}

.browse_letters li a{
    display:inline-block;
    padding:1em;
}

.browse_letters li a:hover{
    background:#222;
    color:#eee;
    display:inline-block;
}

.browse_groups,
.browse_results{
    list-style:disc outside;
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
    margin-bottom: 20px;
}

.browse_groups li,
.browse_results li{
    margin-left: 20px;
    padding:0.5em;
}

.browse_groups li a,
.browse_results li a{
    padding:0px 2px;
}

.browse_groups li a:hover,
.browse_dictionaries li a:hover,
.browse_results li a:hover{
    background:#222;
    color:#eee;
}

.browse_groups li a .head{
    display:inline;
}

.browse_results .pos,
.browse_panel .pos,
.searches .pos{
    font-size:0.8em;
    font-style:italic;
    vertical-align:top;
}

.browse_panel{
    margin-top: 20px;
    padding:20px;
    background:rgba(0, 0, 0, 0.1);
}

.browse_panel a{
    display:block;
    padding:8px 20px;
}

.browse_panel a:hover,
.browse_panel a.current{
    color:#ccc;
    background-color:#333;
}

.browse_panel a[class=seeAllResults],
.browse_panel a[class=seeAllTopics] {
    text-decoration: underline;
}

.browse_panel ul li pos,
.content .searches li pos {
    font-variant:small-caps;
    text-transform:lowercase;
    font-size: 0.8em;
}
/* end */

/* search results & did you mean */
.searches,
.didyoumean {
    -webkit-column-count: 1;
    -moz-column-count: 1;
    column-count: 1;
    margin-bottom: 10px;
    list-style: none;
}

.searches li,
.didyoumean li {
    padding: 0.5em;
    background: aliceblue;
    margin-bottom: 5px;
}

.searches li a,
.didyoumean li a {
    font-weight: bold;
}

.searches li a pos{
    font-weight: normal;
}

.searches li a:hover,
.didyoumean li a:hover{
    text-decoration: underline;
}

.searches li sup {
    vertical-align: top;
    font-size: 0.8em;
}

.search_word {
    color : #364395;
}

/* end */

/* topic cloud */
.cloud {
    margin-bottom: 10px;
}
.cloud li {
    display:inline-block;
}

/* end */

.content{
    position:relative;
    flex:1 0 auto;
    min-height: 500px;
}

.message{
    position:absolute;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    height:100%;
    width:100%;
}

/* custom selector */
.csl{
    font-size:19.2px;
    background-color: white;
    -webkit-transform:rotateY(180deg);
    -moz-transform:rotateY(180deg);
    -o-transform:rotateY(180deg);
    -ms-transform:rotateY(180deg);
    float: right;
    padding: 12px;
    margin: 2px;
    cursor: pointer;
}

.csl .fa-search {
    font-weight: bold;
    color: lightgrey;
}

.csm{
    position:absolute;
    z-index:10;
}

.csm a{
    display:block;
    padding:10px 20px;
    background:#ccc;
}

.csm a:hover,
.csm a.current{
    color:#ccc;
    background-color:#333;
}
/* end */

/* autocomplete */
.inputSuggestions{
    font-size: 16px;
    z-index: 10;
    position: absolute;
}

.inputSuggestions a{
    display:block;
    padding:10px 20px;
    background:#ccc;
}

.inputSuggestions a.footerLink{
    background:#aaa;
}

.inputSuggestions a:hover,
.inputSuggestions a.current{
    color:#ccc;
    background-color:#333;
}

/* end */

/* share panel */
.share_panel a{
    margin:0 10px;
    color: white;
    border-radius: 50%;
    height: 50px;
    width: 50px;
    text-align: center;
    line-height: 1.5em;
}
.right_col .share_panel .share_panel_facebook {
    background: #3b5998;
}
.right_col .share_panel .share_panel_twitter {
    background: #55acee;
}
/* end */

/* entry content */

.entry_content, 
.page_content,
.error_content {
    margin: 28px 50px 20px 50px;
}

.EXAMPLE{
    color:#778899;
    margin-left:20px;
}

.entry_content .dictionary .defRef{
    border-bottom: thin dotted gray;
}

/* end */

/* error content */

.error_content p a {
    text-decoration: underline;
}

/* end */

/* about page */

.aboutlist{
    list-style-type: disc;
}

.aboutText a:hover {
	text-decoration: underline;
}
.aboutlist li{
    margin-left: 20px;
}

.browse_dictionaries,
.browse_letters,
.aboutText,
.howtouseText{
    margin-bottom: 10px;
}
.tooltip {
	color: red;
}
#idmLogo {
	width: 80px;
    vertical-align: middle;
    float: none;
}

/* end */

/* how to use page */

.howtouseText .howtouseP{
    margin-bottom: 20px;
    max-width: 1000px;
}

.howtouseText .howtouseP a{
    text-decoration: underline;
}

.howtouse_image{
    float: none;
    margin-bottom: 30px;
}

.howtouseText #consonants {
    float: left;
    margin-right: 10px;
    margin-bottom: 10px;
}

.howtouseText #vowels {
    margin-bottom: 10px;
}

.opt_content {
	width: 400px;
	margin: 0 auto;
	text-align: left;
}
.items_content {
	display: none;
	margin: auto;
	padding: 10px;
}
.items_title {
    font-weight: bold;
    cursor: pointer;
}
#dot {
	font-size: 14px;
	margin-right: 5px;
    cursor: pointer;
}


/* end */.content .ENTRY .POSGR{
    margin-top:2em;
}

.content .ENTRY .SENSE{
    margin-top:1em;
}

.content .ENTRY .EXAS{
    margin-left:1em;
}

.content .ENTRY .EXACNT .attr-type{
    display:inline-block;
    margin-right:2em;
}

.content .ENTRY .EXACNT .attr-type:before{
    content:"[";
}

.content .ENTRY .EXACNT .attr-type:after{
    content:"]";
}

.content .ENTRY .EXA{
    font-style:italic;
}

.content .ENTRY .EXA:before{
    content:"'";
}

.content .ENTRY .EXA:after{
    content:"'";
}

.content img{
    float: right;
    width: 30%;
}

.content .speaker:hover{
    cursor: pointer;
}

.content td{
    padding-right: 2px;
}

.home .content {
    margin: 0;
}

.home .content .home_content {
    margin: 0 auto 60px auto;
}

.home .content .text_welcome {
    margin: 0 auto 0px;
    text-align: center;
    width: 80%;
}

.home .content .text_welcome h1 {
    font-size: 1.8em;
    margin-bottom: 0px;
}

.home_welcome_link {
    color: red;
    cursor: pointer;
    font-size: 1.8em;
    font-weight: bold;
}

.home .content .cols {
    text-align: center;
}

.home .content .left_col,
.home .content .middle_col,
.home .content .right_col,
.home .content .second_col {
    display: inline-block;
    vertical-align: top;
    text-align: left;
}

.home .content .second_col {
    width: 450px;
}

.home .content .box,
.responsive_cell2 .right_col .box {
    padding: 20px;
}

.home .content .grey_box {
    border: 1px solid lightgray;
    margin: 20px 20px 0 0;
    height: 270px;
}

.responsive_cell2 .right_col .grey_box {
    border: 1px solid lightgray;
    margin: 20px 20px 0 0;
}

.home .content .left_box {
    width: 280px;
}

.responsive_cell2 .right_col .wotd,
.responsive_cell2 .right_col #iotd {
    width: 300px;
}

.home .content div.box_title,
.responsive_cell2 .right_col div.box_title {
    margin-bottom: 10px;
}

.home .content .left_box.wotd .box_title {
    margin: 0;
}

.home .content span.box_title,
.responsive_cell2 .right_col span.box_title {
    color: white;
    padding: 0 20px 2px 7px;
}

.home .content .box,
.responsive_cell2 .right_col .wotd {
    overflow-y: auto;
}

.home .content .wotd .box_title,
.responsive_cell2 .right_col .wotd .box_title {
    background-color: red;
}

.home .content .tdwds li {
    counter-increment: count-me;
    color: #2f5597;
    padding-left: 20px;
}

.home .content .tdwds li:before {
    content: counter(count-me);
    display: block;
    position: relative;
    max-width: 0px;
    max-height: 0px;
    left: -105%;
    top: .05em;
    color: #333333;
}

.home .content .second_col .homeDict {
    overflow: hidden;
    width:  inherit;
}

.home .content .left_box .title_entry,
.responsive_cell2 .right_col .left_box .title_entry {
    font-size: 2em;
    font-weight: bold;
    letter-spacing: -1px;
    display: inherit;
}

.home .content .tdwds .title_entry {
    font-size: 1.2em;
    font-weight: normal;
    letter-spacing: 0px;
    display: block;
}

#wotdlej .phr {
    font-weight: bold;
}

#wotdlej .jap,
#wotdlej .exa {
    display: block;
}

#tcotw ul li {
    display: inline;
}
.home .content .ldoceEntry .Sense {
    margin: 0;
}

.home .content li,
.home .content span.view_more {
    font-weight: bold;
}

.home .content li {
    color: black;
}

.home .content span.view_more {
    color: blue;
}

.home .content div.view_more {
    margin-left: 20px;
}

.home .content .middle_box {
    width: 360px;
}

.home .content .second_col #iotd {
    width: inherit;
}

.home .content .middle_box.tdwds {
    width: 280px;
    overflow: hidden;
}

.home .content #hot_topics_title {
    font-size: 1.3em;
    font-weight: bold;
    color: #000;
    background-color: #e5e5e5;
    padding: 2px 20px 2px 7px;
    margin-bottom: 20px;
    display: inline-block;
}

.home .content .middle_box ul {
    text-align: center;
    font-size: 1.2em;
}

.home .content .middle_box ul li {
    display: inline-block;
}

.home #tcotw .topic_1 {
    font-size: 1.5em;
    color: #2B6EFF;
}
.home #tcotw .topic_2 {
    color: #B7BFCC;
    font-size: 1.5em;
}
.home #tcotw .topic_3 {
    color: #EC0F8C;
    font-size: 1.2em;
} 
.home #tcotw .topic_4 {
    color: #FF801A;
    font-size: 1.2em;
}
.home #tcotw .topic_5 {
    color: #00A9FF;
}
.home #tcotw .topic_6 {
    color: #FFC300;
}
.home #tcotw .topic_7 {
    color: #74AFAD;
    font-size: 0.9em;
}
.home #tcotw .topic_8 {
    color: #A51890;
    font-size: 0.9em;
}
.home #tcotw .topic_9 {
    color: #2ECC40;
    font-size: 0.75em;
}
.home #tcotw .topic_10 {
    color: #FF3333;
    font-size: 0.75em;
}

.home #hot_topics .topic_1 {
    color: #2B6EFF;
}
.home #hot_topics .topic_2 {
    color: #B7BFCC;
}
.home #hot_topics .topic_3 {
    color: #EC0F8C;
} 
.home #hot_topics .topic_4 {
    color: #FF801A;
    font-size: 1.5em;
}
.home #hot_topics .topic_5 {
    color: #00A9FF;
    font-size: 0.75em;
}
.home #hot_topics .topic_6 {
    color: #FFC300;
    font-size: 0.9em;
}
.home #hot_topics .topic_7 {
    color: #74AFAD;
}
.home #hot_topics .topic_8 {
    color: #A51890;
}
.home #hot_topics .topic_9 {
    color: #2ECC40;
}
.home #hot_topics .topic_10 {
    color: #FF3333;
    font-size: 1.2em;
}

.topic .content .topic_1 {
    color: #2B6EFF;
}
.topic .content .topic_2 {
    color: #B7BFCC;
}
.topic .content .topic_3 {
    color: #EC0F8C;
} 
.topic .content .topic_4 {
    font-size: 1.5em;
    color: #FF801A;
}
.topic .content .topic_5 {
    font-size: 0.9em;
    color: #00A9FF;
}
.topic .content .topic_6 {
    font-size: 1.1em;
    color: #FFC300;
}
.topic .content .topic_7 {
    color: #74AFAD;
}
.topic .content .topic_8 {
    color: #A51890;
}
.topic .content .topic_9 {
    color: #2ECC40;
}
.topic .content .topic_10 {
    font-size: 1.2em;
    color: #FF3333;
}

.home .content #pictures_title,
.responsive_cell2 .right_col #pictures_title { 
    background-color: #35a3ff;
}

.home .content #tcotw span.box_title, .home .content .tdwds .box_title {
    background-color: #f1d600;
}

.home .content .homeDict .box_title {
    background-color: #e5e5e5;
    color: #333333;
}

.home .content .right_col {
    margin-top: 20px;
}

.responsive_cell2 .right_col {
    margin-top: 200px;
    margin-bottom: 20px;
    width: 300px;
}

.right_box,
.right_box .hover {
    height: 180px;
    width: 180px;
}
.right_box {
    margin-bottom: 10px;
    background-color: #fae660;
    text-align: center;
    cursor: pointer;
    padding: 10px;
    position: relative;
}

.right_box .symbols {
    font-size: 5em;
    font-family: 'longmaneltdict';
    margin-top: 15px;
    height:120px;
}

.right_box .meanings:before {
    content: "\e616";
}

.right_box .exercises:before {
    font-size:.7em;
    font-weight:bold;
    content: "\e900";
}

.right_box .corpus:before {
    content: "\e613";
}

.right_box .def:before {
    content: "\e610";
}

.right_box .hover {
    display: none;
    background-color: rgba(0,0,0,0.85);
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px;
    text-align: left;
}

.right_box:hover .hover {
    display: block;
}

.right_box .hover div {
    color: #fae660;
    margin-bottom: 5px;
}

.right_box .hover li {
    color: white;
    font-weight: 300;
    font-size: 0.7em;
}

.right_box .hover li:before {
    content: "+";
    margin-right: 4px;
    color: #fae660;
}

.home .content .pictures,
.responsive_cell2 .right_col #iotd .pictures {
    border-top: 1px dotted;
    border-bottom: 1px dotted;
    border-left: 0; /* EDGE */
    border-right: 0; /* EDGE */
    margin: 10px 0;
    border-image: radial-gradient(black, white);
    -webkit-border-image: radial-gradient(black, white);
    border-image-slice: 1;
}

.home .content .pictures img,
.responsive_cell2 .right_col #iotd .pictures img {
    text-align: center;
    margin: 5px 10px;
    max-width: 36%;
    max-height: 36%;
    float: none;
}

.home .content .carousel {
    background-color: #dedddd;
    text-align: center;
    padding: 40px 0 30px;
    float: none;
}

.home .content .fa {
    font-size: 6em;
    color: #9e9d9e;
    cursor: pointer;
}

.home .content .fa-angle-left {
    margin-right: 6%;
}

.home .content .fa-angle-right {
    margin-left: 6%;
}

.home .content .carousel img {
    width: 130px;
}

.home .content .carousel .parts,
.home .content .carousel .right_content,
.home .content .carousel .part_icon {
    display: inline-block;
}

.home .content .carousel .parts,
.home .content .fa {
    vertical-align: middle;
}

.home .content .carousel .parts {
    width: 345px;
}

.home .content .carousel .part1,
.home .content .carousel .part3 {
    margin-right: 40px;
}

.home .content .carousel .part3,
.home .content .carousel .part4 {
    display: none;
}

.home .content .dict_title,
.home .content .carousel .right_content  {
    text-align: left;
}

.home .content .carousel .right_content {
    vertical-align: top;
    margin-top: 5px;
    margin-left: 10px;
}

.home .content .dict_title {
    font-weight: bold;
    margin-bottom: 40px;
    font-size: 0.95em;
}

.home .content .carousel .part_icon {
    text-align: center;
    margin: 0 10px 20px 13px;
    word-break: keep-all;
}

.home .content .carousel .little_text {
    font-size: 0.8em;
    font-weight: bold;
}

.home .content .carousel .icon {
    width: 20px;
    height: 20px;
}

.home .content .more_info {
    background-color: #314089;
    color: white;
    padding: 8px 30px;
    border-radius: 30px;
    display: table;
}

.paragraph {
    display: block;
    padding-top: 4px;
}
.responsive_row {
    clear: both;
}

.responsive_row:before, .responsive_row:after {
    display: table;
    content: "";
    clear: both;
}

    .responsive_cell1 {
        width:10%;
    }
    .responsive_cell2 {
        width:20%;
    }
    .responsive_cell3 {
        width:30%;
    }
    .responsive_cell4 {
        width:40%;
    }
    .responsive_cell5 {
        width:50%;
    }
    .responsive_cell6 {
        width:60%;
    }
    .responsive_cell7 {
        width:70%;
    }
    .responsive_cell8 {
        width:80%;
    }
    .responsive_cell9 {
        width:90%;
    }
    .responsive_cell10 {
        width:100%;
    }

[class*="responsive_cell"] {
    float: left;
}

.content h1.pagetitle, .content h1.topicpagetitle {
    margin-bottom: 20px;
}

.topicCloud {
    margin-bottom: 20px;
}

#ad_topslot.am-home {
    margin: 15px 0;
    text-align: center;
}

#ad_topslot.am-default,
#ad_topslot.am-translator {
    margin: 15px 0 0 0;
}

#ad_btmslot.am-default {
    text-align: center;
}

#ad_rightslot.am-default {
    margin: 15px 0;
}

span[id^="ad_"][class^="am-"] {
	display: block;
}

.contentslot {
    width: 100%;
    min-width: 320px;
    margin: 0.8em auto;
}

/* mobile - low resolutions */

@media screen and (max-width: 332px) {
    .Sense .contentslot {
        margin-left: -30px;
    }
    .assetlink .contentslot, .Tail .contentslot {
        margin-left: -10px;
    }
}

/* mobile */
@media screen and (max-width: 761px) {
    .res_hos {
        display: none !important;
    }
    .dropdown-icon {
        margin-top: 4px;
    }
    .ui.dropdown.selection.custom-select-label-container {
        width: 30px;
    }
    .inputSuggestions {
        left: 30px;
    }
    [class*="responsive_cell"] {
        float: none;
        width: auto;
    }
    .csl {
        padding: 12px 0px 12px 12px;
        margin: 5px 0px 5px 5px;
        font-size: 1em;
    }
    .responsive_hide_on_smartphone, .responsive_hide_on_smartphone_tablet {
        display: none !important;
    }
    .header {
        height: 116px;
        min-width: 300px;
    }
    .home .content .grey_box {
    	height: auto;
    }
    .logo, .home .logo {
        width: 69px;
    }
    .logo_link, .home .logo_link {
        width: 69px;
        margin: 10px;
    }
    .header_version {
        margin-top: 10px;
        right: 10px;
    }
    h1 {
        font-size: 1.6em;
        margin-top: 5px;
    }
    .browse_groups, .browse_results, .didyoumean {
        list-style: disc outside;
        -webkit-column-count: 1;
        -moz-column-count: 1;
        column-count: 1;
        margin-bottom: 15px;
    }
    .search_form {
        width: 73%;
        margin: 0px 0px 10px 0px;
        vertical-align: bottom;
    }
    .content {
        min-height: 200px;
        margin-bottom: 20px;
    }
    .content img {
        clear: both;
        width: 100%;
        display: block;
        margin-left: auto;
        margin-right: auto
    }
    .responsive_cell2 .right_col #iotd .pictures img {
        display: inline;
    }
    .entry_content, .page_content, .error_content {
        margin: 15px 10px 10px 10px;
    }
    .content h1.pagetitle, .content h1.topicpagetitle, .dictionary, .topicCloud {
        margin-bottom: 10px;
    }
    .dictionary_intro, .topic_intro {
        margin: 5px 0 10px 0px !important
    }
    .home .content .text_welcome h1 {
        font-size: 1em;
    }
    .home .content .text_welcome {
        width: 90%;
    }
    .home .content .middle_box, .home .content .left_box, .home .content .second_col {
        width: 100%;
        height: auto;
    }
    .home .content .pictures {
        text-align: center;
    }
    .home .content .pictures img {
        display: inline-block;
        text-align: center;
    }
    .home .content .right_box, .home .content .right_box .hover {
        height: 280px;
        width: 280px;
    }
    .home .content .right_box {
        padding: 30px;
    }
    .home .content .right_box .hover div {
        font-size: 1.3em;
    }
    .home .content .right_box .hover li {
        font-size: 1em;
    }
    .home .content .fa-angle-right {
        margin-left: 2%;
        font-size: 3em;
    }
    .home .content .fa-angle-left {
        margin-right: 2%;
        font-size: 3em;
    }
    #idmLogo {
    	display: inline-block;
    }
    .responsive_cell2 .right_col {
        margin-right: auto;
        margin-left: auto;
        margin-top: 20px;
    }
    .footer, .home .content .fa {
        display: block;
    }
    .footer .links, .footer .responsive_row .blue_part div.pearson {
        padding: 0;
    }
    .home .content .carousel .part1, .home .content .carousel .part3 {
        margin: 0;
    }
    .footer .share_links {
        margin-bottom: 30px;
    }
    .footer .responsive_row .blue_part div {
        margin-left: auto;
        margin-right: auto;
        display: inline;
    }
    #ad_topslot.am-default,
    #ad_topslot.am-translator {
        margin: 5px 0;
        text-align: center;
    }
    .pos:before {
        content: '';
        display: block;
    }
    .home .content .tdwds li:before {
        left: -102%;
    }
    ol.breadcrumb li:not(:first-child):not(:last-child) a {
        max-width: 100px;
        overflow: hidden;
        text-overflow: ellipsis;
    }
}

/* tablet */
@media screen and (min-width: 762px) and (max-width: 947px) {
    .res_hos {
        display: none !important;
    }
    .ui.dropdown.selection.custom-select-label-container {
        width: 30px;
    }
    .dropdown-icon {
        margin-top: 4px;
    }
    .custom-select-label-container {
        width: 30px;
    }
    .inputSuggestions {
        left: 30px;
    }
    .responsive_hide_on_smartphone_tablet {
        display: none;
    }
    .content {
        margin: 0 0 30px 0;
        min-height: 500px;
    }
    .content img {
        width: 50%;
    }
    .responsive_cell2 .right_col #iotd .pictures img {
        display: inline;
    }
    h1 {
        margin-bottom: 10px;
    }
    .content h1.pagetitle, .content h1.topicpagetitle {
        margin-bottom: 10px;
    }
    .responsive_cell6 {
        width: 59%;
    }
    .logo, .home .logo {
        width: 100%;
    }
    .logo_link, .home .logo_link {
        width: 25%;
    }
    .entry_content, .page_content, .error_content {
        margin: 20px 20px 10px 20px;
    }
    .searches, .browse_groups, .browse_results, .didyoumean {
        -webkit-column-count: 1;
        -moz-column-count: 1;
        column-count: 1;
        margin-bottom: 10px;
    }
    .search_form {
        margin: 30px 40px;
    }
    .home .content .text_welcome h1 {
        font-size: 1em;
    }
    .home .content .fa-angle-right {
        margin-left: 0.5%;
        font-size: 3em;
    }
    .home .content .fa-angle-left {
        margin-right: 0.5%;
        font-size: 3em;
    }
    #ad_topslot.am-default,
    #ad_topslot.am-translator {
        margin: 15px 0 0 15px;
    }
    .responsive_cell2 .right_col {
        margin-top: 180px;
    }
    .footer .links {
        padding-left: 100px;
    }
    .home .logo_link {
        margin: 1% 0% 7% 6%;
    }
    .ac_leftslot {
        display: none !important;
    }
}

@media screen and (min-width: 762px) {
    .responsive_hide_on_non_smartphone {
        display: none;
    }
}

/* Desktop */
@media screen and (min-width: 948px) {
    #ad_leftslot_container {
        width: 160px;
        float: left;
        margin: 125px 0 15px 15px;
    }
    .ac_leftslot.sticky {
        position: absolute;
        top: 125px;
        left: 10px;
    }
    .ac_leftslot.sticky #ad_leftslot {
        position: static;
    }
    .home .logo_link {
        margin: 1% 3% 7% 6%;
    }
}

/* Small desktop screen */
@media screen and (min-width: 948px) and (max-width: 1224px) {
    .entry_content, .page_content, .error_content {
        margin: 28px 20px 20px 20px;
    }
    .content .responsive_cell2.left_col {
        width: 10%;
    }
    .responsive_cell6 {
        width: 48%;
    }
    .browse_groups, .browse_results {
        list-style: disc outside;
        -webkit-column-count: 1;
        -moz-column-count: 1;
        column-count: 1;
    }
    .footer .links {
        padding-left: 100px;
    }
}

@media screen and (min-width: 360px) and (max-width: 812px) {
    .exercise-gapfill-drag-bag, .exercise-groups-bag {
        position: fixed;
        bottom: 0;
        background-color: rgba(180, 183, 189, 0.53);
        left: 0;
        width: 100%;
    }
    .exercise-context.static {
        padding: 0px
    }
}
/**** FREEONLINE****/
.page {
    font-family : arial, helvetica, sans-serif;
    font-size : 12pt;
    display : block;
}

.pagetitle,
h1.topicpagetitle {
    font-size : 1.6em;
    font-weight : bold;
}

.topicpagetitle a{
    font-style: italic;
}

.topicpagetitle a:hover{
    color: #314089;
}

.metadata,
.metadata {
    color : magenta;
    display : none;
}

.infls,
.description,
.title,
.url,
.summary,
.og,
.infls,
.description,
.title,
.url,
.summary,
.og {
    display : block;
}

.infls:before,
.infls:before {
    content : 'inflections: ';
}

.description:before,
.description:before {
    content : 'description: ';
}

.summary:before,
.summary:before {
    content : 'summary: ';
}

.title:before,
.title:before {
    content : 'title: ';
}

.exaGroup .title:before,
.exaGroup .title:before {
    content : '';
}

.Crossrefto {
    color : blue;
    font-weight:bold
}

.suppressed {
    display : none;
}

.og .title:before,
.og .title:before {
    content : 'og.title: ';
}

.url:before {
    content : 'url: ';
}

.og .url:before,
.og .url:before {
    content : 'og.url: ';
}

.assetref,
.assetref {
    display : block;
}

.assettype {
    font-weight : bold;
    color : #364395;
}

.dictentry {
    display : block;
    margin-bottom : 25px;
}

.dictionary_intro,
.topic_intro {
    display : block;
    background-color:#35a3ff;
    color:#fff;
    padding-left:10px;
    margin:5px 0 10px -7px
}
.assets_intro,
.asset_intro {
    border : solid 1px ;
    border-color : #f1d600;
    background-color:#f1d600;
    color : #fff;
    font-weight:normal;
    border-radius : 5px;
    -moz-border-radius : 5px;
    -webkit-border-radius : 5px;
    padding-left : 3px;
    padding-right : 3px;
}

.right_col .yellow_box {
    margin-bottom: 10px;
    display: inline-block;
}

.yellow_box {
    margin-top: 22px;
    display: table;
}

/*****  LDOCE  ***************************/
.ldoceEntry .Entry
{
    font-size : 12pt;
    text-align : justify;
    display : block;
    margin-top : 8px;
}

.ldoceEntry .Thesref {
    color : #364395;
}


.ldoceEntry .ABBR
{
    font-weight : bold;
}

.ldoceEntry .ACTIV
{
    display : none;
}

.ldoceEntry .AMEQUIV
{
    font-weight : bold;
}

.ldoceEntry .BOX
{
    display : none;
}

.ldoceEntry .BREQUIV
{
    font-weight : bold;
}

.ldoceEntry .COLLO
{
    font-weight : bold;
    margin-left : 20px;
}

.ldoceEntry .ColloExa
{
    display : block;
}

.ldoceEntry .COLLOINEXA
{
    font-weight : bold;
}

.ldoceEntry .COMMENT
{
    display : none;
}

.ldoceEntry .COMP
{
    font-weight : bold;
}

.ldoceEntry .Crossrefto
{
    font-weight : bold;
    font-size : 120%;
}

.ldoceEntry .DERIV
{
    font-weight : bold;
    font-size : 120%;
}

.ldoceEntry .Entry
{
    font-size : 11pt;
    text-align : justify;
}

.ldoceEntry .ErrorBox
{
    display : block;
}

.ldoceEntry .EXAMPLE
{
    display : block;
    margin-left : 20px;
    color : gray;
}


.ldoceEntry .FIELD
{
    display : none;
}

.ldoceEntry .AC,
.ldoceEntry .synopp {
    color : #fff;
    border-color: #f1d600;
    background-color:#f1d600;
}

.ldoceEntry .FREQ
{
    color : red;
    border-color : red;
}

.ldoceEntry .LEVEL
{
    color : red;
    font-size : 120%;
}

.ldoceEntry .FULLFORM
{
    font-weight : bold;
}

.ldoceEntry .GEO,
.ldoceEntry .geo
{
    font-weight : normal;
    color : #364395;
}

.ldoceEntry .GLOSS
{
    color : #364395;
    font-weight : normal;
    font-style : normal;
}

.ldoceEntry .GRAM,
.bussdictEntry .GRAM
{
    color : green;
    font-weight:bold;
    margin:0 5px 10px 3px
}

.ldoceEntry .GramExa
{
    display : block;
}

.ldoceEntry .HINTBOLD
{
    font-weight : bold;
}

.ldoceEntry .HINTITALIC
{
    font-style : italic;
}

.ldoceEntry .HINTTITLE
{
    font-weight : bold;
}

.ldoceEntry .frequent .HOMNUM {
    vertical-align : super;
    font-size : 12pt;
    color : red;
    font-weight : bold;
}

.ldoceEntry .frequent .HYPHENATION {
    color : red;
    font-size : 160%;
}
.ldoceEntry .HOMNUM
{
    vertical-align : super;
    font-size : 12pt;
    color : red;
    font-weight : bold;
}

.ldoceEntry .HWD
{
    display : none;
}

.ldoceEntry .HYPHENATION,
.ldoceEntry .PHRVBHWD
{
    font-weight : bold;
    font-size : 160%;
    color : red;
}

.ldoceEntry .LEXUNIT,
.ldoceEntry .LEXVAR
{
    font-weight : bold;
}

.ldoceEntry .LINKWORD
{
    color : #364395;
}

.ldoceEntry .NOTE,
.ldoceEntry .Noteprompt
{
    display : none;
}

.ldoceEntry .OBJECT
{
    font-weight : normal;
}

.ldoceEntry .OPP,
.ldoceEntry .ORTHVAR,
.ldoceEntry .PASTPART,
.ldoceEntry .PASTTENSE
{
    font-weight : bold;
}

.ldoceEntry .PhrVbEntry
{
    display : block;
}

.ldoceEntry .PIC,
.ldoceEntry .PICCAL
{
    display : none;
}

.ldoceEntry .PLURALFORM
{
    font-weight : bold;
}

.ldoceEntry .POS,
.bussdictEntry .POS
{
    color : green;
    font-weight:bold;
    margin:0 0 0 10px
}

.ldoceEntry .PRESPART,
.ldoceEntry .PRESPARTX
{
    font-weight : bold;
}

.ldoceEntry .PROPFORM
{
    font-weight : bold;
    margin-left : 20px;
}

.ldoceEntry .PROPFORMPREP
{
    font-weight : bold;
    margin-left : 20px;
}

.ldoceEntry .PTandPP,
.ldoceEntry .PTandPPX
{
    font-weight : bold;
}

.ldoceEntry .REFHOMNUM
{
    vertical-align : super;
    font-size : 60%;
}

.ldoceEntry .REFHWD
{
    font-weight : bold;
    font-style : normal;
}

.ldoceEntry .REFLEX
{
    font-weight : bold;
}

.ldoceEntry .REGISTERLAB
{
    color : purple;
    font-style : italic;
}

.ldoceEntry .RELATEDWD
{
    font-weight : bold;
    color:blue;
}

.ldoceEntry .RunOn
{
    display : block;
    margin-bottom : 10px;
}

.ldoceEntry .Sense {
    display : block;
    margin-left : 20px;
    margin-bottom : 15px;
}

.ldoceEntry .SIGNPOST
{
    background-color: #f18500;
    color: white;
    font-weight: bold;
    font-size: 79%;
    text-transform: uppercase;
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    /* padding-left: 3px; */
    /* padding-right: 3px; */
    padding: 0px 5px;
    letter-spacing: 1px;
}

.ldoceEntry .STRONG
{
    font-style : italic;
}

.ldoceEntry .Subsense
{
    display : block;
    margin-left : 10px;
}

.ldoceEntry .SUPERL,
.ldoceEntry .SYN,
.ldoceEntry .T3PERSSING,
.ldoceEntry .T3PERSSINGX
{
    font-weight : bold;
}

.ldoceEntry .UNCLASSIFIED
{
    font-weight : bold;
}

.ldoceEntry .USAGE
{
    display : none;
}

.ldoceEntry .GramBox .CROSS .neutral {
    color: red;
    margin-right: 10px;
}

.ldoceEntry .neutral
{
    color : black;
    font-style : normal;
    font-weight : normal;
    font-variant : normal;
}

 .ldoceEntry .EXPL .cross,
 .ldoceEntry .GramBox .EXPL .dont_say,
 .ldoceEntry .BADEXA
{
    color : red;
}

.ldoceEntry .italic
{
    font-style : italic;
    font-weight : normal;
}

.ldoceEntry .infllab
{
    font-style : italic;
    font-weight : normal;
}

.ldoceEntry .warning
{
    font-style : normal;
    font-weight : bold;
    color : red;
}

.ldoceEntry .sensenum
{
    font-style : normal;
    font-weight : bold;
    color : black;
}

.ldoceEntry .synopp,
.ldoceEntry .FREQ,
.ldoceEntry .AC
{
    display : inline-block;
    font-style : normal;
    font-weight : bold;
    text-transform : uppercase;
    border-radius : 5px;
    -moz-border-radius : 5px;
    -webkit-border-radius : 5px;
    border : solid 1px;
    padding-left : 4px;
    padding-right : 4px;
}

.bussdictEntry .Box,
.ldoceEntry .ColloBox,
.ldoceEntry .ThesBox,
.ldoceEntry .F2NBox,
.ldoceEntry .GramBox {
    display : block;
    border-radius : 5px;
    -moz-border-radius : 5px;
    -webkit-border-radius : 5px;
    border : solid #364395 1px;
    padding : 15px;
    margin : 8px 0;
}

.GramBox{
    background-color:#fff;
    color:#000
}

.GramBox .boxheader {
    line-height:2em
}

.ColloBox .heading {
    line-height:2em;
    margin:0 10px 0  0
}

.ThesBox .heading{
    line-height:2em
}

.ldoceEntry .HEADING,
.ldoceEntry .heading {
    font-weight : bold;
    font-size : 120%;
    color : #364395;
}

.ldoceEntry .HEADING.newline {
    display : block;
}

.ldoceEntry .SECHEADING,
.ldoceEntry .subheading {
    display : table;
    border-radius : 5px;
    -moz-border-radius : 5px;
    -webkit-border-radius : 5px;
    border : solid #6f469d 2px;
    padding-left : 4px;
    padding-right : 20px;
    margin:25px 0 10px 0;
    font-weight : bold;
    color : white;
    text-transform : uppercase;
    background-color : #6f469d;
}

.ldoceEntry .Collocate,
.ldoceEntry .Exponent {
    display : block;
    margin:15px 0 0 6px;
}

.ldoceEntry .EXPL {
    display : block;
}

.ldoceEntry .COLLOC,
.ldoceEntry .EXP,
.ldoceEntry .EXPR {
    font-weight : bold;
}

.ldoceEntry .keycollo {
    font-weight : bold;
    color : #364395;
}

.ldoceEntry .THESPROPFORM {
    font-weight : bold;
}

.ldoceEntry .COLLEXA,
.ldoceEntry .THESEXA {
    color : gray;
    display : block;
}


.ldoceEntry .LearnerItem {
    display : block;
}

.ldoceEntry .GOODCOLLO {
    font-style : italic;
}

.ldoceEntry .BADCOLLO {
    text-decoration : line-through;
}

.ldoceEntry .DEFBOLD {
    font-weight : bold;
}

.ldoceEntry .exafile {
    color : gray;
    font-style : normal;
    font-size : 120%;
    padding: 5px;
}

.ldoceEntry .amefile {
    color : #4693db;
    font-size : 130%;
    padding-left: 5px;
}

.ldoceEntry .brefile {
    color : #fa6360;
    font-size : 130%;
    padding-left: 5px;
}


/*****  BUSSDICT  ***************************/
.bussdictEntry .Entry
{
    font-size : 12pt;
    text-align : justify;
    display : block;
    margin-top : 8px;
}

.bussdictEntry .supp
{
    background-color : gray;
}

.bussdictEntry .ABBR,
.bussdictEntry .AMEQUIV,
.bussdictEntry .BREQUIV,
.bussdictEntry .COLLO,
.bussdictEntry .COMP
{
    font-weight : bold;
}

.bussdictEntry .ACTIV,
.bussdictEntry .COMMENT
{
    display : none;
}

.bussdictEntry .ColloExa
{
    display : block;
    margin-left : 10px;
}

.bussdictEntry .COLLOINEXA
{
    font-style : italic;
    font-weight : bold;
}

.bussdictEntry .DERIV
{
    font-weight : bold;
    font-size : 120%;
}

.bussdictEntry .ErrorBox
{
    display : block;
}

.bussdictEntry .EXAMPLE
{
    display : block;
    margin-left : 15px;
    color : gray;
}

.bussdictEntry .Box .EXAMPLE
{
    display : inline;
    margin-left : 0px;
    color : black;
    font-style : italic;
}

.bussdictEntry .FIELD
{
    display : none;
}

.bussdictEntry .FREQ,
.bussdictEntry .LEVEL
{
    font-weight : bold;
    color : red;
}

.bussdictEntry .FULLFORM
{
    font-weight : bold;
}

.bussdictEntry .GEO,
span.geo
{
    font-weight : normal;
    font-style : italic;
    color : #364395;
}

.bussdictEntry .GLOSS
{
    font-weight : normal;
    font-style : normal;
    color : #364395;
}

.bussdictEntry .GramExa
{
    display : block;
    margin-left : 10px;
}

.bussdictEntry .HINTBOLD,
.bussdictEntry .HINTTITLE
{
    font-weight : bold;
}

.bussdictEntry .HINTITALIC
{
    font-style : italic;
}

.bussdictEntry .HOMNUM
{
    vertical-align : super;
    font-size : 12pt;
    font-weight : bold;
}

.bussdictEntry .HWD
{
    display : none;
}

.bussdictEntry .HYPHENATION
{
    font-weight : bold;
    font-size : 160%;
}

.bussdictEntry .LEXUNIT,
.bussdictEntry .LEXVAR
{
    font-weight : bold;
}

.bussdictEntry .LINKWORD
{
    color : #364395;
}

.bussdictEntry .NOTE,
.bussdictEntry .Noteprompt
{
    display : none;
}

.bussdictEntry .OBJECT
{
    font-weight : normal;
}

.bussdictEntry .OPP,
.bussdictEntry .ORTHVAR,
.bussdictEntry .PASTPART,
.bussdictEntry .PASTTENSE
{
    font-weight : bold;
}

.bussdictEntry .PhrVbEntry
{
    display : block;
}

.bussdictEntry .PHRVBHWD
{
    font-weight : bold;
    color : #364395;
    font-size : 120%;
}

.bussdictEntry .PIC,
.bussdictEntry .PICCAL
{
    display : none;
}

.bussdictEntry .PLURALFORM
{
    font-weight : bold;
}

.bussdictEntry .PRESPART,
.bussdictEntry .PRESPARTX,
.bussdictEntry .PROPFORM,
.bussdictEntry .PROPFORMPREP,
.bussdictEntry .PTandPP,
.bussdictEntry .PTandPPX
{
    font-weight : bold;
}

.bussdictEntry .REFHOMNUM
{
    vertical-align : super;
    font-size : 60%;
}

.bussdictEntry .REFHWD
{
    text-transform : lowercase;
    font-style : normal;
    font-variant : small-caps;
}

.bussdictEntry .FIELDXX,
.bussdictEntry .Crossrefto .REFLEX {
    display : none;
}

.bussdictEntry .REFLEX
{
    font-weight : bold;
}

.bussdictEntry .REGISTERLAB
{
    color : #364395;
    font-style : italic;
}

.bussdictEntry .RELATEDWD
{
    font-weight : bold;
}

.bussdictEntry .Sense {
    display : block;
    margin-left : 20px;
    margin-bottom : 15px;
}

.bussdictEntry .SIGNPOST
{
    background-color : gray;
    color : white;
    font-weight : bold;
}

.bussdictEntry .STRONG
{
    font-style : italic;
}

.bussdictEntry .Subsense
{
    display : block;
    margin-left : 10px;
}

.bussdictEntry .SUPERL,
.bussdictEntry .SYN,
.bussdictEntry .T3PERSSING,
.bussdictEntry .T3PERSSINGX,
.bussdictEntry .UNCLASSIFIED
{
    font-weight : bold;
}

.bussdictEntry .USAGE
{
    display : none;
}

span.neutral
{
    font-style : normal;
    font-weight : normal;
    font-variant : normal;
}

span.italic,
span.infllab
{
    font-style : italic;
    font-weight : normal;
    font-family : Times New roman;
}

span.warning
{
    font-style : normal;
    font-weight : bold;
    color : red;
}

span.sensenum
{
    font-style : normal;
    font-weight : bold;
    margin-right : 5px;
    margin-left : 3px;

}

span.synopp
{
    font-style : normal;
    font-weight : bold;
    color : darkblue;
}

.bussdictEntry .ColloBox,
.bussdictEntry .ThesBox,
.bussdictEntry .F2NBox,
.bussdictEntry .GramBox,
.bussdictEntry .UsageBox {
    display : block;
    border-style : solid;
}

.bussdictEntry .GramBox.nobox {
    display : inline;
    border-style : none;
    background-color : none;
}

.bussdictEntry .GramBox.nobox .EXPL {
    display : inline;
}

.bussdictEntry .HEADING,
span.heading,
.bussdictEntry .Gramref {
    font-weight : bold;
    font-size : 120%;
    color : #364395;
}

.bussdictEntry .gramref {
    margin-left : 5px;
    margin-right : 5px;
}

.bussdictEntry .HEADING.newline {
    display : block;
}

.bussdictEntry .SECHEADING,
span.subheading {
    display : block;
    font-weight : bold;
    font-style : italic;
    text-decoration : underline;
}

.bussdictEntry .Collocate.newline,
.bussdictEntry .Exponent,
.bussdictEntry .GramBox .EXPL,
.bussdictEntry .EXPL.newline {
    display : block;
}

.bussdictEntry .Collocate.inline {
    display : inline;
}

.bussdictEntry .COLLOC,
.bussdictEntry .EXP,
.bussdictEntry .EXPR {
    font-weight : bold;
}

.bussdictEntry .COLLOC.key {
    color : #364395;
}

span.keycollo {
    font-weight : bold;
    color : #364395;
}

.bussdictEntry .THESPROPFORM {
    font-weight : bold;
}

.bussdictEntry .COLLEXA,
.bussdictEntry .THESEXA,
.bussdictEntry .GOODCOLLO {
    font-style : italic;
}

.bussdictEntry .LearnerItem {
    display : block;
}

.bussdictEntry .BADCOLLO,
.bussdictEntry .BADEXA {
    text-decoration : line-through;
}

.bussdictEntry .DEFBOLD {
    font-weight : bold;
}

.bussdictEntry .CompareWord,
.bussdictEntry .CompareWord,
.bussdictEntry .EXP {
    display : block;
}

.bussdictEntry .UNDERLINE {
    text-decoration : underline;
}

.bussdictEntry .boxheader {
    display : block;
    background-color : #364395;
    color : white;
    font-weight : bold;
}

.bussdictEntry .SubEntry.embedded {
    margin-top : -5px;
    margin-bottom : 0px;
    margin-left : 30px;
}

.bussdictEntry .SubEntry {
    display : block;
    margin-top : 2px;
    margin-bottom : 2px;
    margin-left : 20px;
}

.bussdictEntry .SubEntry .HWD {
    display : inline;
    font-weight : bold;
    font-size : 120%;
    color : #364395;
}

/****** VERB TABLE *****/
.verbTable .entry {
    margin-bottom : 20px;
}

.verbTable .lemma {
    color : black;
    font-size : 120%;
    font-weight : bold;
    margin:0 0 0 10px;  
}

.verbTable table {
    background-color: #fae660;
    margin-bottom: 10px;
    border-collapse: collapse;
    width: 100%;
}

.verbTable .Simple_Form .aux {
    font-weight: bold;
}

.verbTable td {
    padding: 0 10px;
}

.verbTable td.header {
    background-color: #333333;
    color : #fff;padding:0 0 0 10px;
    font-size : 120%;
}

.verbTable td.col1 {
    color : #333333;
    padding:20px 10px 0;
    font-weight:bold;
    font-size: 14px;
    text-decoration:underline
}

.verbTable td.col2 {
    color : gray;
    width:150px
}

.verbTable .view_more,
.verbTable .view_less {
    text-align: center;
    font-weight: bold;
    color: black;
    padding: 40px 0 10px;
}

.verbTable .view_more span,
.verbTable .view_less span {
    cursor: pointer;
}

.verbTable .view_less {
    display: none;
}

.verbTable .next_tenses {
    display: none;
}

.verbTable .geo {
    font-style : italic;
    color : #000000;
    font-size : normal;
    font-weight : normal;
}

.verbTable .aux {
    color : black;
    font-weight : normal;
}

.verbTable .verb_form {
    color : black;
    font-weight : bold;
}

/***** EXAS ******/
.exaGroup .exaEntry {
    margin-bottom : 20px;
    display : block;
}

.exaGroup .exaGroup {
    display : block;
    margin-bottom : 20px;
}

.exaGroup .title {
    font-size : 110%;
    font-weight : bold;
    color : black;
    display : block;
    margin-left : 5px;
    margin-top: 15px;
}

.exaGroup .exa {
    display : block;
    color : gray;
    margin-left : 15px;
}

.exaGroup .NodeW {
    font-weight : bold;
}

.asset {
    margin-top : 30px;
}
/***** TOPIC ******/
.Entry .topics_container {
	display: table;
}

.Entry .related_topics {
    padding: 0 4px 1px 0;
    font-size: 16px;
    font-family: Tahoma, Arial, Helvetica;
    color: #000;
}

.Entry .topic,
.topicCloud .topic_other{
    color: red;
    text-decoration:underline
}

.Entry .topic:hover,
.topicCloud .topic_other:hover {
    color: #4693db;
}
/*** WORD FAMILY ***/
.pos {
	color: green;
	font-weight: normal;
}
.wordfams {
	font-weight: bold;
}
.wordfams .crossRef, .wordfams .w {
	margin: 0 6px;
}
.wordfams .crossRef {
	border-bottom: thin dotted gray;
}
/*** ETYM ***/
.etym .Head {
	font-weight: bold;
}
.etym .Head .HOMNUM {
	vertical-align: super;
    font-size: 12pt;
}/****** CSS TIDY FOR JAPANESE-E***************************/
/*  4 sections: printing and used tags,                  */
/*  xslt tags,                                           */
/*  non-printing and used tags and finally               */
/*  non-used tags (but in the dtd).                      */
/*  tags are alphabetically ordered withi each category  */

/**************PRINTING TAGS******************/
.page {
    font-family: arial, helvetica, sans-serif;
    font-size: 12pt;
    display: block;
}

.pagetitle {
    font-size: 1.6em;
    font-weight: bold;
}

.lejEntry {
    font-size: 12pt;
    display: block;
    margin-top: 20px;
}

.lejEntry .GRAMHEAD {
    font-weight: bold;
    display: block;
}

.lejEntry .BADEXA {
    font-style: italic;
}

.lejEntry .COMPOUND, .lejEntry .ENGEXPR, .lejEntry .ENGLISH, .lejEntry .EXP, .lejEntry .F1, .lejEntry .FULLFORM,
    .lejEntry .HIRAGANA, .lejEntry .HWDFORM, .lejEntry .INFL, .lejEntry .LEXUNIT, .lejEntry .MENUPHRV,
    .lejEntry .OPPOSITE,.lejEntry .PATTERN, .lejEntry .PATTERNPREP, .lejEntry .PHRVAR, .lejEntry .PHRVHWD,
    .lejEntry .PHRVPATT, .lejEntry .RELATEDWD, .lejEntry .SENVAR, .lejEntry .SYNONYM, .lejEntry .POSFORMOF,
    .lejEntry .plusphrases,
    .lejEntry .plusphrasalverbs {
    font-weight: bold;
}

.lejEntry .Phrvbox .POS, .lejEntry .REFSENSE, .lejEntry .CULTDEF, .lejEntry .CATEGORY, .lejEntry .COLLINFO,
    .lejEntry .COLLINFOTRAN, .lejEntry .ELECTRONIC, .lejEntry .ENCYCDEF, .lejEntry .ENGDEF, .lejEntry .ENGDEFINFO,
    .lejEntry .EXACONTEXT, .lejEntry .EXAINFO, .lejEntry .HWD, .lejEntry .LEXUINFO, .lejEntry .OBJINFO,
    .lejEntry .OBJINFOTRAN, .lejEntry .PATTERNINFO, .lejEntry .POSHWD, .lejEntry .POSLEXU, .lejEntry .POSPHRV,
    .lejEntry .POSPOS, .lejEntry .POSSENSENUM, .lejEntry .REMARK, .lejEntry .SEMINDINFO, .lejEntry .SUBCAT,
    .lejEntry .SUBJINFO, .lejEntry .SUBJINFOTRAN, .lejEntry .TOPENTRY, .lejEntry .TYPE, .lejEntry .BOXSEMINFO,
    .lejEntry .PICALL, .lejEntry .SEMIND, .lejEntry .SEMINFO,
    .lejEntry .suppress,
    .suppressed,
    .metadata {
    display: none;
}

.lejEntry .exagr {
    display: block;
    margin-left: 5px;
}

.lejEntry .exagr {
    color: gray;
}

.lejEntry .EXATRAN, .lejEntry .XEXATRAN {
    font-style: normal;
    display: block;
    margin-left: 10px;
}

.lejEntry .FFXREF {
    font-variant: small-caps;
}

.lejEntry .Compoundbox .GRAM {
    color: red;
}

.lejEntry .HOM {
    vertical-align: super;
    font-size: 12pt;
    font-weight: bold;
    color: #017fff
}

.lejEntry.freq .HOM {
    color: red;
}

.lejEntry .HYPHENATION {
    font-size: 160%;
    font-weight: bold;
    color: #017fff
}

.lejEntry.freq .HYPHENATION {
    color: red;
}

.lejEntry .RunOn .HWD {
    font-size: 100%;
    font-weight: bold;
    display: inline;
}

.lejEntry .OBJECT {
    font-weight: normal;
}

.lejEntry .REFHOM {
    vertical-align: super;
    font-size: 60%;
}

.lejEntry.freq .TRAN.FREQTRAN {
    color: red;
    font-weight: bold;
}

.lejEntry .USE {
    display: block;
}

.lejEntry .VAR {
    font-weight: bold;
    color: #017fff
}

.lejEntry .Head .VAR {
    font-weight: bold;
    font-size: 120%;
}

.lejEntry.freq .Head .VAR {
    color: red;
}

.lejEntry.freq .Wordclass .VAR {
    color: black;
}

.lejEntry .XENGEXPR {
    font-weight: bold;
    color: purple;
}

div.menu {
    background-color: #E0E0E0;
    margin: 0px 20px;
    padding: 4px 4px 4px 4px;
}

.lejEntry .COMMENT {
    color: purple;
    font-weight: bold;
    display: block;
    font-size: 110%;
}

.lejEntry .GLOSS {
    color: purple;
}

.lejEntry .SECEXPL {
    color: purple;
    font-weight: bold;
    font-size: 110%;
}

.lejEntry .TITLE {
    color: purple;
    font-size: 130%;
    display: block;
    font-weight: bold;
    /*  display:none;*/
}

.lejEntry .XEXPL {
    color: purple;
    display: none;
}

.lejEntry .BOXHWD {
    font-size: 110%;
    font-weight: bold;
}

.lejEntry .Exponent {
    display: block;
}

.lejEntry .Exa1 {
    display: block;
}

.lejEntry .Exa1 {
    display: block;
}

.lejEntry .Usebox {
    margin-top: 10px;
    display: block;
    background-color: #aecaf1;
    width: 50%;
    margin-bottom: 10px;
    border: solid 1px;
    padding: 5px;
}

.lejEntry .phrasehead {
    display: inline-block;
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border: solid gray 1px;
    padding-left: 4px;
    padding-right: 4px;
    font-weight: bold;
    color: white;
    background-color: #3d3d3d;
    text-align: center;
    width: 50%;
    margin-top: 10px;
}

.lejEntry .Sense {
    display: block;
    margin-left: 15px;
}

.lejEntry .Phrvsense {
    display: block;
    margin-left: 15px;
}

.lejEntry .Lexubox .Sense {
    display: block;
    margin-left: 0px;
}

.lejEntry .Patternbox .Sense {
    display: block;
    margin-left: 0px;
}

.lejEntry .Compoundbox .Sense {
    display: block;
    margin-left: 0px;
}

.lejEntry .Lexubox, .lejEntry .Patternbox,
.lejEntry .Compoundbox, .lejEntry .phrasehead,
.lejEntry .Reference, .lejEntry .Tranbox {
    display: block;
}

.lejEntry .sensenum, .lejEntry .menusense {
    font-weight: bold;
    color: black;
    margin-left: -20px;
}

.lejEntry .subnum, .lejEntry .menusubsense {
    color: black;
}

.lejEntry .boxnum {
    color: black;
}

.lejEntry .warning {
    font-weight: bold;
    color: red;
}

.lejEntry .FREQ {
    color: red;
    border-color: red;
    display: inline-block;
    font-style: normal;
    font-weight: bold;
    text-transform: uppercase;
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border: solid 1px;
    padding-left: 4px;
    padding-right: 4px;
    padding-top: 1px;
    padding-bottom: 2px;
}

.lejEntry .amefile {
    color: #4693db;
    font-size: 130%;
    padding-left: 5px;
}

.lejEntry .inline {
    display: inline;
}

.lejEntry .Etymbox, .lejEntry .Tranbox, .lejEntry .Thesbox, .lejEntry .Cultbox, .lejEntry .Grambox {
    display: block;
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border: solid #364395 1px;
    padding: 15px;
    margin: 8px 0;
}

.lejEntry .heading {
    display: block;
    font-weight: bold;
    font-size: 120%;
    line-height: 2em;
    color: #364395;
}

.lejEntry .related {
    color: #364395;
    border-color: #364395;
    display: inline-block;
    font-style: normal;
    font-weight: bold;
    font-size: 110%;
    text-transform: uppercase;
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border: solid 1px;
    padding-left: 4px;
    padding-right: 4px;
    padding-top: 1px;
    padding-bottom: 2px;
}

.latamEntry .SEMIND {
    display: inline;
}

.lejEntry .SIGNPOST {
    background-color: #cc0000;
    color: white;
    font-weight: bold;
    font-size: 90%;
    text-transform: uppercase;
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    padding-left: 3px;
    padding-right: 3px;
}

.lejEntry .VPRON {
    font-size: 100%;
    font-weight: bold;
    display: inline;
}

.latamEntry .GRAM {
    color: blue;
}

.latamEntry .THESHEAD {
    font-size: 120%;
    line-height: 2em;
    color: #314089;
}

.latamEntry .Lexubox, .latamEntry .Patternbox, .latamEntry .Compoundbox {
    display: block;
    margin-top: 5px;
}

.latamEntry .Lexubox.inline, .latamEntry .Patternbox.inline, .latamEntry .Compoundbox.inline {
    display: inline;
}

.latamEntry .Lexubox .Sense, .latamEntry .Patternbox .Sense, .latamEntry .Compoundbox .Sense {
    display: block;
    margin-top: 0px;
}

.latamEntry .Sense {
    display: block;
    margin-left: 15px;
    margin-top: 10px;
}

.latamEntry .Subsense {
    display: block;
}

/* changes 20171114*/
.lejEntry .SIGNPOST {
    padding-top: 2px;
    padding-bottom: 2px;
}

.latamEntry .TRANCOM {
    color: #314089;
}

.latamEntry .GRAM, .latamEntry .SEMIND, .latamEntry .Tranlabbox, .latamEntry .REGISTER {
    color: #314089;
}

.lejEntry .USE.inline {
    display: inline;
}

/* the two next rules should be removed from above */
.lejEntry .neutral {
    font-weight: normal;
    font-style: normal;
}

.lejEntry.latamEntry .POS,
.lejEntry.latamEntry .TRANPOS,
.lejEntry.latamEntry .TRANINFLTYPE  {
    color: #314089;
    font-style: italic;
}

/* tablet */
@media screen and (min-width: 762px) and (max-width: 947px) {
    .lejEntry .Usebox {
        width: 100%;
    }
}

/* mobile */
@media screen and (max-width: 470px) {
    .lejEntry .Usebox {
        width: 100%;
    }
}
/****** CSS TIDY FOR JAPANESE-E***************************/
/*  4 sections: printing and used tags,                  */
/*  xslt tags,                                           */
/*  non-printing and used tags and finally               */
/*  non-used tags (but in the dtd).                      */
/*  tags are alphabetically ordered withi each category  */


/**************PRINTING TAGS******************/

.page {
    font-family : arial, helvetica, sans-serif;
    font-size : 12pt;
    display : block;
}

.pagetitle {
    font-size : 1.6em;
    font-weight : bold;
}

.metadata,
.metadata {
    color : magenta;
    display : none;
}

.ljeEntry
{
    display : block;
    font-size : 12pt;
    margin-top : 20px;
}

.ljeEntry .Subentry {
    display : block;
    margin-top : 20px;
}

.ljeEntry .Subentry.inline {
    display : inline;
    margin-top : 0px;
}

.ljeEntry .Sense {
    display : block;
}

.ljeEntry .sensenum {
    display : none;
}

.ljeEntry .TranGp {
    display : block;
}

.ljeEntry .Subsense {
    display : block;
    margin-left : 10px;
}

.ljeEntry .HWD {
}

.ljeEntry .HWDFORM {
}

.ljeEntry .HWD {
}

.ljeEntry .TRAN {
    font-weight : bold;
    color : blue;
}

.ljeEntry .Reference {
    font-size : 80%;
    font-style : italic;
    color : purple;
}

.ljeEntry .Link {
    display : none;
}

.ljeEntry .Box {
    display : block;
    margin-bottom : 10px;
}

.ljeEntry .EXATRAN {
    font-style : italic;
    display : block;
}
.ljeEntry .Extraexas,
.ljeEntry .Extraphrases {
    display : block;
    margin-top : 10px;
}

.ljeEntry .header {
    font-weight : bold;
    font-variant : small-caps;
    display : block;
    text-transform : uppercase;
}

.ljeEntry .neutral {
    color : black;
    font-style : normal;
    font-weight : normal;
}

.ljeEntry .suppress {
    display : none;
}
.ljeEntry .exagr {
    display : block;
    margin-left : 5px;
    color : gray;
}

.ljeEntry .OBJINFO {
    display: none;
}

.ljeEntry .Extraphrases,
.ljeEntry .Extraexas
{
    display : block;
    border-radius : 5px;
    -moz-border-radius : 5px;
    -webkit-border-radius : 5px;
    border : solid #364395 1px;
    padding : 15px;
    margin : 8px 0;
}

.ljeEntry .heading {
    display : block;
    font-weight : bold;
    font-size : 120%;
    line-height : 2em;
    color : #364395;
}.exercise .exercise-choice input[type='radio'] {
    display: none;
}

.exercise .exercise-choice input[type='radio']:checked+label,
.exercise .exercise-group .exercise-item {
    background: #92b2dc;
}

.exercise .exercise-choice input[type='radio'].error+label,
.exercise .exercise-item.error,
.exercise .exercise-group .exercise-item.error,
.exercise .exercise-gap-item.error {
    background: #E61928;
}

.exercise .exercise-choice input[type='radio'].correct:checked+label,
.exercise .exercise-item.correct,
.exercise .exercise-group .exercise-item.correct,
.exercise .exercise-gap-item.correct {
    background: #4e7d19;
}

.exercise .exercise-qtext {
    font-size: 1.2em;
}

.exercise .exercise-audioAsset {
    color: #da0000;
    font-size: 1.5em;
}

.exercise .exercise-choice label,
.exercise .exercise-footer button,
.exercise .exercise-footer a.button,
.exercise-item, .exercise-gap-item {
    background: #0cc3ff;
    margin:5px;
    display: inline-block;
    padding: 5px 10px;
    cursor: pointer;
}

.exercise .exercise-choice {
    display: inline-block;
}

.exercise .exercise-group {
    margin: 2px 0 2px 0;
    line-height: 3em;
    background: #f7f7f7;
}

.exercise-gap-drag, .exercise-sequence-drag {
    background: #f7f7f7;
    padding: 2px;
}

.exercise-gap-drag {
    padding: 0px;
    width: 10em;
    vertical-align: middle;
    border: 1px dashed;
    border-radius: 10px;
    margin-bottom: 1px;
    margin-top: 1px;
}

.undropped.exercise-gap-drag {
    height: 44px;
    display: inline-block;
}

.dropped.exercise-gap-drag {
    height: auto;
    min-height: 44px;
    width: auto;
    min-width: 160px;
}

.currentMove{
    position:fixed;
    z-index:50000;
}

.exercise-sequence-drag {
    min-height: 3em;
}

.exercise .exercise-group-title, .exercise-gap-item {
    margin-right: 1em;
    margin: 5px;
    display: inline-block;
    padding: 2px 4px;
}

.exercise .exercise-footer {
    margin-top: 1em;
    margin-bottom: 1em;
}

.results {
    font-size: 1.5em;
}

.exercise-context {
    padding: 0px 10px 0px 10px;
    text-align: center;
    font-weight: bold;
}
.exercise-context.static{
    text-align: left;
}

.exercise-rubric div,
.exercise-mc,
.exercise-mc div,
.exercise-gapfill div,
.exercise-audioAsset,
.gapfill-drag div,
.result{
    display: inline-block;
}

.exercise-mc {
    text-align: center;
    width: 100%;
}

.view {
    overflow: hidden;
    position: relative;
    width:1px;
    background-color: white;
    margin-top: 20px;
}

.container {
    position: absolute;
    top: 0;
    transition: all 0.7s ease;
    left:0;
    overflow-x: auto;
    white-space: nowrap;
}

.round-button {
    display:block;
    height: 1.5em;
    width: 1.5em;
    border-radius: 50%;
    border: 1px solid black;
}
img.contextImage {
    float: none;
    width: auto;
}
.finalResult {
    text-align: center;
    display:inline-block;
    padding: 10px;
}

select, .exercise-gap input {
    margin: 2px;
    border: 1px solid black;
    padding-left: 0.5em;
}

.select-question.correct, .exercise-gap-input.correct {
    background-color: #2E4B0F;
    color: #ffffff;
}

.select-question.error, .exercise-gap-input.error {
    background-color: #730C14;
    color: #ffffff;
}

.exercise-gap-input.error[disabled] {
    background-color: #FFFFFF;
    color: #000000;
}

.select-question.correct,.select-question.error {
    -moz-appearance: none; /* for Firefox */
    -webkit-appearance: none; /* for Chrome */
}

.select-question.correct::-ms-expand, .select-question.error::-ms-expand {
    display: none; /* for IE10 */
}

/* .error {
    background-color: #E61928;
    border-color: #000000;
    color: #ffffff;
}

.correct {
    background: #f6fff9;
    border-color: rgb(117, 222, 117);
    color: #44c361;
}
 */
#tocTitle {
    text-align: left;
}

.prep {
    margin-left: 3em;
}

.bottom-fixed-bar {
    position: fixed;
    bottom: 0;
    background-color: rgba(180, 183, 189, 0.53);
    left: 0;
}

.exercise-reading p {
    text-align: left;
}

.inline-div {
    display: inline-block;
}

.auto-div .exercise-sequence-drag{
    height: auto;
}
.opt_content {
    width: 400px;
    margin: 0 auto;
    text-align: left;
}
.items_content {
    display: none;
    margin: auto;
    padding: 10px;
}
.items_title {
    font-weight: bold;
    cursor: pointer;
}
#dot {
    font-size: 14px;
    margin-right: 5px;
    cursor: pointer;
}

.exercise .exercise-choice label, .exercise .exercise-footer a.button, 
.exercise-item, .exercise-gap-item, .exercise .exercise-group .exercise-item {
    background: #416cd0;
    margin: 5px 1px 5px 1px;
    display: inline-block;
    padding: 5px 8px;
    cursor: pointer;
    color: white;
}

.exercise-gap-item {
    margin: 4px;
}

.exercise .exercise-choice label{
    border-radius: 5px;
}

.inline{
    display: inline-block;
}
.margin1{
    margin-top: 1em;
    white-space: initial;
}
.b1{
    vertical-align: middle;
    padding-right: 10px;
}

.exercise-question {
    display: inline-block;
    vertical-align: top;
    white-space: initial;
    padding-left: 12px;
    padding: 10px;
}

.exercise-gapfill-drag {
    margin-top: 1em;
}

.exercise-gapfill-drag-bag {
    white-space: initial;
}

.exercise-gap-item, .exercise-item {
    display: inline-block;
    vertical-align: middle;
    border-radius: 5px;
}

.exercise-footer button.exercise-replay, 
.exercise-footer button.exercise-show {
    display: none;
}
.exercise-footer button.exercise-replay.inline,
.exercise-footer button.exercise-show.inline {
    display: inline-block;
}
.exercise .exercise-footer button{
    background-color: #6d97d2;
    border-radius: 18px;
    border: 2px solid #6d97d2;
    color : rgb(238, 238, 238);
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
}
.exercise .exercise-footer button:hover {
    background-color: rgb(238, 238, 238);
    color: #6d97d2;
}
.exercise .exercise-footer button.exercise-correct {
	display: none;
}
label .fa, .exercise-gap-item .fa, .exercise-item .fa {
    margin-left: 10px;
}

@media screen and (min-width: 360px) and (max-width: 812px) {
    .exercise-gapfill-drag {
        margin-top: 0;
    }
    .exercise-mc div {
    	display: block;
   	}
    .exercise .exercise-choice {
    	display: block;
	}
	.exercise .exercise-choice label {
		width: 100%;
		text-align: center;
	}
}

/* BREADCRUMB */

ol.breadcrumb {
  margin-left: 18px;
  white-space: nowrap;
  width: 100%;
  letter-spacing: -0.31em;
}

ol.breadcrumb li {
  position: relative;
  margin-left: -18px;
  font-size: 17px;
  display: inline-block;
}

ol.breadcrumb li a, ol.breadcrumb li:hover a {
  background-color: #4064A3;
  color: white;
  padding: 0 .6em;
  display: inline-block;
  line-height: 30px;
  vertical-align: middle;
  transition: unset;
}

ol.breadcrumb li a {
  letter-spacing: normal;
  font-size: 13px;
  border: none;
  cursor: pointer;
  background-color: #314089;
}

ol.breadcrumb li:after, ol.breadcrumb li:before {
  content: "";
  display: inline-block;
  vertical-align: middle;
}

ol.breadcrumb li:before {
  border-top: 15px solid #314089;
  border-bottom: 15px solid #314089;
  border-left: 20px solid transparent;
}

ol.breadcrumb li:after {
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 20px solid #314089;
}

ol.breadcrumb li:hover:before {
  border-top: 15px solid #4064A3;
  border-bottom: 15px solid #4064A3;
  border-left: 20px solid transparent;
}

ol.breadcrumb li:hover:after {
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 20px solid #4064A3;
}

ol.breadcrumb li:first-child:before{
  content: "";
  border: none;
}

ol.breadcrumb li a:hover {
  text-decoration: underline;
}

nav {
	padding-bottom: 1em;
}

/* FIN BREADCRUMB*/

div.about p, div.about blockquote {
	display: block;
	margin-block-start: 1em;
	margin-block-end: 1em;
}

div.about blockquote {
	margin-inline-start: 40px;
	margin-inline-end: 40px;
}

h1 span {
	color: #4064A3;
	font-weight: normal;
	font-size: smaller;
	display: table;
}

h2 {
	font-size: 1.4em;	
}

div.centerBlock div {
	margin-bottom: 25px;
}

.exercise-section {
	margin-bottom: 5px;
	color: #314089;
}

.exercise-section a:hover {
	text-decoration: underline;
}

div.centerBlock div.exercise-introduction {
	margin-bottom: 25px;
}@font-face {
  font-family: 'longmaneltdict';
  src:  url(https://d27ucmmhxk51xv.cloudfront.net/external/fonts/longmaneltdict.eot?version=1.1.89);
  src:  url(https://d27ucmmhxk51xv.cloudfront.net/external/fonts/longmaneltdict.eot?version=1.1.89) format('embedded-opentype'),
    url(https://d27ucmmhxk51xv.cloudfront.net/external/fonts/longmaneltdict.ttf?version=1.1.89) format('truetype'),
    url(https://d27ucmmhxk51xv.cloudfront.net/external/fonts/longmaneltdict.woff?version=1.1.89) format('woff'),
    url(https://d27ucmmhxk51xv.cloudfront.net/external/fonts/longmaneltdict.svg?version=1.1.89) format('svg');
  font-weight: normal;
  font-style: normal;
}

[class^="icon-"], [class*=" icon-"] {
  /* use !important to prevent issues with browser extensions that change fonts */
  font-family: 'longmaneltdict';
  speak: none;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;

  /* Better Font Rendering =========== */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.icon-1010:before {
  content: "\e900";
}
.icon-up:before {
  content: "\e602";
}
.icon-right:before {
  content: "\e603";
}
.icon-left:before {
  content: "\e604";
}
.icon-down:before {
  content: "\e605";
}
.icon-quotes:before {
  content: "\e610";
}
.icon-logo:before {
  content: "\e613";
}
.icon-comment:before {
  content: "\e614";
}
.icon-interrogation:before {
  content: "\e616";
}
.icon-tab:before {
  content: "\ea45";
}
.modal.open {
    display: block;
}

.modal--myd {
    background: #fff;
}

.modal {
    display: none;
    position: absolute;
    z-index: 11501;
    top: 0;
    right: 0;
    left: 0;
    margin: 20px auto 0;
    margin-top: 20px;
    width: 90%;
    max-width: 720px;
    min-height: 380px;
    background: #fff;
    box-shadow: 0 0 8px rgba(0, 0, 0, .05);
}

.modal__close {
    position: absolute;
    top: -8px;
    right: -8px;
    height: 32px;
    line-height: 30px;
    width: 32px;
    text-align: center;
    border-radius: 100%;
    cursor: pointer;
}

.modal__close .fa {
    color: #e84526;
    font-size: 1.6em;
}

.overlay {
    display: none;
    position: fixed;
    z-index: 11500;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background: #dde2ed;
    background: rgba(221, 226, 237, .9);
}

.overlay--active {
    display: block;
}

@media screen and (min-width: 1080px) {
    .modal {
        margin-top: 50px;
    }
}
.translator-form, .translator-translations {
	background: #314089;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 0.9em;
}

.translator-form h1 {
	color: #FFF;
	font-size: 1.35em;
	margin: 0 0 10px;
}

.translator-form label {
	display: block;
    background: #dedddd;
    text-transform: capitalize;
    border-radius: 5px;
    margin: 5px;
}

.translator-form label span {
	box-sizing: border-box;
    width: 72px;
	display: inline-block;
	font-weight: bold;
    padding: 0.5em 0.3em;
}

.translator-form .controls, .translator-form textarea, .translator-form .footer, .translator-form input {
	background: #FFF;
	border: none;
    font-size: inherit;
    padding: 0.5em 0.3em;
    border-radius: 5px;
    margin-bottom: 5px;
}

.translator-form .controls {
	padding: 0;
}

.translator-form .from {
	border-radius: 5px 0 0 5px; 
}

.translator-form .to {
	border-radius: 0 5px 5px 0; 
}

.translator-form .se-select, .translator-form .switch:not(.disabled ), .footer input {
    cursor: pointer;
}

.translator-form .se-select, .translator-form button {
    float: left;
}

.translator-form .switch {
    box-sizing: border-box;
    width: 30px;
    border: none;
    padding: 0.5em 0.3em;
    text-transform: capitalize;
    margin: 0;
    outline: none;
    background: none;
    line-height: inherit;
}

.translator-form .switch.disabled {
    opacity: 0;
}

.translator-form .error {
    background: #FFF;
    color: red;
    padding: 0.3em;
    font-size: 0.9em;
}

.translator-form textarea {
    width: 100%;
	font-size: inherit;
	font-family: inherit;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    margin-bottom: 0;
    outline: none;
    vertical-align: top;
}

.translator-form .footer {
	display: block;
    margin-top: 0;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    padding: 0;
    vertical-align: top;
    color: #666;
    position: relative;
}

.translator-form .limit {
    position: absolute;
    padding: 5px 15px;
    bottom: 0;
    font-size: 0.8em;
}

.translator-form input {
    float: right;
    border-radius: 5px 0;
    background: #e4c738;
    font-weight: bold;
    padding: 0.5em 0.5em;
    margin: 0;
}

.translator-translations {
	background: #dedddd;
}

.translator-translations p {
    padding: 0.5em 0em;
}

/* Select */
.translator-form .se-select {
	position: relative;
	box-sizing: border-box;
	width: calc(50% - 15px);
    padding: 0;
    text-transform: capitalize;
    margin: 0;
    outline: none;
    background: #dedddd;
    height: auto;
}

.translator-form .se-select .se-text {
    padding: 0.5em 0.5em;
    white-space: nowrap; 
    overflow: hidden;
    text-overflow: ellipsis;
    display: inline-block;
    width: calc(100% - 25px);
    vertical-align: middle;
}

.translator-form .se-select .se-options {
	position: absolute;
	box-sizing: border-box;
	min-width: calc(100% + 30px);
    max-height: 17em;
    padding: 0.5em 0.3em;
    background: white;
    overflow: auto;
    z-index: 1000;
    border-radius: 0 0 5px 5px;
    box-shadow: 0 2px 3px 0 rgba(34,36,38,.15);
}

.translator-form .se-select .se-option {
    border-top: 1px solid #fafafa;
    padding: 0.25em 0.5em;
}

.translator-form .se-select .se-option:hover {
	background: #ccc;
}

.translator-form .se-select .se-option.se-selected {
	background: rgba(0,0,0,.03);
    color: rgba(0,0,0,.95);
    font-weight: bold;
}@media screen and (max-width: 761px){
	.header {
		height: auto
	}
	
	.header .logo_link {
		width: auto;
        margin: 10px;
	}
	
	.header .logo {
	    width: 39px;
	}
	
	.header .search_form {
		width: calc(100% - 110px);
	}
	
	.header .header_version {
		vertical-align: bottom;
	    margin: 0px 0px 10px 0px;
	    border-radius: 5px;
    	background: #dedddd;
    	padding: 16px 8px;
    	height: 56px;
    	display: inline-flex;
    	align-items: center;
    	justify-content: space-between;
    	position: static;
    	color: #666;
	}
	
	.header .header_version .fa-globe {
		margin: 0;
	}
	
	.header .header_version .text {
		display: none;
	}
}
}

</style>"""
print(css, '\n')

soup = BeautifulSoup(url, 'lxml')
for body in soup.find_all('div', 'entry_content'):
    print(css, body)
    
