package com.balfilter.reader.bean;

import lombok.Data;
import org.springframework.transaction.annotation.Transactional;

import java.io.Serializable;


@Data
@Transactional
public class BlockInfo implements Serializable {

    private String imgName;

    private String confidence;

    private String model;

    private String comment;

    private Integer isAccepted;
}