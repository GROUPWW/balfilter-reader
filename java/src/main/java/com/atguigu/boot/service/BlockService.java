package com.atguigu.boot.service;


import com.atguigu.boot.bean.BlockInfo;

import java.util.List;

public interface BlockService {

    public List toNxnList(String nxn, Integer maxL, Integer pad);

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);
}
