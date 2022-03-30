package com.balf.boot.bean;

import lombok.Data;

import java.io.Serializable;


@Data
public class UserInfo implements Serializable {

    private String userName;

    private String password;

    private String email;

    private String phone;
}