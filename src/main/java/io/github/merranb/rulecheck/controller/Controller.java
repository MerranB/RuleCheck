package io.github.merranb.rulecheck.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping(path = "/RuleCheck")

public class Controller {

    @PostMapping(path= "/v1/decisions", consumes = "application/json", produces = "application/json")

    public String validate(@RequestBody Map<String, String> payload)
    {
        String value = payload.get("result");

        if ("Good".equalsIgnoreCase(value)) {
            return "Valid";
        } else {
            return "Invalid";
        }
    }
}