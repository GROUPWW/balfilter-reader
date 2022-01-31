package com.atguigu.boot.controller;


import com.atguigu.boot.bean.BlockInfo;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.List;


@Controller
// @RestController //会去往json响应了
public class BlockController {

    // 就Desc查一条吧
    @GetMapping("/100086/{topSusId}")
    public String getUser(HttpServletRequest request,@PathVariable("topSusId") Integer topSusId){
        System.out.println("test");

//        // mock数据，取出倒叙数据出来
//        ArrayList<BlockInfo> blockInfos = new ArrayList<>();
//
//        // mock数据
//        BlockInfo blockInfo1 = new BlockInfo();
//        blockInfo1.setImgName("11x11");
//
//        blockInfos.add(blockInfo1);
//
//
//        // mock数据
//        BlockInfo blockInfo2 = new BlockInfo();
//        blockInfo2.setImgName("22x22");
//
//        blockInfos.add(blockInfo2);
//        request.setAttribute("topSusId",topSusId);
//        request.setAttribute("blockInfo",blockInfos.get(topSusId));

        BlockInfo blockInfo = service


        return "imageview";
    }


    @GetMapping("/test0119")
    public String getUser1(){
        System.out.println("test");
        return "index";
    }


}
