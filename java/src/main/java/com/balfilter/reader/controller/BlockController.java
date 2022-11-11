package com.balfilter.reader.controller;


import com.alibaba.fastjson.JSON;
import com.balfilter.reader.bean.BlockInfo;
import com.balfilter.reader.bean.UserInfo;
import com.balfilter.reader.service.BlockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Math.max;
import static java.lang.Math.min;


@Controller
// @RestController //会去往json响应了
public class BlockController {

    @Autowired
    BlockService blockService;

    @Value("${file.upload.dir}")
    private String realPath;

    @Autowired
    TemplateEngine templateEngine;

    // 就Desc查一条吧
    @GetMapping("/result/{caseID}/{topSusId}")
    public String get(HttpServletRequest request,@PathVariable("topSusId") Integer topSusId,@PathVariable("caseID") String caseID){

        if (topSusId < 0) {
            topSusId = 0;
        }
        BlockInfo blockInfo = blockService.getOneBlockByConfidenceDesc(topSusId, caseID);
        if (blockInfo == null) {
            return "imageview";
        }
        return getBlock(request, blockInfo, caseID);

//        ArrayList arrayList = new ArrayList();
//        ArrayList innerArrayList = new ArrayList();
//        innerArrayList.add("啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊");
//        innerArrayList.add("刘大夫");
//        innerArrayList.add("2017-12-12 17:55:00");
//        arrayList.add(innerArrayList);
//        request.setAttribute("messageList", arrayList);
    }

    @PostMapping("/result/{caseID}/{topSusId}")
    public String post(HttpServletRequest request,@PathVariable("topSusId") Integer topSusId,@PathVariable("caseID") String caseID,Integer isAccepted,String addMessage){
        BlockInfo blockInfo = blockService.getOneBlockByConfidenceDesc(topSusId, caseID);

        if(isAccepted != null) blockService.setOneAccepted(blockInfo.getImgName(), isAccepted,caseID);
        if(addMessage != null){
            HttpSession session = request.getSession();
            UserInfo userInfo = (UserInfo)session.getAttribute("loginUser");
            blockService.addMessage(blockInfo,addMessage,caseID,userInfo.getUserName());
        }

        blockInfo = blockService.getOneBlockByConfidenceDesc(topSusId, caseID); //防止post后还是上一次的状态
        return getBlock(request, blockInfo, caseID);
    }

    private String getBlock(HttpServletRequest request, BlockInfo blockInfo, String caseID) {
        List<ArrayList> oldMessageList = JSON.parseArray(blockInfo.getComment(), ArrayList.class);
        request.setAttribute("messageList",oldMessageList);
        request.setAttribute("blockInfo",blockInfo);
        request.setAttribute("t3x3List",blockService.toNxnList(blockInfo.getImgName(),98,1));
        request.setAttribute("t5x5List",blockService.toNxnList(blockInfo.getImgName(),98,2));
        request.setAttribute("cntRatio",blockService.cntRatio(caseID));
        request.setAttribute("show369",blockService.show369(caseID));
        return "imageview";
    }



    @ResponseBody
    @RequestMapping("/upload/{blockName}")
    // 定义：接收文件对象 MultipartFile file变量名要与form表单中input type="file" 标签name属性名一致
    public String upload(MultipartFile file,@PathVariable("blockName") String blockName) throws IOException {

        // 文件名
        String originalFilename = file.getOriginalFilename();

        String newFileName = blockName;

        // 上传文件到哪
        file.transferTo(new File(realPath, newFileName));
        return "纠正成功";
    }




    @ResponseBody
    @RequestMapping("/toPDF/{caseID}/{topSusId}")
    public String toPDF(Context context, @PathVariable("topSusId") Integer topSusId, @PathVariable("caseID") String caseID, HttpServletResponse response) throws IOException {
        BlockInfo blockInfo = blockService.getOneBlockByConfidenceDesc(topSusId, caseID);
        List<ArrayList> oldMessageList = JSON.parseArray(blockInfo.getComment(), ArrayList.class);
        context.setVariable("messageList",oldMessageList);
        context.setVariable("blockInfo",blockInfo);
        context.setVariable("t3x3List",blockService.toNxnList(blockInfo.getImgName(),98,1));
        context.setVariable("t5x5List",blockService.toNxnList(blockInfo.getImgName(),98,2));
        context.setVariable("cntRatio",blockService.cntRatio(caseID));
        context.setVariable("topSusId",topSusId);
        context.setVariable("caseID",caseID);
        context.setVariable("show369",blockService.show369(caseID));
        System.out.println(context);
        String result = templateEngine.process("table", context);
        System.out.println(result);
        File file = blockService.toPDF(result);

        if (!file.exists()) {
            return "下载文件不存在";
        }
        response.reset();
        response.setContentType("application/octet-stream");
        response.setCharacterEncoding("utf-8");
        response.setContentLength((int) file.length());
        // 设置编码格式
        response.setHeader("Content-Disposition",
                "attachment;fileName=" + caseID + "_" + blockInfo.getImgName()+".pdf");
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(file));
        byte[] buff = new byte[1024];
        OutputStream os = response.getOutputStream();
        int i = 0;
        while ((i = bis.read(buff)) != -1) {
            os.write(buff, 0, i);
            os.flush();
        }
        bis.close();
        os.close();
        return "下载成功";
    }

    @GetMapping(value = "/imgList")
    public String getUpload(HttpServletRequest request){
        List imgList = blockService.imgList();
        request.setAttribute("imgList",imgList);
        return "imgList";
    }

}




