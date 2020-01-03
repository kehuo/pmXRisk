目前2个模版 climate operation <br>

### 天气服务网站: https://www.tianqiapi.com/ <br>
### 天气服务 appid: "67548155" appsecret: "BGrju1UP"):<br>

### pm 服务网站:https://aqicn.org/json-api/doc/<br>

Todo <br>
### 定时检查缺失数据的机制<br>
1 每一段时间检查所有城市的weather/pm 数据。如果一段时间内数据缺失量较大，暂时将该城市的"status"字段设置为 "disabled city"中， 下次检查如果数据恢复，则重新将status字段设置为"active city". <br>
2 需要更新 city 表, 加一列 "status", 值暂定取"disabled" 和 "active". <br>
3 注: 当前city表还未添加active字段<br>
### 定时清理过期数据及冷数据分区<br>
1 定时清理时间过久的数据<br>
2 冷数据分区等处理<br>


