package io.github.merranb.rulecheck.model;

public class AuditEvent {

    String date_time;
    String event;

    public String getDate_time() {
        return date_time;
    }

    public void setDate_time(String date_time) {
        this.date_time = date_time;
    }

    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public AuditEvent() {
    }

}
