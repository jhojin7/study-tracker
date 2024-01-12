package com.example.demo.controller;

import com.example.demo.model.Status;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;


@RestController
@RequestMapping(value="/status")
public class StatusController {
    @GetMapping(value="")
    public String getStatusUser(){
        return "status hello";
    }
    @GetMapping(value="/{sid}")
    public Status getStatusBySid(@PathVariable int sid){
        return Status.builder().sid(sid).uid("user1").result("wa").pid(1001).build();
    }

    @GetMapping(value="/user/{uid}")
    public List<Status> getStatusByUid(@PathVariable String uid){
        // return Status.findByUid(uid);
        List<Status> arr = new ArrayList<>();
        for (int i=0;i<5;i++)
            arr.add(Status.builder().sid(i).uid(uid).result("ac").pid(i).build());
        return arr;
    }
}
