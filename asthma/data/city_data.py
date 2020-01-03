# 同时支持Weather/PM 第三方API的城市
import json

cities = [
    {
        "city_code": "101010100",
        "name_en": "beijing",
        "name_zh": "北京",
        "province_en": "beijing",
        "province_zh": "北京",
        "latitude": "39.904989",
        "longitude": "116.405285"
    },
    {
        "city_code": "101020100",
        "name_en": "shanghai",
        "name_zh": "上海",
        "province_en": "shanghai",
        "province_zh": "上海",
        "latitude": "31.231706",
        "longitude": "121.472644"
    },
    {
        "city_code": "101030100",
        "name_en": "tianjin",
        "name_zh": "天津",
        "province_en": "tianjin",
        "province_zh": "天津",
        "latitude": "39.125596",
        "longitude": "117.190182"
    },
    {
        "city_code": "101040100",
        "name_en": "chongqing",
        "name_zh": "重庆",
        "province_en": "chongqing",
        "province_zh": "重庆",
        "latitude": "29.291965",
        "longitude": "108.170255"
    },
    {
        "city_code": "101050101",
        "name_en": "haerbin",
        "name_zh": "哈尔滨",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "45.756967",
        "longitude": "126.642464"
    },
    {
        "city_code": "101050201",
        "name_en": "qiqihaer",
        "name_zh": "齐齐哈尔",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "47.342081",
        "longitude": "123.95792"
    },
    {
        "city_code": "101050301",
        "name_en": "mudanjiang",
        "name_zh": "牡丹江",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "44.582962",
        "longitude": "129.618602"
    },
    {
        "city_code": "101050401",
        "name_en": "jiamusi",
        "name_zh": "佳木斯",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "46.809606",
        "longitude": "130.361634"
    },
    {
        "city_code": "101050501",
        "name_en": "suihua",
        "name_zh": "绥化",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "46.637393",
        "longitude": "126.99293"
    },
    {
        "city_code": "101050601",
        "name_en": "heihe",
        "name_zh": "黑河",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "50.249585",
        "longitude": "127.499023"
    },
    {
        "city_code": "101050801",
        "name_en": "yichun",
        "name_zh": "伊春",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "47.726851",
        "longitude": "128.899284"
    },
    {
        "city_code": "101050901",
        "name_en": "daqing",
        "name_zh": "大庆",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "46.590734",
        "longitude": "125.11272"
    },
    {
        "city_code": "101051101",
        "name_en": "jixi",
        "name_zh": "鸡西",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "45.300046",
        "longitude": "130.975966"
    },
    {
        "city_code": "101051201",
        "name_en": "hegang",
        "name_zh": "鹤岗",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "47.332085",
        "longitude": "130.277487"
    },
    {
        "city_code": "101051301",
        "name_en": "shuangyashan",
        "name_zh": "双鸭山",
        "province_en": "heilongjiang",
        "province_zh": "黑龙江省",
        "latitude": "46.643442",
        "longitude": "131.157304"
    },
    {
        "city_code": "101060101",
        "name_en": "changchun",
        "name_zh": "长春",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "43.886841",
        "longitude": "125.3245"
    },
    {
        "city_code": "101060201",
        "name_en": "jilin",
        "name_zh": "吉林",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "43.843577",
        "longitude": "126.55302"
    },
    {
        "city_code": "101060306",
        "name_en": "yanbian",
        "name_zh": "延边",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "42.904823",
        "longitude": "129.513228"
    },
    {
        "city_code": "101060401",
        "name_en": "siping",
        "name_zh": "四平",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "43.170344",
        "longitude": "124.370785"
    },
    {
        "city_code": "101060601",
        "name_en": "baicheng",
        "name_zh": "白城",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "45.619026",
        "longitude": "122.841114"
    },
    {
        "city_code": "101060701",
        "name_en": "liaoyuan",
        "name_zh": "辽源",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "42.902692",
        "longitude": "125.145349"
    },
    {
        "city_code": "101060901",
        "name_en": "baishan",
        "name_zh": "白山",
        "province_en": "jilin",
        "province_zh": "吉林省",
        "latitude": "41.942505",
        "longitude": "126.427839"
    },
    {
        "city_code": "101070101",
        "name_en": "shenyang",
        "name_zh": "沈阳",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.796767",
        "longitude": "123.429096"
    },
    {
        "city_code": "101070201",
        "name_en": "dalian",
        "name_zh": "大连",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "38.91459",
        "longitude": "121.618622"
    },
    {
        "city_code": "101070301",
        "name_en": "anshan",
        "name_zh": "鞍山",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.110626",
        "longitude": "122.995632"
    },
    {
        "city_code": "101070401",
        "name_en": "fushun",
        "name_zh": "抚顺",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.922644",
        "longitude": "124.097979"
    },
    {
        "city_code": "101070501",
        "name_en": "benxi",
        "name_zh": "本溪",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.297909",
        "longitude": "123.770519"
    },
    {
        "city_code": "101070601",
        "name_en": "dandong",
        "name_zh": "丹东",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "40.124296",
        "longitude": "124.383044"
    },
    {
        "city_code": "101070701",
        "name_en": "jinzhou",
        "name_zh": "锦州",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.119269",
        "longitude": "121.135742"
    },
    {
        "city_code": "101070801",
        "name_en": "yingkou",
        "name_zh": "营口",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "40.667432",
        "longitude": "122.235151"
    },
    {
        "city_code": "101070901",
        "name_en": "fuxin",
        "name_zh": "阜新",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "42.058607",
        "longitude": "121.743125"
    },
    {
        "city_code": "101071001",
        "name_en": "liaoyang",
        "name_zh": "辽阳",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.269402",
        "longitude": "123.18152"
    },
    {
        "city_code": "101071101",
        "name_en": "tieling",
        "name_zh": "铁岭",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "42.223316",
        "longitude": "123.725669"
    },
    {
        "city_code": "101071201",
        "name_en": "chaoyang",
        "name_zh": "朝阳",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.576758",
        "longitude": "120.451176"
    },
    {
        "city_code": "101071301",
        "name_en": "panjin",
        "name_zh": "盘锦",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "41.124484",
        "longitude": "122.06957"
    },
    {
        "city_code": "101071401",
        "name_en": "huludao",
        "name_zh": "葫芦岛",
        "province_en": "liaoning",
        "province_zh": "辽宁省",
        "latitude": "40.755572",
        "longitude": "120.856394"
    },
    {
        "city_code": "101080101",
        "name_en": "huhehaote",
        "name_zh": "呼和浩特",
        "province_en": "neimenggu",
        "province_zh": "内蒙古自治区",
        "latitude": "40.818311",
        "longitude": "111.670801"
    },
    {
        "city_code": "101080201",
        "name_en": "baotou",
        "name_zh": "包头",
        "province_en": "neimenggu",
        "province_zh": "内蒙古自治区",
        "latitude": "40.658168",
        "longitude": "109.840405"
    },
    {
        "city_code": "101080301",
        "name_en": "wuhai",
        "name_zh": "乌海",
        "province_en": "neimenggu",
        "province_zh": "内蒙古自治区",
        "latitude": "39.673734",
        "longitude": "106.825563"
    },
    {
        "city_code": "101080501",
        "name_en": "tongliao",
        "name_zh": "通辽",
        "province_en": "neimenggu",
        "province_zh": "内蒙古自治区",
        "latitude": "43.617429",
        "longitude": "122.263119"
    },
    {
        "city_code": "101080601",
        "name_en": "chifeng",
        "name_zh": "赤峰",
        "province_en": "neimenggu",
        "province_zh": "内蒙古自治区",
        "latitude": "42.275317",
        "longitude": "118.956806"
    },
    {
        "city_code": "101080701",
        "name_en": "eerduosi",
        "name_zh": "鄂尔多斯",
        "province_en": "neimenggu",
        "province_zh": "内蒙古自治区",
        "latitude": "39.817179",
        "longitude": "109.99029"
    },
    {
        "city_code": "101090101",
        "name_en": "shijiazhuang",
        "name_zh": "石家庄",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "38.045474",
        "longitude": "114.502461"
    },
    {
        "city_code": "101090201",
        "name_en": "baoding",
        "name_zh": "保定",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "38.867657",
        "longitude": "115.482331"
    },
    {
        "city_code": "101090301",
        "name_en": "zhangjiakou",
        "name_zh": "张家口",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "40.811901",
        "longitude": "114.884091"
    },
    {
        "city_code": "101090402",
        "name_en": "chengde",
        "name_zh": "承德",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "40.976204",
        "longitude": "117.939152"
    },
    {
        "city_code": "101090501",
        "name_en": "tangshan",
        "name_zh": "唐山",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "39.635113",
        "longitude": "118.175393"
    },
    {
        "city_code": "101090601",
        "name_en": "langfang",
        "name_zh": "廊坊",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "39.523927",
        "longitude": "116.704441"
    },
    {
        "city_code": "101090701",
        "name_en": "cangzhou",
        "name_zh": "沧州",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "38.310582",
        "longitude": "116.857461"
    },
    {
        "city_code": "101090801",
        "name_en": "hengshui",
        "name_zh": "衡水",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "37.735097",
        "longitude": "115.665993"
    },
    {
        "city_code": "101090901",
        "name_en": "xingtai",
        "name_zh": "邢台",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "37.05073",
        "longitude": "114.561132"
    },
    {
        "city_code": "101091001",
        "name_en": "handan",
        "name_zh": "邯郸",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "36.612273",
        "longitude": "114.490686"
    },
    {
        "city_code": "101091101",
        "name_en": "qinhuangdao",
        "name_zh": "秦皇岛",
        "province_en": "hebei",
        "province_zh": "河北省",
        "latitude": "39.942531",
        "longitude": "119.586579"
    },
    {
        "city_code": "101100101",
        "name_en": "taiyuan",
        "name_zh": "太原",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "37.857014",
        "longitude": "112.549248"
    },
    {
        "city_code": "101100201",
        "name_en": "datong",
        "name_zh": "大同",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "40.090511",
        "longitude": "113.301438"
    },
    {
        "city_code": "101100301",
        "name_en": "yangquan",
        "name_zh": "阳泉",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "37.861188",
        "longitude": "113.583285"
    },
    {
        "city_code": "101100401",
        "name_en": "jinzhong",
        "name_zh": "晋中",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "37.696495",
        "longitude": "112.736465"
    },
    {
        "city_code": "101100501",
        "name_en": "changzhi",
        "name_zh": "长治",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "36.191112",
        "longitude": "113.113556"
    },
    {
        "city_code": "101100601",
        "name_en": "jincheng",
        "name_zh": "晋城",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "35.497553",
        "longitude": "112.851274"
    },
    {
        "city_code": "101100701",
        "name_en": "linfen",
        "name_zh": "临汾",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "36.08415",
        "longitude": "111.517973"
    },
    {
        "city_code": "101100801",
        "name_en": "yuncheng",
        "name_zh": "运城",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "35.022778",
        "longitude": "111.003957"
    },
    {
        "city_code": "101100901",
        "name_en": "shuozhou",
        "name_zh": "朔州",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "39.331261",
        "longitude": "112.433387"
    },
    {
        "city_code": "101101001",
        "name_en": "xinzhou",
        "name_zh": "忻州",
        "province_en": "shanxi",
        "province_zh": "山西省",
        "latitude": "38.41769",
        "longitude": "112.733538"
    },
    {
        "city_code": "101110101",
        "name_en": "xian",
        "name_zh": "西安",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "34.263161",
        "longitude": "108.948024"
    },
    {
        "city_code": "101110200",
        "name_en": "xianyang",
        "name_zh": "咸阳",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "34.333439",
        "longitude": "108.705117"
    },
    {
        "city_code": "101110300",
        "name_en": "yanan",
        "name_zh": "延安",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "36.596537",
        "longitude": "109.49081"
    },
    {
        "city_code": "101110401",
        "name_en": "yulin",
        "name_zh": "榆林",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "38.290162",
        "longitude": "109.741193"
    },
    {
        "city_code": "101110501",
        "name_en": "weinan",
        "name_zh": "渭南",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "34.499381",
        "longitude": "109.502882"
    },
    {
        "city_code": "101110701",
        "name_en": "ankang",
        "name_zh": "安康",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "32.6903",
        "longitude": "109.029273"
    },
    {
        "city_code": "101110801",
        "name_en": "hanzhong",
        "name_zh": "汉中",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "33.077668",
        "longitude": "107.028621"
    },
    {
        "city_code": "101110901",
        "name_en": "baoji",
        "name_zh": "宝鸡",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "34.369315",
        "longitude": "107.14487"
    },
    {
        "city_code": "101111001",
        "name_en": "tongchuan",
        "name_zh": "铜川",
        "province_en": "shan-xi",
        "province_zh": "陕西省",
        "latitude": "34.916582",
        "longitude": "108.979608"
    },
    {
        "city_code": "101120101",
        "name_en": "jinan",
        "name_zh": "济南",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.675807",
        "longitude": "117.000923"
    },
    {
        "city_code": "101120201",
        "name_en": "qingdao",
        "name_zh": "青岛",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.082982",
        "longitude": "120.355173"
    },
    {
        "city_code": "101120301",
        "name_en": "zibo",
        "name_zh": "淄博",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.814939",
        "longitude": "118.047648"
    },
    {
        "city_code": "101120401",
        "name_en": "dezhou",
        "name_zh": "德州",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "37.453968",
        "longitude": "116.307428"
    },
    {
        "city_code": "101120501",
        "name_en": "yantai",
        "name_zh": "烟台",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "37.539297",
        "longitude": "121.391382"
    },
    {
        "city_code": "101120601",
        "name_en": "weifang",
        "name_zh": "潍坊",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.70925",
        "longitude": "119.107078"
    },
    {
        "city_code": "101120701",
        "name_en": "jining",
        "name_zh": "济宁",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "35.415393",
        "longitude": "116.587245"
    },
    {
        "city_code": "101120801",
        "name_en": "taian",
        "name_zh": "泰安",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.194968",
        "longitude": "117.129063"
    },
    {
        "city_code": "101120901",
        "name_en": "linyi",
        "name_zh": "临沂",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "35.065282",
        "longitude": "118.326443"
    },
    {
        "city_code": "101121001",
        "name_en": "heze",
        "name_zh": "菏泽",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "35.246531",
        "longitude": "115.469381"
    },
    {
        "city_code": "101121101",
        "name_en": "binzhou",
        "name_zh": "滨州",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "37.383542",
        "longitude": "118.016974"
    },
    {
        "city_code": "101121201",
        "name_en": "dongying",
        "name_zh": "东营",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "37.461567",
        "longitude": "118.507543"
    },
    {
        "city_code": "101121301",
        "name_en": "weihai",
        "name_zh": "威海",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "37.509691",
        "longitude": "122.116394"
    },
    {
        "city_code": "101121401",
        "name_en": "zaozhuang",
        "name_zh": "枣庄",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "34.856424",
        "longitude": "117.557964"
    },
    {
        "city_code": "101121501",
        "name_en": "rizhao",
        "name_zh": "日照",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "35.428588",
        "longitude": "119.461208"
    },
    {
        "city_code": "101121601",
        "name_en": "laiwu",
        "name_zh": "莱芜",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.214397",
        "longitude": "117.677736"
    },
    {
        "city_code": "101121701",
        "name_en": "liaocheng",
        "name_zh": "聊城",
        "province_en": "shandong",
        "province_zh": "山东省",
        "latitude": "36.456013",
        "longitude": "115.980367"
    },
    {
        "city_code": "101130101",
        "name_en": "wulumuqi",
        "name_zh": "乌鲁木齐",
        "province_en": "xinjiang",
        "province_zh": "新疆维吾尔自治区",
        "latitude": "43.792818",
        "longitude": "87.617733"
    },
    {
        "city_code": "101130301",
        "name_en": "shihezi",
        "name_zh": "石河子",
        "province_en": "xinjiang",
        "province_zh": "新疆维吾尔自治区",
        "latitude": "44.305886",
        "longitude": "86.041075"
    },
    {
        "city_code": "101130401",
        "name_en": "changji",
        "name_zh": "昌吉",
        "province_en": "xinjiang",
        "province_zh": "新疆维吾尔自治区",
        "latitude": "44.014577",
        "longitude": "87.304012"
    },
    {
        "city_code": "101130901",
        "name_en": "kashi",
        "name_zh": "喀什",
        "province_en": "xinjiang",
        "province_zh": "新疆维吾尔自治区",
        "latitude": "39.467664",
        "longitude": "75.989138"
    },
    {
        "city_code": "101131012",
        "name_en": "yili",
        "name_zh": "伊犁",
        "province_en": "xinjiang",
        "province_zh": "新疆维吾尔自治区",
        "latitude": "43.92186",
        "longitude": "81.317946"
    },
    {
        "city_code": "101131201",
        "name_en": "hami",
        "name_zh": "哈密",
        "province_en": "xinjiang",
        "province_zh": "新疆维吾尔自治区",
        "latitude": "42.833248",
        "longitude": "93.51316"
    },
    {
        "city_code": "101140201",
        "name_en": "rikaze",
        "name_zh": "日喀则",
        "province_en": "xizang",
        "province_zh": "西藏自治区",
        "latitude": "29.267519",
        "longitude": "88.885148"
    },
    {
        "city_code": "101150101",
        "name_en": "xining",
        "name_zh": "西宁",
        "province_en": "qinghai",
        "province_zh": "青海省",
        "latitude": "36.623178",
        "longitude": "101.778916"
    },
    {
        "city_code": "101160101",
        "name_en": "lanzhou",
        "name_zh": "兰州",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "36.058039",
        "longitude": "103.823557"
    },
    {
        "city_code": "101160301",
        "name_en": "pingliang",
        "name_zh": "平凉",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "35.54279",
        "longitude": "106.684691"
    },
    {
        "city_code": "101160401",
        "name_en": "qingyang",
        "name_zh": "庆阳",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "35.734218",
        "longitude": "107.638372"
    },
    {
        "city_code": "101160501",
        "name_en": "wuwei",
        "name_zh": "武威",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "37.929996",
        "longitude": "102.634697"
    },
    {
        "city_code": "101160601",
        "name_en": "jinchang",
        "name_zh": "金昌",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "38.514238",
        "longitude": "102.187888"
    },
    {
        "city_code": "101160701",
        "name_en": "zhangye",
        "name_zh": "张掖",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "38.932897",
        "longitude": "100.455472"
    },
    {
        "city_code": "101160801",
        "name_en": "jiuquan",
        "name_zh": "酒泉",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "39.744023",
        "longitude": "98.510795"
    },
    {
        "city_code": "101160901",
        "name_en": "tianshui",
        "name_zh": "天水",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "34.578529",
        "longitude": "105.724998"
    },
    {
        "city_code": "101161301",
        "name_en": "baiyin",
        "name_zh": "白银",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "36.54568",
        "longitude": "104.173606"
    },
    {
        "city_code": "101161401",
        "name_en": "jiayuguan",
        "name_zh": "嘉峪关",
        "province_en": "gansu",
        "province_zh": "甘肃省",
        "latitude": "39.786529",
        "longitude": "98.277304"
    },
    {
        "city_code": "101170101",
        "name_en": "yinchuan",
        "name_zh": "银川",
        "province_en": "ningxia",
        "province_zh": "宁夏回族自治区",
        "latitude": "38.46637",
        "longitude": "106.278179"
    },
    {
        "city_code": "101170201",
        "name_en": "shizuishan",
        "name_zh": "石嘴山",
        "province_en": "ningxia",
        "province_zh": "宁夏回族自治区",
        "latitude": "39.01333",
        "longitude": "106.376173"
    },
    {
        "city_code": "101180101",
        "name_en": "zhengzhou",
        "name_zh": "郑州",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "34.757975",
        "longitude": "113.665412"
    },
    {
        "city_code": "101180201",
        "name_en": "anyang",
        "name_zh": "安阳",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "36.103442",
        "longitude": "114.352482"
    },
    {
        "city_code": "101180301",
        "name_en": "xinxiang",
        "name_zh": "新乡",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "35.190021",
        "longitude": "113.806186"
    },
    {
        "city_code": "101180401",
        "name_en": "xuchang",
        "name_zh": "许昌",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "34.022956",
        "longitude": "113.826063"
    },
    {
        "city_code": "101180501",
        "name_en": "pingdingshan",
        "name_zh": "平顶山",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "33.735241",
        "longitude": "113.307718"
    },
    {
        "city_code": "101180601",
        "name_en": "xinyang",
        "name_zh": "信阳",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "32.123274",
        "longitude": "114.075031"
    },
    {
        "city_code": "101180701",
        "name_en": "nanyang",
        "name_zh": "南阳",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "32.999082",
        "longitude": "112.540918"
    },
    {
        "city_code": "101180801",
        "name_en": "kaifeng",
        "name_zh": "开封",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "34.797049",
        "longitude": "114.341447"
    },
    {
        "city_code": "101180901",
        "name_en": "luoyang",
        "name_zh": "洛阳",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "34.663041",
        "longitude": "112.434468"
    },
    {
        "city_code": "101181001",
        "name_en": "shangqiu",
        "name_zh": "商丘",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "34.437054",
        "longitude": "115.650497"
    },
    {
        "city_code": "101181101",
        "name_en": "jiaozuo",
        "name_zh": "焦作",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "35.23904",
        "longitude": "113.238266"
    },
    {
        "city_code": "101181201",
        "name_en": "hebi",
        "name_zh": "鹤壁",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "35.748236",
        "longitude": "114.295444"
    },
    {
        "city_code": "101181301",
        "name_en": "puyang",
        "name_zh": "濮阳",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "35.768234",
        "longitude": "115.041299"
    },
    {
        "city_code": "101181401",
        "name_en": "zhoukou",
        "name_zh": "周口",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "33.620357",
        "longitude": "114.649653"
    },
    {
        "city_code": "101181501",
        "name_en": "luohe",
        "name_zh": "漯河",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "33.575855",
        "longitude": "114.026405"
    },
    {
        "city_code": "101181601",
        "name_en": "zhumadian",
        "name_zh": "驻马店",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "32.980169",
        "longitude": "114.024736"
    },
    {
        "city_code": "101181701",
        "name_en": "sanmenxia",
        "name_zh": "三门峡",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "34.777338",
        "longitude": "111.194099"
    },
    {
        "city_code": "101181801",
        "name_en": "jiyuan",
        "name_zh": "济源",
        "province_en": "henan",
        "province_zh": "河南省",
        "latitude": "35.090378",
        "longitude": "112.590047"
    },
    {
        "city_code": "101190101",
        "name_en": "nanjing",
        "name_zh": "南京",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "32.041544",
        "longitude": "118.767413"
    },
    {
        "city_code": "101190201",
        "name_en": "wuxi",
        "name_zh": "无锡",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "31.574729",
        "longitude": "120.301663"
    },
    {
        "city_code": "101190301",
        "name_en": "zhenjiang",
        "name_zh": "镇江",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "32.204402",
        "longitude": "119.452753"
    },
    {
        "city_code": "101190401",
        "name_en": "suzhou",
        "name_zh": "苏州",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "31.299379",
        "longitude": "120.619585"
    },
    {
        "city_code": "101190501",
        "name_en": "nantong",
        "name_zh": "南通",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "32.016212",
        "longitude": "120.864608"
    },
    {
        "city_code": "101190601",
        "name_en": "yangzhou",
        "name_zh": "扬州",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "32.393159",
        "longitude": "119.421003"
    },
    {
        "city_code": "101190701",
        "name_en": "yancheng",
        "name_zh": "盐城",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "33.377631",
        "longitude": "120.139998"
    },
    {
        "city_code": "101190801",
        "name_en": "xuzhou",
        "name_zh": "徐州",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "34.261792",
        "longitude": "117.184811"
    },
    {
        "city_code": "101190901",
        "name_en": "huaian",
        "name_zh": "淮安",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "33.597506",
        "longitude": "119.021265"
    },
    {
        "city_code": "101191001",
        "name_en": "lianyungang",
        "name_zh": "连云港",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "34.600018",
        "longitude": "119.178821"
    },
    {
        "city_code": "101191101",
        "name_en": "changzhou",
        "name_zh": "常州",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "31.772752",
        "longitude": "119.946973"
    },
    {
        "city_code": "101191201",
        "name_en": "taizhou",
        "name_zh": "泰州",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "32.484882",
        "longitude": "119.915176"
    },
    {
        "city_code": "101191301",
        "name_en": "suqian",
        "name_zh": "宿迁",
        "province_en": "jiangsu",
        "province_zh": "江苏省",
        "latitude": "33.963008",
        "longitude": "118.275162"
    },
    {
        "city_code": "101200101",
        "name_en": "wuhan",
        "name_zh": "武汉",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.584355",
        "longitude": "114.298572"
    },
    {
        "city_code": "101200201",
        "name_en": "xiangyang",
        "name_zh": "襄阳",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "32.042426",
        "longitude": "112.144146"
    },
    {
        "city_code": "101200301",
        "name_en": "ezhou",
        "name_zh": "鄂州",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.396536",
        "longitude": "114.890593"
    },
    {
        "city_code": "101200401",
        "name_en": "xiaogan",
        "name_zh": "孝感",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.926423",
        "longitude": "113.926655"
    },
    {
        "city_code": "101200501",
        "name_en": "huanggang",
        "name_zh": "黄冈",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.447711",
        "longitude": "114.879365"
    },
    {
        "city_code": "101200601",
        "name_en": "huangshi",
        "name_zh": "黄石",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.220074",
        "longitude": "115.077048"
    },
    {
        "city_code": "101200701",
        "name_en": "xianning",
        "name_zh": "咸宁",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "29.832798",
        "longitude": "114.328963"
    },
    {
        "city_code": "101200801",
        "name_en": "jingzhou",
        "name_zh": "荆州",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.326857",
        "longitude": "112.23813"
    },
    {
        "city_code": "101200901",
        "name_en": "yichang",
        "name_zh": "宜昌",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.702636",
        "longitude": "111.290843"
    },
    {
        "city_code": "101201001",
        "name_en": "enshi",
        "name_zh": "恩施",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.283114",
        "longitude": "109.48699"
    },
    {
        "city_code": "101201101",
        "name_en": "shiyan",
        "name_zh": "十堰",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "32.646907",
        "longitude": "110.787916"
    },
    {
        "city_code": "101201201",
        "name_en": "shennongjia",
        "name_zh": "神农架",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "31.744449",
        "longitude": "110.671525"
    },
    {
        "city_code": "101201301",
        "name_en": "suizhou",
        "name_zh": "随州",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "31.717497",
        "longitude": "113.37377"
    },
    {
        "city_code": "101201401",
        "name_en": "jingmen",
        "name_zh": "荆门",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "31.03542",
        "longitude": "112.204251"
    },
    {
        "city_code": "101201501",
        "name_en": "tianmen",
        "name_zh": "天门",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.653061",
        "longitude": "113.165862"
    },
    {
        "city_code": "101201601",
        "name_en": "xiantao",
        "name_zh": "仙桃",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.364953",
        "longitude": "113.453974"
    },
    {
        "city_code": "101201701",
        "name_en": "qianjiang",
        "name_zh": "潜江",
        "province_en": "hubei",
        "province_zh": "湖北省",
        "latitude": "30.421215",
        "longitude": "112.896866"
    },
    {
        "city_code": "101210101",
        "name_en": "hangzhou",
        "name_zh": "杭州",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "30.287459",
        "longitude": "120.153576"
    },
    {
        "city_code": "101210201",
        "name_en": "huzhou",
        "name_zh": "湖州",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "30.867198",
        "longitude": "120.102398"
    },
    {
        "city_code": "101210301",
        "name_en": "jiaxing",
        "name_zh": "嘉兴",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "30.762653",
        "longitude": "120.750865"
    },
    {
        "city_code": "101210401",
        "name_en": "ningbo",
        "name_zh": "宁波",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "29.868388",
        "longitude": "121.549792"
    },
    {
        "city_code": "101210507",
        "name_en": "shaoxing",
        "name_zh": "绍兴",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "29.997117",
        "longitude": "120.582112"
    },
    {
        "city_code": "101210601",
        "name_en": "taizhou",
        "name_zh": "台州",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "28.661378",
        "longitude": "121.428599"
    },
    {
        "city_code": "101210701",
        "name_en": "wenzhou",
        "name_zh": "温州",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "28.000575",
        "longitude": "120.672111"
    },
    {
        "city_code": "101210801",
        "name_en": "lishui",
        "name_zh": "丽水",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "28.451993",
        "longitude": "119.921786"
    },
    {
        "city_code": "101210901",
        "name_en": "jinhua",
        "name_zh": "金华",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "29.089524",
        "longitude": "119.649506"
    },
    {
        "city_code": "101211001",
        "name_en": "quzhou",
        "name_zh": "衢州",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "28.941708",
        "longitude": "118.87263"
    },
    {
        "city_code": "101211101",
        "name_en": "zhoushan",
        "name_zh": "舟山",
        "province_en": "zhejiang",
        "province_zh": "浙江省",
        "latitude": "30.016028",
        "longitude": "122.106863"
    },
    {
        "city_code": "101220101",
        "name_en": "hefei",
        "name_zh": "合肥",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "31.86119",
        "longitude": "117.283042"
    },
    {
        "city_code": "101220201",
        "name_en": "bengbu",
        "name_zh": "蚌埠",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "32.939667",
        "longitude": "117.363228"
    },
    {
        "city_code": "101220301",
        "name_en": "wuhu",
        "name_zh": "芜湖",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "31.326319",
        "longitude": "118.376451"
    },
    {
        "city_code": "101220401",
        "name_en": "huainan",
        "name_zh": "淮南",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "32.647574",
        "longitude": "117.018329"
    },
    {
        "city_code": "101220501",
        "name_en": "maanshan",
        "name_zh": "马鞍山",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "31.689362",
        "longitude": "118.507906"
    },
    {
        "city_code": "101220601",
        "name_en": "anqing",
        "name_zh": "安庆",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "30.50883",
        "longitude": "117.043551"
    },
    {
        "city_code": "101220701",
        "name_en": "suzhou",
        "name_zh": "宿州",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "33.633891",
        "longitude": "116.984084"
    },
    {
        "city_code": "101220801",
        "name_en": "fuyang",
        "name_zh": "阜阳",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "32.896969",
        "longitude": "115.819729"
    },
    {
        "city_code": "101220901",
        "name_en": "bozhou",
        "name_zh": "亳州",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "33.869338",
        "longitude": "115.782939"
    },
    {
        "city_code": "101221001",
        "name_en": "huangshan",
        "name_zh": "黄山",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "29.709239",
        "longitude": "118.317325"
    },
    {
        "city_code": "101221101",
        "name_en": "chuzhou",
        "name_zh": "滁州",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "32.303627",
        "longitude": "118.316264"
    },
    {
        "city_code": "101221201",
        "name_en": "huaibei",
        "name_zh": "淮北",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "33.971707",
        "longitude": "116.794664"
    },
    {
        "city_code": "101221301",
        "name_en": "tongling",
        "name_zh": "铜陵",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "30.929935",
        "longitude": "117.816576"
    },
    {
        "city_code": "101221401",
        "name_en": "xuancheng",
        "name_zh": "宣城",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "30.945667",
        "longitude": "118.757995"
    },
    {
        "city_code": "101221501",
        "name_en": "luan",
        "name_zh": "六安",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "31.752889",
        "longitude": "116.507676"
    },
    {
        "city_code": "101221701",
        "name_en": "chizhou",
        "name_zh": "池州",
        "province_en": "anhui",
        "province_zh": "安徽省",
        "latitude": "30.656037",
        "longitude": "117.489157"
    },
    {
        "city_code": "101230101",
        "name_en": "fuzhou",
        "name_zh": "福州",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "26.075302",
        "longitude": "119.306239"
    },
    {
        "city_code": "101230201",
        "name_en": "xiamen",
        "name_zh": "厦门",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "24.490474",
        "longitude": "118.11022"
    },
    {
        "city_code": "101230301",
        "name_en": "ningde",
        "name_zh": "宁德",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "26.65924",
        "longitude": "119.527082"
    },
    {
        "city_code": "101230401",
        "name_en": "putian",
        "name_zh": "莆田",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "25.431011",
        "longitude": "119.007558"
    },
    {
        "city_code": "101230501",
        "name_en": "quanzhou",
        "name_zh": "泉州",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "24.908853",
        "longitude": "118.589421"
    },
    {
        "city_code": "101230601",
        "name_en": "zhangzhou",
        "name_zh": "漳州",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "24.510897",
        "longitude": "117.661801"
    },
    {
        "city_code": "101230701",
        "name_en": "longyan",
        "name_zh": "龙岩",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "25.091603",
        "longitude": "117.02978"
    },
    {
        "city_code": "101230801",
        "name_en": "sanming",
        "name_zh": "三明",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "26.265444",
        "longitude": "117.635001"
    },
    {
        "city_code": "101230901",
        "name_en": "nanping",
        "name_zh": "南平",
        "province_en": "fujian",
        "province_zh": "福建省",
        "latitude": "26.635627",
        "longitude": "118.178459"
    },
    {
        "city_code": "101240101",
        "name_en": "nanchang",
        "name_zh": "南昌",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "28.676493",
        "longitude": "115.892151"
    },
    {
        "city_code": "101240201",
        "name_en": "jiujiang",
        "name_zh": "九江",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "29.712034",
        "longitude": "115.992811"
    },
    {
        "city_code": "101240301",
        "name_en": "shangrao",
        "name_zh": "上饶",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "28.44442",
        "longitude": "117.971185"
    },
    {
        "city_code": "101240401",
        "name_en": "fuzhou",
        "name_zh": "抚州",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "27.98385",
        "longitude": "116.358351"
    },
    {
        "city_code": "101240501",
        "name_en": "yichun",
        "name_zh": "宜春",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "27.8043",
        "longitude": "114.391136"
    },
    {
        "city_code": "101240601",
        "name_en": "jian",
        "name_zh": "吉安",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "27.111699",
        "longitude": "114.986373"
    },
    {
        "city_code": "101240701",
        "name_en": "ganzhou",
        "name_zh": "赣州",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "25.85097",
        "longitude": "114.940278"
    },
    {
        "city_code": "101240801",
        "name_en": "jingdezhen",
        "name_zh": "景德镇",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "29.29256",
        "longitude": "117.214664"
    },
    {
        "city_code": "101240901",
        "name_en": "pingxiang",
        "name_zh": "萍乡",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "27.622946",
        "longitude": "113.852186"
    },
    {
        "city_code": "101241001",
        "name_en": "xinyu",
        "name_zh": "新余",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "27.810834",
        "longitude": "114.930835"
    },
    {
        "city_code": "101241101",
        "name_en": "yingtan",
        "name_zh": "鹰潭",
        "province_en": "jiangxi",
        "province_zh": "江西省",
        "latitude": "28.238638",
        "longitude": "117.033838"
    },
    {
        "city_code": "101250101",
        "name_en": "changsha",
        "name_zh": "长沙",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "28.19409",
        "longitude": "112.982279"
    },
    {
        "city_code": "101250201",
        "name_en": "xiangtan",
        "name_zh": "湘潭",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "27.82973",
        "longitude": "112.944052"
    },
    {
        "city_code": "101250301",
        "name_en": "zhuzhou",
        "name_zh": "株洲",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "27.835806",
        "longitude": "113.151737"
    },
    {
        "city_code": "101250401",
        "name_en": "hengyang",
        "name_zh": "衡阳",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "26.900358",
        "longitude": "112.607693"
    },
    {
        "city_code": "101250501",
        "name_en": "chenzhou",
        "name_zh": "郴州",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "25.793589",
        "longitude": "113.032067"
    },
    {
        "city_code": "101250601",
        "name_en": "changde",
        "name_zh": "常德",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "29.040225",
        "longitude": "111.691347"
    },
    {
        "city_code": "101250700",
        "name_en": "yiyang",
        "name_zh": "益阳",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "28.570066",
        "longitude": "112.355042"
    },
    {
        "city_code": "101250801",
        "name_en": "loudi",
        "name_zh": "娄底",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "27.728136",
        "longitude": "112.008497"
    },
    {
        "city_code": "101250901",
        "name_en": "shaoyang",
        "name_zh": "邵阳",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "27.237842",
        "longitude": "111.46923"
    },
    {
        "city_code": "101251001",
        "name_en": "yueyang",
        "name_zh": "岳阳",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "29.37029",
        "longitude": "113.132855"
    },
    {
        "city_code": "101251101",
        "name_en": "zhangjiajie",
        "name_zh": "张家界",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "29.127401",
        "longitude": "110.479921"
    },
    {
        "city_code": "101251201",
        "name_en": "huaihua",
        "name_zh": "怀化",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "27.550082",
        "longitude": "109.97824"
    },
    {
        "city_code": "101251401",
        "name_en": "yongzhou",
        "name_zh": "永州",
        "province_en": "hunan",
        "province_zh": "湖南省",
        "latitude": "26.434516",
        "longitude": "111.608019"
    },
    {
        "city_code": "101260101",
        "name_en": "guiyang",
        "name_zh": "贵阳",
        "province_en": "guizhou",
        "province_zh": "贵州省",
        "latitude": "26.578343",
        "longitude": "106.713478"
    },
    {
        "city_code": "101260201",
        "name_en": "zunyi",
        "name_zh": "遵义",
        "province_en": "guizhou",
        "province_zh": "贵州省",
        "latitude": "27.706626",
        "longitude": "106.937265"
    },
    {
        "city_code": "101270101",
        "name_en": "chengdu",
        "name_zh": "成都",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "30.659462",
        "longitude": "104.065735"
    },
    {
        "city_code": "101270201",
        "name_en": "panzhihua",
        "name_zh": "攀枝花",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "26.580446",
        "longitude": "101.716007"
    },
    {
        "city_code": "101270301",
        "name_en": "zigong",
        "name_zh": "自贡",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "29.352765",
        "longitude": "104.773447"
    },
    {
        "city_code": "101270401",
        "name_en": "mianyang",
        "name_zh": "绵阳",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "31.46402",
        "longitude": "104.741722"
    },
    {
        "city_code": "101270501",
        "name_en": "nanchong",
        "name_zh": "南充",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "30.795281",
        "longitude": "106.082974"
    },
    {
        "city_code": "101270601",
        "name_en": "dazhou",
        "name_zh": "达州",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "31.209484",
        "longitude": "107.502262"
    },
    {
        "city_code": "101270701",
        "name_en": "suining",
        "name_zh": "遂宁",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "30.513311",
        "longitude": "105.571331"
    },
    {
        "city_code": "101270901",
        "name_en": "bazhong",
        "name_zh": "巴中",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "31.858809",
        "longitude": "106.753669"
    },
    {
        "city_code": "101271001",
        "name_en": "luzhou",
        "name_zh": "泸州",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "28.889138",
        "longitude": "105.443348"
    },
    {
        "city_code": "101271101",
        "name_en": "yibin",
        "name_zh": "宜宾",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "28.760189",
        "longitude": "104.630825"
    },
    {
        "city_code": "101271201",
        "name_en": "neijiang",
        "name_zh": "内江",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "29.58708",
        "longitude": "105.066138"
    },
    {
        "city_code": "101271301",
        "name_en": "ziyang",
        "name_zh": "资阳",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "30.122211",
        "longitude": "104.641917"
    },
    {
        "city_code": "101271401",
        "name_en": "leshan",
        "name_zh": "乐山",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "29.582024",
        "longitude": "103.761263"
    },
    {
        "city_code": "101271501",
        "name_en": "meishan",
        "name_zh": "眉山",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "30.048318",
        "longitude": "103.831788"
    },
    {
        "city_code": "101271601",
        "name_en": "liangshan",
        "name_zh": "凉山",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "27.886762",
        "longitude": "102.258746"
    },
    {
        "city_code": "101272001",
        "name_en": "deyang",
        "name_zh": "德阳",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "31.127991",
        "longitude": "104.398651"
    },
    {
        "city_code": "101272101",
        "name_en": "guangyuan",
        "name_zh": "广元",
        "province_en": "sichuan",
        "province_zh": "四川省",
        "latitude": "32.433668",
        "longitude": "105.829757"
    },
    {
        "city_code": "101280101",
        "name_en": "guangzhou",
        "name_zh": "广州",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.125178",
        "longitude": "113.280637"
    },
    {
        "city_code": "101280201",
        "name_en": "shaoguan",
        "name_zh": "韶关",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "24.801322",
        "longitude": "113.591544"
    },
    {
        "city_code": "101280301",
        "name_en": "huizhou",
        "name_zh": "惠州",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.079404",
        "longitude": "114.412599"
    },
    {
        "city_code": "101280401",
        "name_en": "meizhou",
        "name_zh": "梅州",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "24.299112",
        "longitude": "116.117582"
    },
    {
        "city_code": "101280501",
        "name_en": "shantou",
        "name_zh": "汕头",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.37102",
        "longitude": "116.708463"
    },
    {
        "city_code": "101280601",
        "name_en": "shenzhen",
        "name_zh": "深圳",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "22.547",
        "longitude": "114.085947"
    },
    {
        "city_code": "101280701",
        "name_en": "zhuhai",
        "name_zh": "珠海",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "22.224979",
        "longitude": "113.553986"
    },
    {
        "city_code": "101280800",
        "name_en": "foshan",
        "name_zh": "佛山",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.028762",
        "longitude": "113.122717"
    },
    {
        "city_code": "101280901",
        "name_en": "zhaoqing",
        "name_zh": "肇庆",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.051546",
        "longitude": "112.472529"
    },
    {
        "city_code": "101281001",
        "name_en": "zhanjiang",
        "name_zh": "湛江",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "21.274898",
        "longitude": "110.364977"
    },
    {
        "city_code": "101281101",
        "name_en": "jiangmen",
        "name_zh": "江门",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "22.590431",
        "longitude": "113.094942"
    },
    {
        "city_code": "101281201",
        "name_en": "heyuan",
        "name_zh": "河源",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.746266",
        "longitude": "114.697802"
    },
    {
        "city_code": "101281301",
        "name_en": "qingyuan",
        "name_zh": "清远",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.685022",
        "longitude": "113.051227"
    },
    {
        "city_code": "101281401",
        "name_en": "yunfu",
        "name_zh": "云浮",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "22.929801",
        "longitude": "112.044439"
    },
    {
        "city_code": "101281501",
        "name_en": "chaozhou",
        "name_zh": "潮州",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.661701",
        "longitude": "116.632301"
    },
    {
        "city_code": "101281601",
        "name_en": "dongguan",
        "name_zh": "东莞",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.046237",
        "longitude": "113.746262"
    },
    {
        "city_code": "101281701",
        "name_en": "zhongshan",
        "name_zh": "中山",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "22.521113",
        "longitude": "113.382391"
    },
    {
        "city_code": "101281801",
        "name_en": "yangjiang",
        "name_zh": "阳江",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "21.859222",
        "longitude": "111.975107"
    },
    {
        "city_code": "101281901",
        "name_en": "jieyang",
        "name_zh": "揭阳",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "23.543778",
        "longitude": "116.355733"
    },
    {
        "city_code": "101282001",
        "name_en": "maoming",
        "name_zh": "茂名",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "21.659751",
        "longitude": "110.919229"
    },
    {
        "city_code": "101282101",
        "name_en": "shanwei",
        "name_zh": "汕尾",
        "province_en": "guangdong",
        "province_zh": "广东省",
        "latitude": "22.774485",
        "longitude": "115.364238"
    },
    {
        "city_code": "101290101",
        "name_en": "kunming",
        "name_zh": "昆明",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "25.040609",
        "longitude": "102.712251"
    },
    {
        "city_code": "101290201",
        "name_en": "dali",
        "name_zh": "大理",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "25.589449",
        "longitude": "100.225668"
    },
    {
        "city_code": "101290301",
        "name_en": "honghe",
        "name_zh": "红河",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "23.366775",
        "longitude": "103.384182"
    },
    {
        "city_code": "101290401",
        "name_en": "qujing",
        "name_zh": "曲靖",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "25.501557",
        "longitude": "103.797851"
    },
    {
        "city_code": "101290701",
        "name_en": "yuxi",
        "name_zh": "玉溪",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "24.350461",
        "longitude": "102.543907"
    },
    {
        "city_code": "101291001",
        "name_en": "zhaotong",
        "name_zh": "昭通",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "27.336999",
        "longitude": "103.717216"
    },
    {
        "city_code": "101291401",
        "name_en": "lijiang",
        "name_zh": "丽江",
        "province_en": "yunnan",
        "province_zh": "云南省",
        "latitude": "26.872108",
        "longitude": "100.233026"
    },
    {
        "city_code": "101300101",
        "name_en": "nanning",
        "name_zh": "南宁",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "22.82402",
        "longitude": "108.320004"
    },
    {
        "city_code": "101300301",
        "name_en": "liuzhou",
        "name_zh": "柳州",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "24.314617",
        "longitude": "109.411703"
    },
    {
        "city_code": "101300401",
        "name_en": "laibin",
        "name_zh": "来宾",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "23.733766",
        "longitude": "109.229772"
    },
    {
        "city_code": "101300501",
        "name_en": "guilin",
        "name_zh": "桂林",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "25.274215",
        "longitude": "110.299121"
    },
    {
        "city_code": "101300601",
        "name_en": "wuzhou",
        "name_zh": "梧州",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "23.474803",
        "longitude": "111.297604"
    },
    {
        "city_code": "101300801",
        "name_en": "guigang",
        "name_zh": "贵港",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "23.0936",
        "longitude": "109.602146"
    },
    {
        "city_code": "101300901",
        "name_en": "yulin",
        "name_zh": "玉林",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "22.63136",
        "longitude": "110.154393"
    },
    {
        "city_code": "101301101",
        "name_en": "qinzhou",
        "name_zh": "钦州",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "21.967127",
        "longitude": "108.624175"
    },
    {
        "city_code": "101301301",
        "name_en": "beihai",
        "name_zh": "北海",
        "province_en": "guangxi",
        "province_zh": "广西壮族自治区",
        "latitude": "21.473343",
        "longitude": "109.119254"
    },
    {
        "city_code": "101310101",
        "name_en": "haikou",
        "name_zh": "海口",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "20.031971",
        "longitude": "110.33119"
    },
    {
        "city_code": "101310201",
        "name_en": "sanya",
        "name_zh": "三亚",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "18.247872",
        "longitude": "109.508268"
    },
    {
        "city_code": "101310202",
        "name_en": "dongfang",
        "name_zh": "东方",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "19.10198",
        "longitude": "108.653789"
    },
    {
        "city_code": "101310211",
        "name_en": "qionghai",
        "name_zh": "琼海",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "19.246011",
        "longitude": "110.466785"
    },
    {
        "city_code": "101310212",
        "name_en": "wenchang",
        "name_zh": "文昌",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "19.612986",
        "longitude": "110.753975"
    },
    {
        "city_code": "101310215",
        "name_en": "wanning",
        "name_zh": "万宁",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "18.796216",
        "longitude": "110.388793"
    },
    {
        "city_code": "101310222",
        "name_en": "wuzhishan",
        "name_zh": "五指山",
        "province_en": "hainan",
        "province_zh": "海南省",
        "latitude": "18.776921",
        "longitude": "109.516662"
    },
    {
        "city_code": "101320101",
        "name_en": "hongkong",
        "name_zh": "香港岛",
        "province_en": "hongkong",
        "province_zh": "香港特别行政区",
        "latitude": "22.307",
        "longitude": "114.177"
    },
    {
        "city_code": "101330101",
        "name_en": "macao",
        "name_zh": "澳门",
        "province_en": "macao",
        "province_zh": "澳门特别行政区",
        "latitude": "22.202",
        "longitude": "113.544"
    },
    {
        "city_code": "101340101",
        "name_en": "taipei",
        "name_zh": "台北",
        "province_en": "taiwan",
        "province_zh": "台湾省",
        "latitude": "25.04",
        "longitude": "121.516"
    }
]


province_list = [
 '北京',
 '天津',
 '河北省',
 '山西省',
 '内蒙古自治区',
 '辽宁省',
 '吉林省',
 '黑龙江省',
 '上海',
 '江苏省',
 '浙江省',
 '安徽省',
 '福建省',
 '江西省',
 '山东省',
 '河南省',
 '湖北省',
 '湖南省',
 '广东省',
 '广西壮族自治区',
 '海南省',
 '重庆',
 '四川省',
 '贵州省',
 '云南省',
 '西藏自治区',
 '陕西省',
 '甘肃省',
 '青海省',
 '宁夏回族自治区',
 '新疆维吾尔自治区',
 '台湾省',
 '香港特别行政区',
 '澳门特别行政区']


def main():
    # 生成json文件
    res = []
    for i in province_list:
        tmp_prov = {}
        tmp_prov['name'] = i
        tmp_prov['sub'] = []
        for j in cities:
            if j['province_zh'] == i:
                tmp_prov['sub'].append(j['name_zh'])
        res.append(tmp_prov)
    with open('city283_v2123.json', 'w') as f:
        f.write(json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    print('共%s个城市' % len(cities))
    switch = input('是否生成json文件(1生成, 0不生成):')
    if switch == "1":
        main()
    else:
        exit()