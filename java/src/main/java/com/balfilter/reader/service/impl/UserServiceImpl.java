package com.balfilter.reader.service.impl;


import com.balfilter.reader.bean.UserInfo;
import com.balfilter.reader.mapper.UserMapper;
import com.balfilter.reader.service.UserService;
import com.balfilter.reader.util.RSAUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.DigestUtils;

//import javax.swing.text.Document;

import static java.lang.Math.max;
import static java.lang.Math.min;


@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserMapper userMapper;

    String salt = "20211021"; //盐值

    public String addUser(UserInfo userInfo) throws Exception {
        if(userInfo.getUserName() == null || userInfo.getUserName().length() == 0) return "请输入用户名";
        if(userInfo.getPassword() == null || userInfo.getPassword().length() == 0) return "请输入密码";
        if(!userInfo.getEmail().matches("\\w+@\\w+(\\.\\w{2,3})*\\.\\w{2,3}")) return "请输入正确的邮箱";
        if(userInfo.getPhone() == null || userInfo.getPhone().length() != 11) return "请输入正确的手机号码";
        if(userMapper.cntUser(userInfo.getUserName())>0) return "该用户名已存在";

        userInfo.setPassword(RSAUtil.decryptWithPrivate(userInfo.getPassword()));
        String md5Password = DigestUtils.md5DigestAsHex((userInfo.getPassword() + salt).getBytes()); //密码md5加盐
        userInfo.setPassword(md5Password);

        userMapper.addUser(userInfo);
        return null;
    }

    public UserInfo login(UserInfo userInfo) throws Exception {

        String before = userInfo.getPassword();
        userInfo.setPassword(RSAUtil.decryptWithPrivate(userInfo.getPassword()));
        String after = userInfo.getPassword();

        String inputMd5Password = DigestUtils.md5DigestAsHex((userInfo.getPassword() + salt).getBytes());
        UserInfo databaseUserInfo = userMapper.selectOneUser(userInfo);
        // System.out.println(databaseUserInfo);
        if(databaseUserInfo == null) return null;
        String trueMd5Password = databaseUserInfo.getPassword();
        if(inputMd5Password.equals(trueMd5Password)) return databaseUserInfo;
        return null;
    }



}
