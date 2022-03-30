package com.balf.boot.controller;



import com.balf.boot.bean.UserInfo;
import com.balf.boot.service.BlockService;
import com.balf.boot.service.UserService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import javax.servlet.http.HttpSession;


@Slf4j
@Controller
public class UserController {

    @Autowired
    UserService userService;

    /**
     * 来登录页
     * @return
     */
    @GetMapping(value = {"/","/login"})
    public String loginPage(){
        return "login";
    }


    @PostMapping("/login")
    public String login(UserInfo userInfo, HttpSession session, Model model){ //RedirectAttributes

        if(userService.login(userInfo) != null){
            //把登陆成功的用户保存起来
            session.setAttribute("loginUser",userInfo);
            //登录成功重定向到main.html;  重定向防止表单重复提交
            return "login-success";
        }else {
            model.addAttribute("msg","账号密码错误");
            //回到登录页面
            return "login";
        }

    }

    @GetMapping(value = {"/register"})
    public String registerPage(){

        return "register";
    }


    @PostMapping("/register")
    public String register(UserInfo userInfo, HttpSession session, Model model){ //RedirectAttributes
        String msg = userService.addUser(userInfo);
        if(msg == null){
            return "register-success";
        }else {
            model.addAttribute("msg",msg);
            return "register";
        }

    }

}
