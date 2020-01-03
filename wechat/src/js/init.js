window.onerror = function(errorMessage, scriptURI, lineNumber,columnNumber,errorObj) {
    var error = [];
    error.push('错误信息：' + errorMessage);
    error.push('出错文件：' + scriptURI);
    error.push('出错行号：' + lineNumber);
    error.push('出错列号：' + columnNumber);
    error.push('错误详情：' + JSON.stringify(errorObj));
    alert(error);
};

var pageManager = {
    $container: $('#container'),
    _pageStack: [],
    _configs: [],
    _pageAppend: function(){},
    _defaultPage: null,
    _pageIndex: 1,
    _pageRender: {},
    setDefault: function (defaultPage) {
        this._defaultPage = this._find('name', defaultPage);
        return this;
    },
    setPageAppend: function (pageAppend) {
        this._pageAppend = pageAppend;
        return this;
    },
    init: function () {
        var self = this;

        $(window).on('hashchange', function () {
            var state = history.state || {};
            var url = location.hash.indexOf('#') === 0 ? location.hash : '#';
            var page = self._find('url', url) || self._defaultPage;
            if (state._pageIndex <= self._pageIndex || self._findInStack(url)) {
                self._back(page);
            } else {
                self._go(page);
            }
        });

        if (history.state && history.state._pageIndex) {
            this._pageIndex = history.state._pageIndex;
        }

        this._pageIndex--;

        var url = location.hash.indexOf('#') === 0 ? location.hash : '#';
        var page = self._find('url', url) || self._defaultPage;
        this._go(page);
        return this;
    },
    push: function (config) {
        this._configs.push(config);
        return this;
    },
    go: function (to) {
        var config = this._find('name', to);
        if (!config) {
            return;
        }
        location.hash = config.url;
    },
    _go: function (config) {
        this._pageIndex ++;

        history.replaceState && history.replaceState({_pageIndex: this._pageIndex}, '', location.href);

        // delete body .weui-msg__extra-area
        $('body .weui-msg__extra-area').remove();

        var html = config.render();
        var $html = $(html).addClass('slideIn').addClass(config.name);
        $html.on('animationend webkitAnimationEnd', function(){
            $html.removeClass('slideIn').addClass('js_show');
        });
        this.$container.html($html);
        this._pageAppend.call(this, $html);
        //bind events
        if (typeof config.bind === 'function') {
            config.bind.call(this.$container);
        }
        this._pageStack.push({
            config: config,
            dom: $html
        });

        // add title name
        setPageTitle(config.title);

        return this;
    },
    back: function () {
        history.back();
    },
    _back: function (config) {
        this._pageIndex --;

        var stack = this._pageStack.pop();
        if (!stack) {
            return;
        }

        var url = location.hash.indexOf('#') === 0 ? location.hash : '#';
        // var found = this._findInStack(url);
        // if (!found) {
        //     var html = config.render();
        //     var $html = $(html).addClass('js_show').addClass(config.name);
        //     $html.insertBefore(stack.dom);

        //     if (!config.isBind) {
        //         this._bind(config);
        //     }
        //     this._pageStack.push({
        //         config: config,
        //         dom: $html
        //     });
        // }
        // delete body .weui-msg__extra-area
        $('body .weui-msg__extra-area').remove();

        var html = config.render();
        var $html = $(html).addClass('js_show').addClass(config.name);
        $html.insertBefore(stack.dom);

        if (!config.isBind) {
            this._bind(config);
        }
        this._pageStack.push({
            config: config,
            dom: $html
        });
        // add title name
        setPageTitle(config.title);

        stack.dom.addClass('slideOut').on('animationend webkitAnimationEnd', function () {
            stack.dom.remove();
        });
        //bind events
        if (typeof config.bind === 'function') {
            config.bind.call(this.$container);
        }
        return this;
    },
    _findInStack: function (url) {
        var found = null;
        for (var i = 0, len = this._pageStack.length; i < len; i++){
            var stack = this._pageStack[i];
            if (stack.config.url === url) {
                found = stack;
                break;
            }
        }
        return found;
    },
    _find: function (key, value) {
        var params = {};
        var tempVal = value;
        if (tempVal){
            var valueSplitIndex = tempVal.indexOf('/');
            if (valueSplitIndex > -1){
                value = tempVal.substring(0, valueSplitIndex);
                var paramsStr = tempVal.substring(valueSplitIndex);
                var query = paramsStr.match(new RegExp('[\?\&][^\?\&]+=[^\?\&]+', 'g'));
                if (query && query.length>0) {
                    var queryRst = {};
                    for (var q = 0; q < query.length; q++) {
                        var querySplitIndex = query[q].indexOf('=');
                        var queryKey = query[q].substring(1, querySplitIndex);
                        var queryVal = query[q].substring(querySplitIndex+1);
                        queryRst[queryKey] = queryVal;
                    }
                    params.query = queryRst;
                }
            }
        }
        var page = null;
        for (var i = 0, len = this._configs.length; i < len; i++) {
            if (this._configs[i][key] === value) {
                this._configs[i].params = params;
                page = this._configs[i];
                break;
            }
        }
        return page;
    },
    _bind: function (page) {
        var events = page.events || {};
        for (var t in events) {
            for (var type in events[t]) {
                this.$container.on(type, t, events[t][type]);
            }
        }
        page.isBind = true;
    }
};

function setPageTitle(title){
    // add title name
    document.title = title;
    // if (globalStore.survey.schema && globalStore.survey.schema.name){
    //     document.title = globalStore.survey.schema.name;
    // }
    // hack在微信等webview中无法修改document.title的情况
    var iframe = document.createElement('iframe');
    iframe.src = '/favicon.ico';
    iframe.style.visibility = 'hidden';
    iframe.onload = function () {
        setTimeout(function () {
            document.body.removeChild(iframe);
        }, 0);
    };
    document.body.appendChild(iframe);
}

function androidInputBugFix(){
    // .container 设置了 overflow 属性, 导致 Android 手机下输入框获取焦点时, 输入法挡住输入框的 bug
    // 相关 issue: https://github.com/weui/weui/issues/15
    // 解决方法:
    // 0. .container 去掉 overflow 属性, 但此 demo 下会引发别的问题
    // 1. 参考 http://stackoverflow.com/questions/23757345/android-does-not-correctly-scroll-on-input-focus-if-not-body-element
    //    Android 手机下, input 或 textarea 元素聚焦时, 主动滚一把
    if (/Android/gi.test(navigator.userAgent)) {
        window.addEventListener('resize', function () {
            if (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA') {
                window.setTimeout(function () {
                    document.activeElement.scrollIntoViewIfNeeded();
                }, 0);
            }
        });
    }
}


//init
$(function () {
    FastClick.attach(document.body);
    androidInputBugFix();
});
