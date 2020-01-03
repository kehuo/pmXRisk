var getOption = function() {
    var pm25data = [];
    var pm10data = [];
    var xAxisData = [];

    for (var i = 0; i < globalStore.pmInfo.data.length; i++) {
        xAxisData.push(globalStore.pmInfo.data[i].hour);
        var symbolMark = i % 4 === 0;
        pm25data.push({
            value: globalStore.pmInfo.data[i].pm25,
            symbol: symbolMark ? 'circle' : 'none',
            symbolSize: symbolMark ? 4 : 0,
            label: {
                show: symbolMark,
                position: globalStore.pmInfo.data[i].pm25 > globalStore.pmInfo.data[i].pm10 ? 'top' : 'bottom',
            }
        });
        pm10data.push({
            value: globalStore.pmInfo.data[i].pm10,
            symbol: symbolMark ? 'circle' : 'none',
            symbolSize: symbolMark ? 4 : 0,
            label: {
                show: symbolMark,
                position: globalStore.pmInfo.data[i].pm25 > globalStore.pmInfo.data[i].pm10 ? 'bottom' : 'top',
            }
        });
    }

    var option = {
        grid: {
            right: 0,
            top: 35,
            bottom: 20
        },
        legend: {
            selectedMode: false,
            data: [{
                name: 'PM2.5',
                textStyle: {
                    color: '#fff'
                }
            },{
                name: 'PM10',
                textStyle: {
                    color: '#f7b500'
                }
            }]
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                interval: 3,
                color: 'rgba(255,255,255,0.4)',
                // formatter: function(value, index) {
                //     var date = new Date(value);
                //     return date.getHours();
                // }
            },
            data: xAxisData,
        },
        yAxis: {
            type: 'value',
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisLabel: {
                color: 'rgba(255,255,255,0.4)',
            },
        },
        series: [{
            name: 'PM2.5',
            data: pm25data,
            type: 'line',
            smooth: true,
            lineStyle: {
                color: '#fff',
                width: 1,
            },
            itemStyle: {
                color: '#fff',
            },
            areaStyle: {
                color: 'rgba(255,255,255,0.1)'
            },
            label: {
                color: '#fff',
            },
            connectNulls: true,
        },{
            name: 'PM10',
            data: pm10data,
            type: 'line',
            smooth: true,
            lineStyle: {
                color: '#f7b500',
                width: 1,
            },
            areaStyle: {
                color: 'rgba(247,181,0,0.1)'
            },
            itemStyle: {
                color: '#f7b500',
            },
            label: {
                color: '#f7b500',
            },
            connectNulls: true,
        }]
    };
    return option;
}

function getWeatherIcon(weather, currentTime) {
    var isNight = true;
    if (currentTime.hours() > 5 && currentTime.hours() < 18) {
        isNight = false;
    }

    var weatherIconMap = {
        day: {
            "晴": "qing", "阴": "yin", "多云": "duoyun", "雨夹雪": "yujiaxue", "小雨": "xiaoyu", "中雨": "zhongyu ", 
            "阵雨": "leizhenyu", "小雪": "xiaoxue", "中雪": "zhongxue", "大雪": "daxue", "大雨": "dayu", "雾": "wumai",
            "暴雨": "dayu", "雷阵雨": "leizhenyu", "阵雪": "xiaoxue", "暴雪": "daxue", "扬沙": "shachenbao", "大暴雨": "dayu",
            "霾": "雾霾", "浮尘": "shachenbao", "晴转多云": "duoyunzhuanqing", "小雪转晴": "xiaoxue", "多云转晴": "duoyunzhuanqing",
            "多云转阴": "duoyun", "晴转阴": "qing", "阴转多云": "yin", "多云转小雪": "duoyun", "阵雪转晴": "xiaoxue",
            "晴转阵雪": "qing", "小雪转多云": "xiaoxue", "小雨转多云": "xiaoyu", "晴转小雪": "qing", "多云转雨夹雪": "duoyun",
            "多云转阵雪": "duoyun", "阵雨转多云": "leizhenyu", "多云转小雨": "duoyun", "多云转阵雨": "duoyun", "阵雪转小雪": "xiaoxue",
            "阴转小雪": "yin", "小雪转阴": "xiaoxue", "阵雪转多云": "xiaoxue", "阴转晴": "yin", "阴转阵雪": "yin", "阵雪转阴": "xiaoxue",
            "扬沙转多云": "shachenbao", "扬沙转晴": "shachenbao", "浮尘转晴": "shachenbao", "晴转雨夹雪": "qing", "多云转中雪": "duoyun",
            "晴转中雪": "qing", "阴转小雨": "yin", "小雨转中雨": "xiaoyu", "小雨转阴": "xiaoyu", "中雨转多云": "zhongyu",
            "中雨转小雨": "zhongyu", "阴转中雨": "yin", "多云转中雨": "duoyun", "小雨转大雨": "xiaoyu", "阵雨转中雨": "leizhenyu",
            "阵雨转大雨": "leizhenyu", "阴转大雨": "yin", "雾转多云": "wumai", "阵雨转小雨": "leizhenyu", "中雨转阴": "zhongyu",
            "晴转小雨": "qing", "多云转大雨": "duoyun", "小雨转暴雨": "xiaoyu", "阵雨转晴": "leizhenyuzhuanqing", "小雨转晴": "xiaoyu",
            "阵雨转中到大雨": "leizhenyu", "小雨转阵雨": "xiaoyu", "阵雨转阴": "leizhenyu", "雨夹雪转晴": "yujiaxue", "雨夹雪转多云": "yujiaxue",
            "小雨转小雪": "xiaoyu", "小雪转雨夹雪": "xiaoxue", "阴转阵雨": "yin", "小雨转小到中雨": "xiaoyu", "小到中雨转小雨": "xiaoyu",
            "小到中雨转阴": "xiaoyu", "晴转阵雨": "qing", "中雨转阵雨": "zhongyu", "阵雨转雷阵雨": "leizhenyu", "多云转大雪": "duoyun",
            "阴转中雪": "yin", "阴转大雪": "yin", "雨夹雪转阴": "yujiaxue", "雨夹雪转小雪": "yujiaxue", "小雨转大雪": "xiaoyu",
            "雨夹雪转大雪": "yujiaxue", "雨夹雪转中雪": "yujiaxue", "中雨转小雪": "zhongyu", "中雨转中雪": "zhongyu", "晴转大雪": "qing",
            "小雨转雨夹雪": "xiaoyu", "阴转雨夹雪": "yin", "多云转雾": "duoyun", "小雪转阵雪": "xiaoxue", "小雪转中雪": "xiaoxue",
            "多云转小到中雪": "duoyun", "中雪转多云": "zhongxue", "中雪转小雪": "zhongxue", "大雪转小雪": "daxue", "中雨转大雨": "zhonguu",
            "阵雨转雨夹雪": "leizhenyu", "多云转小到中雨": "duoyun", "小到中雨": "xiaoyu", "小到中雨转阵雨": "xiaoyu", "小雨转阵雪": "xiaoyu",
            "雷阵雨转多云": "leizhenyu", "雷阵雨转阵雨": "leizhenyu", "多云转扬沙": "duoyun", "晴转扬沙": "qing", "扬沙转阴": "shachenbao",
            "浮尘转霾": "shachenbao", "晴转霾": "qing", "霾转阴": "wumai", "霾转多云": "wumai", "霾转晴": "wumai", "小到中雪转多云": "xiaoxue",
            "大雪转多云": "daxue", "雨夹雪转小雨": "yujiaxue", "大雨转阴": "dayu", "浮尘转多云": "shachenbao", "多云转霾": "duoyun",
            "晴转雾": "qing", "小雨转中雪": "xiaoyu", "阵雨转小雪": "leizhenyu", "晴转雷阵雨": "leizhenyuzhuanqing","阴转雾": "yin"
        },
        night: {
            "晴": "yewan", "阴": "yin", "多云": "yewanduoyun", "雨夹雪": "yujiaxue", "小雨": "xiaoyu", "中雨": "zhongyu ", 
            "阵雨": "leizhenyu", "小雪": "xiaoxue", "中雪": "zhongxue", "大雪": "daxue", "大雨": "dayu", "雾": "wumai",
            "暴雨": "dayu", "雷阵雨": "leizhenyu", "阵雪": "xiaoxue", "暴雪": "daxue", "扬沙": "shachenbao", "大暴雨": "dayu",
            "霾": "雾霾", "浮尘": "shachenbao", "晴转多云": "duoyunzhuanqing", "小雪转晴": "xiaoxue", "多云转晴": "duoyunzhuanqing",
            "多云转阴": "yewanduoyun", "晴转阴": "yewan", "阴转多云": "yin", "多云转小雪": "yewanduoyun", "阵雪转晴": "xiaoxue",
            "晴转阵雪": "yewan", "小雪转多云": "xiaoxue", "小雨转多云": "xiaoyu", "晴转小雪": "yewan", "多云转雨夹雪": "yewanduoyun",
            "多云转阵雪": "yewanduoyun", "阵雨转多云": "leizhenyu", "多云转小雨": "yewanduoyun", "多云转阵雨": "yewanduoyun", "阵雪转小雪": "xiaoxue",
            "阴转小雪": "yin", "小雪转阴": "xiaoxue", "阵雪转多云": "xiaoxue", "阴转晴": "yin", "阴转阵雪": "yin", "阵雪转阴": "xiaoxue",
            "扬沙转多云": "shachenbao", "扬沙转晴": "shachenbao", "浮尘转晴": "shachenbao", "晴转雨夹雪": "yewan", "多云转中雪": "yewanduoyun",
            "晴转中雪": "yewan", "阴转小雨": "yin", "小雨转中雨": "xiaoyu", "小雨转阴": "xiaoyu", "中雨转多云": "zhongyu",
            "中雨转小雨": "zhongyu", "阴转中雨": "yin", "多云转中雨": "yewanduoyun", "小雨转大雨": "xiaoyu", "阵雨转中雨": "leizhenyu",
            "阵雨转大雨": "leizhenyu", "阴转大雨": "yin", "雾转多云": "wumai", "阵雨转小雨": "leizhenyu", "中雨转阴": "zhongyu",
            "晴转小雨": "yewan", "多云转大雨": "yewanduoyun", "小雨转暴雨": "xiaoyu", "阵雨转晴": "leizhenyuzhuanqing", "小雨转晴": "xiaoyu",
            "阵雨转中到大雨": "leizhenyu", "小雨转阵雨": "xiaoyu", "阵雨转阴": "leizhenyu", "雨夹雪转晴": "yujiaxue", "雨夹雪转多云": "yujiaxue",
            "小雨转小雪": "xiaoyu", "小雪转雨夹雪": "xiaoxue", "阴转阵雨": "yin", "小雨转小到中雨": "xiaoyu", "小到中雨转小雨": "xiaoyu",
            "小到中雨转阴": "xiaoyu", "晴转阵雨": "yewan", "中雨转阵雨": "zhongyu", "阵雨转雷阵雨": "leizhenyu", "多云转大雪": "yewanduoyun",
            "阴转中雪": "yin", "阴转大雪": "yin", "雨夹雪转阴": "yujiaxue", "雨夹雪转小雪": "yujiaxue", "小雨转大雪": "xiaoyu",
            "雨夹雪转大雪": "yujiaxue", "雨夹雪转中雪": "yujiaxue", "中雨转小雪": "zhongyu", "中雨转中雪": "zhongyu", "晴转大雪": "yewan",
            "小雨转雨夹雪": "xiaoyu", "阴转雨夹雪": "yin", "多云转雾": "yewanduoyun", "小雪转阵雪": "xiaoxue", "小雪转中雪": "xiaoxue",
            "多云转小到中雪": "yewanduoyun", "中雪转多云": "zhongxue", "中雪转小雪": "zhongxue", "大雪转小雪": "daxue", "中雨转大雨": "zhonguu",
            "阵雨转雨夹雪": "leizhenyu", "多云转小到中雨": "yewanduoyun", "小到中雨": "xiaoyu", "小到中雨转阵雨": "xiaoyu", "小雨转阵雪": "xiaoyu",
            "雷阵雨转多云": "leizhenyu", "雷阵雨转阵雨": "leizhenyu", "多云转扬沙": "yewanduoyun", "晴转扬沙": "yewan", "扬沙转阴": "shachenbao",
            "浮尘转霾": "shachenbao", "晴转霾": "yewan", "霾转阴": "wumai", "霾转多云": "wumai", "霾转晴": "wumai", "小到中雪转多云": "xiaoxue",
            "大雪转多云": "daxue", "雨夹雪转小雨": "yujiaxue", "大雨转阴": "dayu", "浮尘转多云": "shachenbao", "多云转霾": "yewanduoyun",
            "晴转雾": "yewan", "小雨转中雪": "xiaoyu", "阵雨转小雪": "leizhenyu", "晴转雷阵雨": "leizhenyuzhuanqing","阴转雾": "yin"
        },
    };
    if(!weather) {
    	return weatherIconMap[isNight ? 'night' : 'day']['晴']
	}
    var weatherIcon = weatherIconMap[isNight ? 'night' : 'day'][weather];
    if (!weatherIcon) {
        if (weather.indexOf('转') > -1) {
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day'][weather.split('转')[0]]
        } else if (weather.indexOf('阴') > -1) {
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day']['阴']
        } else if (weather.indexOf('晴') > -1) {
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day']['晴']
        } else if (weather.indexOf('多云') > -1){
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day']['多云']
        } else if (weather.indexOf('雪') > -1){
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day']['小雪']
        } else if (weather.indexOf('霾') > -1){
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day']['雾霾']
        } else {
            weatherIcon = weatherIconMap[isNight ? 'night' : 'day']['晴']
        }
    }

    return weatherIcon;
}

function getIsoWeekDay(date) {
    var weekDays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'];
    return weekDays[date.isoWeekday() - 1];
}

function getCitiesInfo() {
    var url = URL.GET_CITIES;
    $http.get(url, null, false, function(res) {
        if (res && res.code === 'SUCCESS' && res.data) {
            globalStore.cities = res.data.cities;
        }
    });
}

function buildUpdageAgoContent(minutes) {
    if (typeof minutes === 'undefined' || minutes === null) {
        return null;
    }
    if (minutes < 60) {
        return numeral(minutes).format('0') + '分钟前更新';
    } else {
        return numeral(minutes / 60).format('0') + '小时前更新';
    }
}

function getWeatherInfo() {
    var url = URL.GET_WEATHER_INFO + '?cityName=' + encodeURIComponent(globalStore.address.city);
    $http.get(url, null, false, function(res) {
        if (res && res.code === 'SUCCESS' && res.data) {
            var resData = res.data[globalStore.address.city];
            var nowTime = moment();
            if (resData && resData.weather && JSON.stringify(resData.weather) !== "{}") {
                nowTime =  moment(resData.weather['current_time']);
                globalStore.weatherInfo = {
                    temperatureRange: numeral(resData.weather['temperature_lowest']).format('0') + '~' + numeral(resData.weather['temperature_highest']).format('0') + '℃',
                    temperatureAverage: numeral(resData.weather['temperature_average']).format('0') + '℃',
                    updatedAgo: buildUpdageAgoContent(resData.weather['updated_at_minutes_ago']),
                    humidity: numeral(resData.weather['humidity']).format('0') + '%',
                    dayOfWeek: resData.weather['week'] || getIsoWeekDay(nowTime),
                    weather: resData.weather['weather_condition'],
                    weatherIcon: getWeatherIcon(resData.weather['weather_condition'], nowTime),
                    today: nowTime.format('M月D日'),
                };
            } else {
                globalStore.weatherInfo = {
                    temperatureRange: '',
                    temperatureAverage: '',
                    updatedAgo: null,
                    humidity: '',
                    dayOfWeek: getIsoWeekDay(nowTime),
                    weather: '',
                    weatherIcon: '',
                    today: nowTime.format('M月D日'),
                }
            }
            if (resData.pm && JSON.stringify(resData.pm) !== "{}" && resData.pm.pm_avg_today) {
                globalStore.pmInfo = {
                    avg: {
                        pm25: numeral(resData.pm.pm_avg_today['pm2.5']).format('0'),
                        pm10: numeral(resData.pm.pm_avg_today['pm10']).format('0'),
                    },
                    data: buildPmListData(resData.pm, nowTime),
                };
            } else {
                globalStore.pmInfo = {
                    avg: {
                        pm10: '',
                        pm25: ''
                    },
                    data: [],
                };
            }
        }
    });

}

function buildPmListData(data, nowTime) {
    var pmList = [];
    for (var i = 0; i < 24; i++) {
        var pmItem = {
            datetime: nowTime.subtract(1, 'hours').format('YYYY-MM-DD HH:00:00'),
            pm10: null,
            pm25: null,
        }
        pmItem.ts = moment(pmItem.datetime).unix(),
        pmItem.hour = moment(pmItem.datetime).format('H:00');
        var k = moment(pmItem.datetime).format('YYYY-MM-DD HH:mm:ss');
        if (data[k]) {
            pmItem.pm10 = numeral(data[k].pm10).format('0');
            pmItem.pm25 = numeral(data[k]['pm2.5']).format('0');
        }
        pmList.push(pmItem);
    }
    // $.each(data, function(k) {
    //     if (k !== 'pm_avg_today') {
    //         pmList.push({
    //             datetime: k,
    //             ts: moment(k).unix(),
    //             pm10: numeral(data[k].pm10).format('0'),
    //             pm25: numeral(data[k].pm25).format('0'),
    //         });
    //     }
    // });
    pmList = pmList.sort((a, b) => {
        return a.ts - b.ts;
    });
    return pmList;
}

function getRiskInfo() {
    var url = URL.GET_RISK_INFO + '?cityName=' + encodeURIComponent(globalStore.address.city) + '&isFever=' + (globalStore.isFever ? '1' : '0');
    $http.get(url, null, false, function(res) {
        if (res && res.code === 'SUCCESS' && res.data) {
            globalStore.riskInfo = {
                pm25ProbVal: numeral(res.data.PM25_prob * 100).format('0'),
                pm25ProbContent: numeral(res.data.PM25_prob).format('0%'),
                pm25Comment: res.data.PM25_comment,
                pm10ProbVal: numeral(res.data.PM10_prob * 100).format('0'),
                pm10ProbContent: numeral(res.data.PM10_prob).format('0%'),
                pm10Comment: res.data.PM10_comment,
            };
        } else {
            globalStore.riskInfo = {
                pm25ProbVal: 0,
                pm25ProbContent: '0%',
                pm25Comment: '',
                pm10ProbVal: 0,
                pm10ProbContent: '0%',
                pm10Comment: '',
            };
        }
    });
}

var healthy_travel = {
	title: '出行风险提醒',
	name: 'healthy_travel',
	url: '#healthy_travel',
	render: function () {

        // init globalStore
        var nowTime = moment();
        globalStore.address = config.defaultCity;
        globalStore.isFever = true;
        globalStore.weatherInfo = {
            temperatureRange: '',
            temperatureAverage: '',
            updatedAgo: null,
            humidity: '',
            dayOfWeek: getIsoWeekDay(moment()),
            weather: '',
            weatherIcon: '',
            today: nowTime.format('M月D日'),
        };
        globalStore.pmInfo = {
            avg: {
                pm10: '',
                pm25: ''
            },
            data: [],
        };
        globalStore.riskInfo = {
            pm25ProbVal: 0,
            pm25ProbContent: '0%',
            pm25Comment: '',
            pm10ProbVal: 0,
            pm10ProbContent: '0%',
            pm10Comment: '',
        };

        getCitiesInfo();
        getWeatherInfo();
        getRiskInfo();
       
		var htmlParams = {
            address: globalStore.address,
            weatherInfo: globalStore.weatherInfo,
            pmInfo: globalStore.pmInfo,
            isFever: globalStore.isFever,
            riskInfo: globalStore.riskInfo,
        };

		$.hideLoading();
		return template('tpl_healthy_travel', htmlParams);
	},
	bind: function () {
        var rateStars = $('#healthy_travel_notice_stars').rateYo({
            starWidth: '25px',
            spacing: '5px',
            normalFill: '#fff',
            ratedFill: '#ffbb00',
            rating: globalStore.riskInfo.pm25ProbVal,
            readOnly: true,
            maxValue: 100,
            starSvg: '<svg width="48px" height="48px" viewBox="0 0 48 48" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Page-1" stroke="none" stroke-width="1" fill-rule="evenodd"><g id="jkcx4-copy" transform="translate(-77.000000, -1001.000000)"><path d="M100.547809,1039.47063 L90.3708046,1044.821 C89.3931155,1045.335 88.1838612,1044.95911 87.6698595,1043.98142 C87.4651814,1043.5921 87.3945521,1043.14616 87.4689057,1042.71265 L89.4125407,1031.38039 C89.5238166,1030.7316 89.3087196,1030.0696 88.8373474,1029.61012 L80.6039776,1021.58457 C79.8130105,1020.81357 79.7968259,1019.54734 80.5678283,1018.75637 C80.8748455,1018.44141 81.2771303,1018.23643 81.7124044,1018.17318 L93.0906416,1016.51983 C93.7420619,1016.42517 94.3051931,1016.01603 94.5965171,1015.42575 L99.6850195,1005.11531 C100.173864,1004.12481 101.373116,1003.71813 102.363623,1004.20697 C102.758048,1004.40163 103.077303,1004.72089 103.271964,1005.11531 L108.360466,1015.42575 C108.65179,1016.01603 109.214921,1016.42517 109.866342,1016.51983 L121.244579,1018.17318 C122.337669,1018.33202 123.095032,1019.3469 122.936196,1020.43999 C122.872947,1020.87527 122.667973,1021.27755 122.353006,1021.58457 L114.119636,1029.61012 C113.648264,1030.0696 113.433167,1030.7316 113.544443,1031.38039 L115.488078,1042.71265 C115.6748,1043.80132 114.943624,1044.83523 113.854951,1045.02195 C113.421436,1045.09631 112.9755,1045.02568 112.586179,1044.821 L102.409174,1039.47063 C101.826526,1039.16432 101.130457,1039.16432 100.547809,1039.47063 Z" id="风险指数"></path></g></g></svg>'
        });

        
        var lineChart = echarts.init(document.getElementById('healthy_travel_pm_line_chart'), 'pm', {
            renderer: 'svg',
        });
        lineChart.setOption(getOption());

        function renderWeatherInfo() {
            $('#healthy_travel_today').html(globalStore.weatherInfo.today);
            $('#healthy_travel_week').html(globalStore.weatherInfo.dayOfWeek);
            $('#healthy_travel_weather_update').html(globalStore.weatherInfo.updatedAgo);
            $('#healthy_travel_weather_img').html('<i class="pmicon pmicon-'+ globalStore.weatherInfo.weatherIcon +'">');
            $('#healthy_travel_weather').html(globalStore.weatherInfo.weather);
            $('#healthy_travel_temperature_range').html(globalStore.weatherInfo.temperatureRange);
            $('#healthy_travel_temperature').html(globalStore.weatherInfo.temperatureAverage);
            $('#healthy_travel_humidity').html(globalStore.weatherInfo.humidity);
            $('#healthy_travel_pm25').html(globalStore.pmInfo.avg.pm25);
            $('#healthy_travel_pm10').html(globalStore.pmInfo.avg.pm10);
            lineChart.setOption(getOption());
        }

        function renderRiskInfo() {
            rateStars.rateYo('rating', globalStore.riskInfo.pm25ProbVal);
            $('#healthy_travel_notice_per').html(globalStore.riskInfo.pm25ProbContent);
            $('#healthy_travel_notice_content').html(globalStore.riskInfo.pm25Comment);
        }

        $('.healthy_travel_address_content').cityPicker({
            title: "请选择城市",
            showDistrict: false,
            rawData: globalStore.cities,
            value: globalStore.address.province + ' ' + globalStore.address.city,
            // onChange: (e, vals, displayVals) => {
            //     console.log('val', displayVals);
            // },
            onClose: (e) => {
                globalStore.address =  {
                    province: e.value[0],
                    city: e.value[1]
                };
                $('span.healthy_travel_address_content').html(e.value[1]);
                $.showLoading();
                getWeatherInfo();
                getRiskInfo();
                renderWeatherInfo();
                renderRiskInfo();
                $.hideLoading();
            }
        });

        $('#healthy_travel_is_fever').off('click').on('click', function() {
            globalStore.isFever = !globalStore.isFever;
            $.showLoading();
            getRiskInfo();
            renderRiskInfo();
            $.hideLoading();
        });
	},
};

