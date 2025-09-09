package io.github.merranb.rulecheck.repository;

import io.github.merranb.rulecheck.model.Rule;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RuleRepository extends JpaRepository<Rule, Long> {
}
