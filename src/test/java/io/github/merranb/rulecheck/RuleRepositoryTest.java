package io.github.merranb.rulecheck;

import io.github.merranb.rulecheck.model.Rule;
import io.github.merranb.rulecheck.repository.RuleRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
@ActiveProfiles("test")
class RuleRepositoryTest {

	@Autowired
	private RuleRepository ruleRepository;

	@Test
	void testSaveAndFindRule() {
		Rule rule = new Rule();
		rule.setName("Test Rule");

		Rule saved = ruleRepository.save(rule);
		assertThat(saved.getId()).isNotNull();

		Rule found = ruleRepository.findById(saved.getId()).orElse(null);
		assertThat(found).isNotNull();
		assertThat(found.getName()).isEqualTo("Test Rule");
	}
}
