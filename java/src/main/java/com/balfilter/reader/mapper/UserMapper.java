package com.balfilter.reader.mapper;

import com.balfilter.reader.bean.UserInfo;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;


@Repository
public interface UserMapper {

//    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID);

    @Insert("insert into user (user_name,password,email,phone) values(#{userName},#{password},#{email},#{phone})")
    public Integer addUser(UserInfo userInfo);

    @Select("select count(*) from user where user_name=#{userName}")
    public Integer cntUser(String username);

    @Select("select * from user where user_name=#{userName}")
    public UserInfo selectOneUser(UserInfo userInfo);
}

