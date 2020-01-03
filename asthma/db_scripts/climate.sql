DROP TABLE IF EXISTS `city`;

CREATE TABLE `city` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `city_code` varchar(64) NOT NULL  COMMENT '聚合API城市code',
  `name_en` varchar(64) NOT NULL  COMMENT '城市拼音名',
  `name_zh` varchar(128) NOT NULL  COMMENT '城市中文名',
  `province_en` varchar(64) NOT NULL  COMMENT '城市所在省拼音名',
  `province_zh` varchar(64) NOT NULL  COMMENT '城市所在省中文名',
  `latitude` varchar(64) NOT NULL  COMMENT '城市所在纬度',
  `longitude` varchar(64) NOT NULL  COMMENT '城市所在经度',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



DROP TABLE IF EXISTS `weather`;

CREATE TABLE `weather` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `city_code` varchar(64) NOT NULL  COMMENT '聚合API城市code',
  `weather_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '这一天的天气',
  `week` varchar(64) NOT NULL COMMENT '星期几',
  `temperature_average` varchar(64) NOT NULL  COMMENT '平均气温',
  `temperature_lowest` varchar(64) NOT NULL  COMMENT '最低气温',
  `temperature_highest` varchar(64) NOT NULL  COMMENT '最高气温',
  `wind_power` varchar(64) NOT NULL  COMMENT '风力等级',
  `wind_speed` varchar(64) NOT NULL COMMENT '风速',
  `humidity` int(11) NOT NULL COMMENT '湿度',
  `weather_condition` varchar(64) NOT NULL COMMENT 'weather condition天气情况(晴,阴等)',
  `ultraviolet` varchar(64) NOT NULL COMMENT '紫外线强度',
  `ultraviolet_description` varchar(64) NOT NULL COMMENT '紫外线建议和描述',
  `blood_sugar` varchar(64) NOT NULL COMMENT '血糖指数',
  `blood_sugar_description` varchar(64) NOT NULL COMMENT '血糖建议和描述',
  `dress` varchar(64) NOT NULL COMMENT '穿衣指数',
  `dress_description` varchar(64) NOT NULL  COMMENT '穿衣的建议和描述',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录的创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录的更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




DROP TABLE IF EXISTS `pm`;

CREATE TABLE `pm` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `city_code` varchar(64) NOT NULL COMMENT '聚合API城市code',
  `pm_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '这一天的PM值',
  `pm_25` varchar(64) NOT NULL  COMMENT 'PM2.5',
  `pm_10` varchar(128) NOT NULL  COMMENT 'PM10',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录的创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录的更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL COMMENT '角色id, 0位普通,1为管理员',
  `name` varchar(64) NOT NULL COMMENT '用户登陆账号',
  `password` varchar(64) NOT NULL DEFAULT '' COMMENT '用户密码',
  `fullname` varchar(64) NOT NULL COMMENT '用户姓名',
  `email` varchar(64) DEFAULT '' COMMENT '电子邮箱',
  `disabled` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` int(11) NOT NULL DEFAULT '0',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `risk_comment`;

CREATE TABLE `risk_comment` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `level` int(11) NOT NULL COMMENT '风险概率对应的等级',
  `threshold` float(6) NOT NULL COMMENT '风险概率阈值,0.2,0.4等',
  `comment` text NOT NULL  COMMENT '每个等级对应的评论',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录的创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录的更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `level_id` int(11) NOT NULL COMMENT '信息的严重等级id',
  `level_name` varchar(64) NOT NULL COMMENT '信息的严重等级名,共3种',
  `notification` text NOT NULL COMMENT '报错信息',
  `notification_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发生时间',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '该条记录更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
