-- upos_service 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `upos_service` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `upos_service`;

-- 테이블 upos_service.UnitReal 구조 내보내기
CREATE TABLE IF NOT EXISTS `UnitReal` (
  `szUnitID` varchar(50) DEFAULT NULL,
  `runDatetime` datetime DEFAULT NULL,
  `Power` double DEFAULT NULL,
  `ChilledWater_Q` double DEFAULT NULL,
  `ChilledWater_In_T` double DEFAULT NULL,
  `ChilledWater_Out_T` double DEFAULT NULL,
  `ChilledWater_Delta_T` double DEFAULT NULL,
  `ChilledWater_USRT` double DEFAULT NULL,
  `Part_Load_Ratio` double DEFAULT NULL,
  `ChilledWater_eUSRT` double DEFAULT NULL,
  `ChilledWater_tUSRT` double DEFAULT NULL,
  `Run_Time` int(11) DEFAULT NULL,
  `RunTime_Rate` int(11) DEFAULT NULL,
  `Temperature_Control_Eff` double DEFAULT NULL,
  `Demand_Responding_Eff` double DEFAULT NULL,
  `Demand_Responding_eEff` double DEFAULT NULL,
  `Demand_Responding_tEff` double DEFAULT NULL,
  `Equipment_Running_Eff` double DEFAULT NULL,
  `Equipment_Running_eEff` double DEFAULT NULL,
  `Equipment_Running_tEff` double DEFAULT NULL,
  `Energy_PUB` double DEFAULT NULL,
  `Energy_ePUB` double DEFAULT NULL,
  `Energy_tPUB` double DEFAULT NULL,
  `Energy_EFF` double DEFAULT NULL,
  `Energy_eEFF` double DEFAULT NULL,
  `Energy_tEFF` double DEFAULT NULL,
  `OilPress_Delta_T` double DEFAULT NULL,
  `_ChilledWater_In_T` double DEFAULT NULL,
  `_ChilledWater_Out_T` double DEFAULT NULL,
  `CoolingWater_In_T` double DEFAULT NULL,
  `CoolingWater_Out_T` double DEFAULT NULL,
  `Evaporator_T` double DEFAULT NULL,
  `Condenser_T` double DEFAULT NULL,
  `CompDischarge_T` double DEFAULT NULL,
  `OilTank_T` double DEFAULT NULL,
  `Bearing_T` double DEFAULT NULL,
  `Motor_R_T` double DEFAULT NULL,
  `Motor_S_T` double DEFAULT NULL,
  `Motor_T_T` double DEFAULT NULL,
  `OilTank_P` double DEFAULT NULL,
  `OilPump_P` double DEFAULT NULL,
  `Motor_A` double DEFAULT NULL,
  `Motor_V` double DEFAULT NULL,
  `Vane_Pct` double DEFAULT NULL,
  `Diffuser_Pct` double DEFAULT NULL,
  `Evaporator_P` double DEFAULT NULL,
  `Condenser_P` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOAD DATA LOCAL INFILE
'/UnitReal_df_month.csv' into table UnitReal
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(szUnitID,runDatetime,Power,ChilledWater_Q,ChilledWater_In_T,ChilledWater_Out_T,ChilledWater_Delta_T,ChilledWater_USRT,Part_Load_Ratio,ChilledWater_eUSRT,ChilledWater_tUSRT,Run_Time,RunTime_Rate,Temperature_Control_Eff,Demand_Responding_Eff,Demand_Responding_eEff,Demand_Responding_tEff,Equipment_Running_Eff,Equipment_Running_eEff,Equipment_Running_tEff,Energy_PUB,Energy_ePUB,Energy_tPUB,Energy_EFF,Energy_eEFF,Energy_tEFF,OilPress_Delta_T,_ChilledWater_In_T,_ChilledWater_Out_T,CoolingWater_In_T,CoolingWater_Out_T,Evaporator_T,Condenser_T,CompDischarge_T,OilTank_T,Bearing_T,Motor_R_T,Motor_S_T,Motor_T_T,OilTank_P,OilPump_P,Motor_A,Motor_V,Vane_Pct,Diffuser_Pct,Evaporator_P,Condenser_P);
