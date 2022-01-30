#!/usr/bin/python3




import jk_version
import jk_testing
import jk_json





@jk_testing.TestCase()
def test_case_0(ctx):
	constraint1 = \
		jk_version.VersionConstraintAND(
			jk_version.VersionConstraintAND(
				jk_version.VersionConstraintGE(
					jk_version.Version("2.3.4"),
				),
				jk_version.VersionConstraintGT(
					jk_version.Version("3.4.5"),
				),
			),
			jk_version.VersionConstraintOR(
				jk_version.VersionConstraintLE(
					jk_version.Version("4.5.6"),
				),
				jk_version.VersionConstraintLT(
					jk_version.Version("5.6.7"),
				),
			),
			jk_version.VersionConstraintEQ(
				jk_version.Version("1.2.3")
			),
		)
	jData1 = constraint1.toJSON()

	print("-" * 120)
	jk_json.prettyPrint(jData1)
	print("-" * 120)

	constraint2 = jk_version.deserializeConstraint(jData1)
	jData2 = constraint2.toJSON()

	jk_json.prettyPrint(jData2)
	print("-" * 120)

	jk_testing.Assert.isEqual(jData1, jData2)
#




################################################################################################################################




testDriver = jk_testing.TestDriver()

results = testDriver.runTests([
	(test_case_0, True),
])

#reporter = TestReporterHTML()
#reporter.report(results, webbrowserType="chromium")











