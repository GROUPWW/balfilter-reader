package com.atguigu.boot.controller;


import com.atguigu.boot.bean.BlockInfo;
import com.atguigu.boot.service.BlockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Math.max;
import static java.lang.Math.min;


@Controller
// @RestController //会去往json响应了
public class BlockController {

    @Autowired
    BlockService blockService;

    // 就Desc查一条吧
    @GetMapping("/result/{caseID}/{topSusId}")
    public String get(HttpServletRequest request,@PathVariable("topSusId") Integer topSusId,@PathVariable("caseID") String caseID){

        BlockInfo blockInfo = blockService.getOneBlockByConfidenceDesc(topSusId, caseID);
        request.setAttribute("blockInfo",blockInfo);
        request.setAttribute("t3x3List",blockService.toNxnList(blockInfo.getImgName(),98,1));
        request.setAttribute("t5x5List",blockService.toNxnList(blockInfo.getImgName(),98,2));

        return "imageview";
    }

    @PostMapping("/result/{caseID}/{topSusId}")
    public String post(HttpServletRequest request,@PathVariable("topSusId") Integer topSusId,@PathVariable("caseID") String caseID,Integer isAccepted){

        BlockInfo blockInfo = blockService.getOneBlockByConfidenceDesc(topSusId, caseID);


        blockService.setOneAccepted(blockInfo.getImgName(), isAccepted,caseID);
        request.setAttribute("blockInfo",blockInfo);
        request.setAttribute("t3x3List",blockService.toNxnList(blockInfo.getImgName(),98,1));
        request.setAttribute("t5x5List",blockService.toNxnList(blockInfo.getImgName(),98,2));

        return "imageview";
    }

//    @GetMapping("/test0119")
//    public String getUser1(){
//        System.out.println("test");
//        return "index";
//    }



//    def to_nxn_list(nxn,max_l,pad):
//    r,c = int(nxn.split('x')[0]),int(nxn.split('x')[1])
//    center_int_row = min(max_l - pad - 1, max(pad, r))
//    center_int_col = min(max_l - pad - 1, max(pad, c))
//    nxn_res = []
//            for i in range(center_int_row - pad, center_int_row + pad + 1):
//            for j in range(center_int_col - pad, center_int_col + pad+ 1):
//            nxn_res.append(str(i)+"x"+str(j))
//            return nxn_res

}
