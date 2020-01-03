var globalStore = {
    homeProcess:{}
};
$(function () {
    function preload(){
        // 对浏览器的UserAgent进行正则匹配，不含有微信独有标识的则为其他浏览器
        var useragent = navigator.userAgent;
        var wechatAgent = useragent.match(/MicroMessenger/i);
        var androidAgent = useragent.match(/Android/i);
        var windowsAgent = useragent.match(/WindowsWechat/i);
        // if (!wechatAgent || windowsAgent || wechatAgent.length <=0) {
        //     var errorMsgHtml = template('tpl_shared_msg_error', {
        //         title: '请在微信客户端打开链接',
        //         btnText: '关闭',
        //         btnId: 'mrClose',
        //     });
        //     $('#container').html(errorMsgHtml);
        //     $('#container #mrClose').unbind('click').click(function(){
        //         window.opener=null;
        //         window.open('','_self');
        //         window.close();
        //     });
        //     return false;
        // }

        $(window).on('load', function(){
            var imgList = [
                './images/layers/content.png',
                './images/layers/navigation.png',
                './images/layers/popout.png',
                './images/layers/transparent.gif'
            ];
            for (var i = 0, len = imgList.length; i < len; ++i) {
                new Image().src = imgList[i];
            }
        });
    }

    function setJSAPI(){
        $.getJSON('https://xxx.com/api/sign?url=' + encodeURIComponent(location.href.split('#')[0]), function (res) {
            wx.config({
                beta: true,
                debug: false,
                appId: res.appid,
                timestamp: res.timestamp,
                nonceStr: res.nonceStr,
                signature: res.signature,
                jsApiList: [
                    'onMenuShareTimeline',
                    'onMenuShareAppMessage',
                    'onMenuShareQQ',
                    'onMenuShareWeibo',
                    'onMenuShareQZone',
                    // 'setNavigationBarColor',
                    'setBounceBackground'
                ]
            });
            wx.ready(function () {
                /*
                 wx.invoke('setNavigationBarColor', {
                 color: '#F8F8F8'
                 });
                 */
                wx.invoke('setBounceBackground', {
                    'backgroundColor': '#F8F8F8',
                    'footerBounceColor' : '#F8F8F8'
                });

                wx.onMenuShareAppMessage({
                    title: 'WeUI',
                    desc: '为微信 Web 服务量身设计',
                    link: location.href,
                    imgUrl: 'https://mmbiz.qpic.cn/mmemoticon/ajNVdqHZLLA16apETUPXh9Q5GLpSic7lGuiaic0jqMt4UY8P4KHSBpEWgM7uMlbxxnVR7596b3NPjUfwg7cFbfCtA/0'
                });
                wx.onMenuShareTimeline({
                    title: 'WeUI, 为微信 Web 服务量身设计',
                    desc: 'WeUI, 为微信 Web 服务量身设计',
                    link: 'https://weui.io',
                    imgUrl: 'https://mmbiz.qpic.cn/mmemoticon/ajNVdqHZLLA16apETUPXh9Q5GLpSic7lGuiaic0jqMt4UY8P4KHSBpEWgM7uMlbxxnVR7596b3NPjUfwg7cFbfCtA/0'
                });
                wx.onMenuShareQQ(option);
            });
        });
    }

    function setPageManager(){
        var winH = $(window).height();
        pageManager.push(home)
            .push(button)
            .push(list)
            .push(input)
            .push(toast)
            .push(dialog)
            .push(progress)
            .push(msg)
            .push(msgSuccess)
            .push(msgWarn)
            .push(article)
            .push(navbar)
            .push(tabbar)
            .push(panel)
            .push(actionsheet)
            .push(icons)
            .push(searchbar)
            .push(footer)
            .push(picker)
            .push(gallery)
            .push(flex)
            .push(loadmore)
            .push(layers)
            .push(uploader)
            .push(preview)
            .push(grid)
            .push(mxnBasicInfo)
            .push(mxnSurvey)
            .setPageAppend(function($html){
                var $foot = $html.find('.page__ft');
                if ($foot.length < 1){
                    return;
                }

                if ($foot.position().top + $foot.height() < winH){
                    $foot.addClass('j_bottom');
                } else {
                    $foot.removeClass('j_bottom');
                }
            })
            .setDefault('home')
            .init();
    }

    //init
    preload();
    setJSAPI();
    setPageManager();

    window.pageManager = pageManager;
    window.home = function(){
        location.hash = '';
    };
});
