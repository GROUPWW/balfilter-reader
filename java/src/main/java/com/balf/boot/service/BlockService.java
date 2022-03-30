package com.balf.boot.service;


import com.balf.boot.bean.BlockInfo;

import java.util.List;

public interface BlockService {

    public List toNxnList(String nxn, Integer maxL, Integer pad);

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);

    public Integer addMessage(BlockInfo blockInfo, String addMessage,String caseID,String userInfo);
}
