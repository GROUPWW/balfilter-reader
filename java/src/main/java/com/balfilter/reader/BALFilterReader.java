package com.balfilter.reader;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.balfilter.reader.mapper") //加上mapperscan
public class BALFilterReader {

    public static void main(String[] args) {
        SpringApplication.run(BALFilterReader.class, args);
    }

}
