package io.github.merranb.rulecheck.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/RuleCheck")

public class Controller {

    @PostMapping(path= "/v1/decisions", consumes = "application/json", produces = "application/json")

    public String helloGFG()
    {
        return "Hello GeeksForGeeks";
    }
}