package com.atguigu.boot.service.impl;


import com.atguigu.boot.bean.BlockInfo;
import com.atguigu.boot.mapper.BlockMapper;
import com.atguigu.boot.service.BlockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

import static java.lang.Math.max;
import static java.lang.Math.min;

@Service
public class BlockServiceImpl implements BlockService {

    @Autowired
    BlockMapper blockMapper;

    public BlockInfo getOneBlockByConfidenceDesc(Integer index, String caseID){
        return blockMapper.getOneBlockByConfidenceDesc(index, caseID);
    }


    public Integer setOneAccepted(String imgName, Integer isAccepted,String caseID){
        return blockMapper.setOneAccepted(imgName, isAccepted,caseID);
    }








    // 这个应该移动到service里
    public List toNxnList(String nxn, Integer maxL, Integer pad){
        ArrayList<String> strings = new ArrayList<>();
        Integer r = Integer.valueOf(nxn.split("x")[0]);
        Integer c = Integer.valueOf(nxn.split("x")[1]);
        Integer centerIntRow = min(maxL - pad - 1, max(pad, r));
        Integer centerIntCol = min(maxL - pad - 1, max(pad, c));
        for(int i = centerIntRow- pad; i<centerIntRow + pad + 1; i+=1){
            for (int j = centerIntCol- pad; j<centerIntCol + pad + 1; j+=1){
                strings.add(i + "x" + j);
            }
        }

        return strings;
    }

}
