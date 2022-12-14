package com.balfilter.reader.service;


import com.balfilter.reader.bean.BlockInfo;

import java.io.File;
import java.util.List;

public interface BlockService {

    public List toNxnList(String nxn, Integer maxL, Integer pad);

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);

    public Integer setOnePositive(String imgName, Integer isPositive,String caseID);

    public Integer addMessage(BlockInfo blockInfo, String addMessage,String caseID,String userInfo);

    public List cntRatio(String caseID);

    public List imgList();

    public File toPDF(String html);

    public List show369(String caseID);
}
