package com.balfilter.reader.controller;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;


@Controller
// @RestController //会去往json响应了
public class MainController {

    @Value("${file.upload.dir}")
    private String realPath;

    @GetMapping(value = "/upload")
    public String getUpload(){
        return "upload";
    }

    @PostMapping("/upload")
    // 定义：接收文件对象 MultipartFile file变量名要与form表单中input type="file" 标签name属性名一致
    public String upload_dataset(MultipartFile file) throws IOException, InterruptedException {

        // 文件名
        String originalFilename = file.getOriginalFilename();
        System.out.println(originalFilename);

        // 上传文件到哪
        file.transferTo(new File(realPath, originalFilename));
        System.out.println(originalFilename);

        Process process = Runtime.getRuntime().exec("python E://wangningyu/BALF/detect_upload.py --img " + originalFilename);
//
        String ls_1;
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        while ( (ls_1=bufferedReader.readLine()) != null)
            System.out.println(ls_1);

        return "upload-success";
    }


    @GetMapping(value = "/")
    public String loginPage(){
        return "main";
    }





}




