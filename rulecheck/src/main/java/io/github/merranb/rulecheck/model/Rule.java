package io.github.merranb.rulecheck.model;

public class Rule {

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    String name;
    String description;

    public Rule(String name, String description) {
        this.name = name;
        this.description = description;
    }




}
