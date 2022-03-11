package com.balf.boot.bean;

import lombok.Data;

import java.io.Serializable;


@Data
public class BlockInfo implements Serializable {

    private String imgName;

    private String confidence;

    private String model;

    private String comment;

    private Integer isAccepted;
}