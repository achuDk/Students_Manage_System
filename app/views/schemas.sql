# 创建表结构

# 班级表
CREATE TABLE IF NOT EXISTS classes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(30) NOT NULL UNIQUE
);

# 教师表
CREATE TABLE IF NOT EXISTS teachers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL
);

# 班级_教师-多对多_关系表
CREATE TABLE IF NOT EXISTS cls_tch (
  id INT PRIMARY KEY AUTO_INCREMENT,
  cid INT,
  tid INT,
  FOREIGN KEY (cid) REFERENCES classes(id),
  FOREIGN KEY (tid) REFERENCES teachers(id)
);

# 学生表_多对一班级
CREATE TABLE IF NOT EXISTS students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  age INT,
  gender ENUM('female','male'),
  cid INT,
  FOREIGN KEY (cid) REFERENCES classes(id)
);