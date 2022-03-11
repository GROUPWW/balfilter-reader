package com.balf.boot.mapper;

import com.balf.boot.bean.BlockInfo;
import org.springframework.stereotype.Repository;


@Repository
public interface BlockMapper {

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);
}

