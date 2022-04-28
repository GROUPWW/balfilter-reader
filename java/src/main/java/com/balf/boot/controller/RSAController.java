package com.balf.boot.controller;

import com.balf.boot.util.RSAUtil;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RSAController {

    @RequestMapping("/getPublicKey")
    public String getPublicKey(){
        return RSAUtil.getPublicKey();
    }
}
