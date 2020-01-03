function errorAllHandler(result, errHandle) {
    if (result.status === 401 || result.status === 403) {
        $.alert('无权访问，请重新登录！', function() {
            location.href = URL.WECHAT_OATUTH_CLIENT
                            .replace('{appId}', config.wechat.service.appid)
                            .replace('{redirectUri}', config.serverUri);
        });
        return;
    }
    if (errHandle) {
        errHandle(result);
    } else if (result.response) {
        var resJson = JSON.parse(result.response);
        if (resJson && resJson.errorMessage){
            $.alert(resJson.errorMessage);
        }
        return;
    }
}

function buildGetParamsAsBBFormat(data) {
    if (!data) {
        return null;
    }
    var result = JSON.stringify(data);
    return {param: result};
}

//Http
var $http = {};
$http.get = function (url, data, isasync, handle, errHandle, loading=false) {
    $.ajax({
        type: 'GET',
        async: isasync,
        url: config.apiUri + url,
        // data to be added to query string, such as:{ name: 'Zepto.js' }
        data: buildGetParamsAsBBFormat(data),
        dataType: 'text',
        cache: false,
        xhrFields: {
            withCredentials: true
        },
	    beforeSend: function(request) {
            if (loading) {
                $.showLoading();
            }
		    // var token = getToken();
		    // if (token !== '') {
			//     request.setRequestHeader('token', token);
		    // }
	    },
	    contentType: 'application/json',
        success: function (result) {
            //有时微信返回会出现option方法莫名变为GET获得OK导致异常的现象，在此改为获取text自行转换json
            if (result === 'OK'){
                return;
            }
            if (!result || result === 'null'){
                $.alert('获取信息失败');
                return;
            }
            var rstData = JSON.parse(result);
            handle(rstData);
            if (loading) {
                $.hideLoading();
            }
        },
        error: function (xhr, errorType, error) {
            errorAllHandler(xhr, errHandle);
            // alert(JSON.stringify(xhr));
            // alert(errorType);
            // alert(error);
            if (loading) {
                $.hideLoading();
            }
        }
    });
};

$http.post = function (url, data, isasync, handle, errHandle) {
    var payload = {};
	var token = getToken();
	console.log('globalStore', globalStore, globalStore.token);
    if (typeof (data) === 'object') {
	    payload = JSON.parse(JSON.stringify(data));
	    if (token != '') {
            payload['token']= token;
	    }
	    payload = JSON.stringify(payload);
    } else {
	    payload = data
    }
    console.log('payload', payload);

    $.ajax({
        type: 'POST',
        async: isasync,
        url: config.apiUri + url,
        // post payload:
        // data: typeof (data) == 'object' ? JSON.stringify(data) : data,
	    data: payload,
        dataType: 'json',
	    cache: false,
	    xhrFields: {
            withCredentials: true
        },
	    beforeSend: function(request) {
        	// var token = getToken();
            // if (token !== '') {
	        //     request.setRequestHeader('token', token);
            // }
	    },
        contentType: 'application/json',
        success: function (result, textStatus, request) {
            var token = request.getResponseHeader('set-token');
            if (token && token !== '') {
	            setToken(token)
            }
            handle(result);
        },
        error: function (xhr, errorType, error) {
            errorAllHandler(xhr, errHandle);
	        // alert(JSON.stringify(xhr));
	        // alert(errorType);
	        // alert(error);
        }
    });
};

$http.put = function (url, data, isasync, handle, errHandle) {
	var payload = {};
	var token = getToken();
	console.log('globalStore', globalStore, globalStore.token);
	if (typeof (data) === 'object') {
		payload = JSON.parse(JSON.stringify(data));
		if (token != '') {
			payload['token']= token;
		}
		payload = JSON.stringify(payload);
	} else {
		payload = data
	}

    $.ajax({
        type: 'PUT',
        async: isasync,
        url: config.apiUri + url,
        // put payload:
        // data: typeof (data) == 'object' ? JSON.stringify(data) : data,
        dataType: 'json',
	    data: payload,
        xhrFields: {
            withCredentials: true
        },
	    cache: true,
	    beforeSend: function(request) {
		    var token = getToken();
		    if (token !== '') {
			    request.setRequestHeader('token', token);
		    }
	    },
	    contentType: 'application/json',
        success: function (result) {
            handle(result);
        },
        error: function (xhr, errorType, error) {
            errorAllHandler(xhr, errHandle);
            // alert(JSON.stringify(xhr));
            // alert(errorType);
            // alert(error);
        }
    });
};

$http.del = function (url, data, isasync, handle, errHandle) {
	var payload = {};
	var token = getToken();
	console.log('globalStore', globalStore, globalStore.token);
	if (typeof (data) === 'object') {
		payload = JSON.parse(JSON.stringify(data));
		if (token != '') {
			payload['token']= token;
		}
		payload = JSON.stringify(payload);
	} else {
		payload = data
	}

    $.ajax({
        type: 'DELETE',
        async: isasync,
        url: config.apiUri + url,
        // delete payload:
        // data: typeof (data) == 'object' ? JSON.stringify(data) : data,
	    data: payload,
        dataType: 'json',
        xhrFields: {
            withCredentials: true
        },
	    beforeSend: function(request) {
		    var token = getToken();
		    if (token !== '') {
			    request.setRequestHeader('token', token);
		    }
	    },
        contentType: 'application/json',
        success: function (result) {
            handle(result);
        },
        error: function (xhr, errorType, error) {
            errorAllHandler(xhr, errHandle);
            // alert(JSON.stringify(xhr));
            // alert(errorType);
            // alert(error);
        }
    });
};
