--create database xinsheng;
CREATE TABLE IF NOT EXISTS `house`(
   `house_id`   INT UNSIGNED AUTO_INCREMENT,
   `ke_id`      VARCHAR(20),                                --贝壳网中的id
   `xiaoqu_id`  VARCHAR(20),                                --小区id
   `build_area` FLOAT,                                      --建筑面积
   `inner_area` FLOAT,                                      --套内面积
   `direction`  VARCHAR(5),                                 --朝向
   `floor`      VARCHAR(5),                                 --楼层
   `build_year` INT,                                        --始建年
   `suite_type` VARCHAR(10),                                --户型（几套几）
   `house_year` INT,                                        --房屋年限
   `is_deal`    TINYINT(1)                                  --是否成交
   `deal_price` FLOAT                                       --成交价
   `deal_date`  DATETIME                                    --成交时间
   PRIMARY KEY ( `house_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `price`(
   `price_id`           INT UNSIGNED AUTO_INCREMENT,
   `house_id`           INT UNSIGNED ,                      --房屋id
   `expect_price`       FLOAT ,                             --挂牌价格
   `expect_date`        DATETIME ,                          --挂牌时间
   PRIMARY KEY ( `price_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;