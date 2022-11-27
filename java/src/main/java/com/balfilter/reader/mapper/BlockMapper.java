package com.balfilter.reader.mapper;

import com.balfilter.reader.bean.BlockInfo;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;


@Repository
public interface BlockMapper {

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);

    public Integer setOnePositive(String imgName, Integer isPositive,String caseID);

    @Update("update database_${caseID} set comment = #{newMessageJson} where img_name = #{blockInfo.imgName}")
    public Integer addMessage(BlockInfo blockInfo,String newMessageJson,String caseID);

    @Select("with t0 as (select count(*) as t0 from database_${caseID} where CONFIDENCE =0 and is_valid=1),t_small as (select count(*) as t_small from database_${caseID} where CONFIDENCE >0 and CONFIDENCE<0.3),t1 as (select count(*) as t1 from database_${caseID} where CONFIDENCE >=0.3 and CONFIDENCE<0.6),t3 as (select count(*) as t3 from database_${caseID} where CONFIDENCE>=0.6 and CONFIDENCE<0.9),t4 as (select count(*) as t4 from database_${caseID} where CONFIDENCE>=0.9) select * from t0,t_small,t1,t3,t4")
    public Map cnt(String caseID);

    @Select("select * from information_schema.TABLES where TABLE_SCHEMA=(select database())")
    public List<Map> listTable();

    @Select("with t1 as (select AVG(CONFIDENCE) as t1 from database_${caseID} where CONFIDENCE >=0.3),t3 as (select AVG(CONFIDENCE) as t3  from database_${caseID} where CONFIDENCE>=0.6),t4 as (select AVG(CONFIDENCE) as t4 from database_${caseID} where CONFIDENCE>=0.9) select * from t1,t3,t4")
    public List<Map> cntAvg(String caseID);

    @Select("with t1 as (select count(*) as t1 from database_${caseID} where CONFIDENCE >=0.3),t3 as (select count(*) as t3 from database_${caseID} where CONFIDENCE>=0.6),t4 as (select count(*) as t4 from database_${caseID} where CONFIDENCE>=0.9) select * from t1,t3,t4")
    public List<Map> cntNum(String caseID);
}

