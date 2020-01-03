
var globalStore = {
	// --- start
	// openId: null,
	// // --- free_text
	// patient: {age: localStorage.getItem('age') === null ? '12' : localStorage.getItem('age'), gender: localStorage.getItem('gender') === null ? '男' : localStorage.getItem('gender')},       // age, gender
	// hotItems: [],
	// historyItems: [],
	// queryText: '',
	// selectItems: [],
	// symptomItems: [],
	// // --- symptom_list
	// entityList: [],
	// understand: true,
	// // --- add_new_symptom ---
	// wait: false,
	// candidates: [],
	// // --- hospital_list
	// hospitals: [],
	// showHospitals: [],
	// currentLocation: '',
	// orderMethod: '智能排序',
	// levelFilter: '全部医院',
	// token: ''
};

$(function () {
	function handleFontSize(){
		// 设置网页字体为默认大小
		WeixinJSBridge.invoke('setFontSizeCallback', { 'fontSize' : 0 });
		// 重写设置网页字体大小的事件
		WeixinJSBridge.on('menu:setfont', function() {
			WeixinJSBridge.invoke('setFontSizeCallback', { 'fontSize' : 0 });
		});
	}

	function preload(){
		//修正微信字体

		if (typeof WeixinJSBridge == 'object' && typeof WeixinJSBridge.invoke == 'function') {
			handleFontSize();
		} else {
			if (document.addEventListener) {
				document.addEventListener('WeixinJSBridgeReady', handleFontSize, false);
			} else if (document.attachEvent) {
				document.attachEvent('WeixinJSBridgeReady', handleFontSize);
				document.attachEvent('onWeixinJSBridgeReady', handleFontSize);
			}
		}
		// 对浏览器的UserAgent进行正则匹配，不含有微信独有标识的则为其他浏览器
		var useragent = navigator.userAgent;
		var wechatAgent = useragent.match(/MicroMessenger/i);
		var androidAgent = useragent.match(/Android/i);
		var windowsAgent = useragent.match(/WindowsWechat/i);

		// if (!wechatAgent || windowsAgent || wechatAgent.length <=0) {

		// 	var errorMsgHtml = template('tpl_msg_warn', {
		// 		desc: '请在微信客户端打开链接',
		// 		btnId: 'msgWarnClose',
		// 		btnClass: 'weui-msg__content-btn',
		// 	});
		// 	errorMsgHtml = $(errorMsgHtml).addClass('js_show').addClass('msgWarn');
		// 	$('#container').html(errorMsgHtml);
		// 	$('#container #msgWarnClose').off('click').on('click', function(){
		// 		window.opener=null;
		// 		window.open('','_self');
		// 		window.close();
		// 	});
		// 	return false;
		// }

		$(window).on('load', function(){
			var imgList = [];
			for (var i = 0, len = imgList.length; i < len; ++i) {
				new Image().src = imgList[i];
			}
		});
		return true;
	}

	// function setJSAPI(){
	// 	var jsApiUrl = URL.GET_WECHAT_CONFIG
	// 		.replace('{url}', encodeURIComponent(location.href.split('#')[0]));
	// 	$http.get(jsApiUrl, null, false, function (res) {
	// 		wx.config(res);
	// 		wx.ready(function () {
	// 			//隐藏右上角菜单
	// 			wx.hideOptionMenu();
	// 		});
	// 	});
	// }

	function setPageManager(){
		var winH = $(window).height();
		pageManager.push(healthy_travel)
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
			.setDefault('healthy_travel')
			.init();
	}

	//init
	var isPreLoadOK = preload();
	if (!isPreLoadOK){
		return false;
	}
	// setJSAPI();
    wx.hideOptionMenu();
	setPageManager();

	window.pageManager = pageManager;
	window.home = function(){
		location.hash = '';
	};
});
