CREATE DATABASE `covid19donor` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `covid19donor`.`credentials` (
  `userId` varchar(50) NOT NULL,
  `password` varchar(45) NOT NULL,
  `memberId` int NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `covid19donor`.`member` (
  `memberId` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `bloodGroup` varchar(10) NOT NULL,
  `city` varchar(45) NOT NULL,
  `isActive` tinyint DEFAULT NULL,
  PRIMARY KEY (`memberId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `covid19donor`.`credentials` (
  `userId` varchar(50) NOT NULL,
  `password` varchar(45) NOT NULL,
  `memberId` int NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `covid19donor`.`donors` (
  `iddonors` int NOT NULL,
  `memberId` int NOT NULL,
  `dateOfRequest` varchar(20) NOT NULL,
  PRIMARY KEY (`iddonors`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `covid19donor`.`patients` (
  `idpatients` int NOT NULL,
  `memberId` int NOT NULL,
  `dateOfRequest` varchar(20) NOT NULL,
  PRIMARY KEY (`idpatients`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `covid19donor`.`credentials`
(`userId`,
`password`,
`memberId`)
VALUES
('dsutradhar',
'cGFzc3dvcmQ=',
1);

INSERT INTO `covid19donor`.`credentials`
(`userId`,
`password`,
`memberId`)
VALUES
('monali',
'cGFzc3dvcmQ=',
1);

INSERT INTO `covid19donor`.`member`
(`memberId`,
`name`,
`area`,
`phoneNumber`,
`bloodGroup`,
`city`,
`isActive`)
VALUES
(1,
'Monali Sutradhar',
'Chhend Area',
'8055425098',
'A+',
'Rourkela',
1);

INSERT INTO `covid19donor`.`member`
(`memberId`,
`name`,
`area`,
`phoneNumber`,
`bloodGroup`,
`city`,
`isActive`)
VALUES
(2,
'Dipankar Sutradhar',
'Sector Area',
'8055425098',
'A+',
'Rourkela',
1);
