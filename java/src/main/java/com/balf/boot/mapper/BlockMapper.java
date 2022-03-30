package com.balf.boot.mapper;

import com.balf.boot.bean.BlockInfo;
import org.apache.ibatis.annotations.Update;
import org.springframework.stereotype.Repository;


@Repository
public interface BlockMapper {

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);

    @Update("update database_${caseID} set comment = #{newMessageJson} where img_name = #{blockInfo.imgName}")
    public Integer addMessage(BlockInfo blockInfo,String newMessageJson,String caseID);
}

