package com.atguigu.boot.mapper;

import com.atguigu.boot.bean.BlockInfo;
import org.springframework.stereotype.Repository;


@Repository
public interface BlockMapper {

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);
}

