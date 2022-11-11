package com.balfilter.reader.service;


import com.balfilter.reader.bean.UserInfo;

public interface UserService {

//    public List toNxnList(String nxn, Integer maxL, Integer pad);
//
//    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);
//
//    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID);

    public String addUser(UserInfo userInfo) throws Exception;

    public UserInfo login(UserInfo userInfo) throws Exception;
}
