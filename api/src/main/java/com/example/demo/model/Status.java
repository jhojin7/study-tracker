package com.example.demo.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.*;

@Builder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Status {
    // sid pid uid result timestamp
    public int sid;
    private int pid;
    public String uid;
    private String result;

}

