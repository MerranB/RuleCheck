package io.github.merranb.rulecheck.model;

public class Policy {

    public Policy(Rule rule) {
        this.rule = rule;
    }

    public Rule getRule() {
        return rule;
    }

    public void setRule(Rule rule) {
        this.rule = rule;
    }

    Rule rule;

}
