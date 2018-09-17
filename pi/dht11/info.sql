-- ----------------------------
-- 创建数据表结构
-- ----------------------------

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for info
-- ----------------------------
DROP TABLE IF EXISTS `info`;
CREATE TABLE `info`  (
  `tid` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nowtime` bigint(255) UNSIGNED NOT NULL,
  `temperature` int(255) NOT NULL,
  `humidity` int(255) UNSIGNED NOT NULL,
  PRIMARY KEY (`tid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3310 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
