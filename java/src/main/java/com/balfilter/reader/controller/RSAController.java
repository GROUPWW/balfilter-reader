package com.balfilter.reader.controller;

import com.balfilter.reader.util.RSAUtil;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RSAController {

    @RequestMapping("/getPublicKey")
    public String getPublicKey(){
        return RSAUtil.getPublicKey();
    }

    @RequestMapping("/getPrivateKey")
    public String getPrivateKey(){
        return RSAUtil.getPrivateKey();
    }
}
