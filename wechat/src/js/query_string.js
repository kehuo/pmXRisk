//获取QueryString的数组
function getQueryString() {
    var result = location.search.match(new RegExp('[\?\&][^\?\&]+=[^\?\&]+', 'g'));
    if (result == null) {
        return '';
    }
    for (var i = 0; i < result.length; i++) {
        result[i] = result[i].substring(1);
    }
    return result;
}

//根据QueryString参数名称获取值
function getQueryStringByName(name) {
    var result = location.search.match(new RegExp('[\?\&]' + name + '=([^\&]+)', 'i'));
    if (result == null || result.length < 1) {
        return '';
    }
    return result[1];
}

function getQueryStringByNameAndFullUrl(name) {
    var fieldsA = location.href.split('/');
    var lastOneField = fieldsA[fieldsA.length-1];
    if (!lastOneField.startsWith('?')) {
        return null;
    }
    var result = lastOneField.match(new RegExp('[\?\&]' + name + '=([^\&]+)', 'i'));
    if (result == null || result.length < 1) {
        return '';
    }
    return result[1];
}

function buildQueryString(params, paramStr) {
    var result = '';
    var cnt = 0;
    for (var key in params) {
        var value = params[key];
        var strVal = null;
        switch (typeof value) {
        case 'number':
        case 'boolean':
        case 'string':
            strVal = String(value);
            break;
        case 'object':
            if (value.constructor === Array) {
                strVal = value.toString();
            }
            break;
        default:
            break;
        }
        if (strVal) {
            var curPart = '&';
            if (cnt === 0) {
                curPart = '?';
            }
            curPart += key + '=' + strVal;
            result += curPart;
            cnt++;
        }
    }
    if (paramStr) {
        if (result === ''){
            result = '?' + paramStr;
        } else {
            result += '&' + paramStr;
        }
    }

    return result;
}


function setToken(value) {
	window.localStorage.setItem('token', value);
}

function getToken() {
    var token = window.localStorage.getItem('token');
    return token
}

// function setCookie(c_name,value,expiredays)
// {
// 	var exdate=new Date();
// 	exdate.setDate(exdate.getDate()+expiredays);
// 	document.cookie=c_name+ "=" + value +
// 		((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
// }

//取回cookie
// function getCookie(c_name)
// {
//     console.log('get Cookie: ', c_name, globalStore);
// 	if (globalStore.token && globalStore.token !== '') {
// 	    console.log('get token');
// 		return globalStore.token
// 	}
// 	if (document.cookie.length>0)
// 	{
// 		c_start=document.cookie.indexOf(c_name + "=");
// 		if (c_start!=-1)
// 		{
// 			c_start=c_start + c_name.length+1;
// 			c_end=document.cookie.indexOf(";",c_start);
// 			if (c_end==-1) c_end=document.cookie.length;
// 			return document.cookie.substring(c_start,c_end)
// 		}
// 	}
// 	return ''
// }
