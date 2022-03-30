package com.balf.boot.service;


import com.balf.boot.bean.BlockInfo;
import com.balf.boot.bean.UserInfo;

import java.util.List;

public interface UserService {

//    public List toNxnList(String nxn, Integer maxL, Integer pad);
//
//    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);
//
//    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);

    public String addUser(UserInfo userInfo);

    public UserInfo login(UserInfo userInfo);
}
