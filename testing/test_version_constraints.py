#!/usr/bin/python3




from jk_version import *
from jk_version.constraints import *
from jk_testing import *




#
# Successes
#


@TestCase()
def test_0(ctx):
	v0 = Version("1.2.3")
	v1 = Version("1.2.4")

	assert VersionConstraintEQ(v0).check(v0)
	assert not VersionConstraintEQ(v0).check(v1)

	assert not VersionConstraintNE(v0).check(v0)
	assert VersionConstraintNE(v0).check(v1)

	assert VersionConstraintGE(v0).check(v0)
	assert VersionConstraintGE(v0).check(v1)

	assert not VersionConstraintGT(v0).check(v0)
	assert VersionConstraintGT(v0).check(v1)

	assert VersionConstraintLE(v0).check(v0)
	assert not VersionConstraintLE(v0).check(v1)

	assert not VersionConstraintLT(v0).check(v0)
	assert not VersionConstraintLT(v0).check(v1)
#

@TestCase()
def test_OR(ctx):
	v0 = Version("1.2.3")
	v1 = Version("1.2.4")
	v2 = Version("1.2.5")

	c = VersionConstraintOR(
		VersionConstraintEQ(v0),
		VersionConstraintEQ(v1),
	)

	assert c.check(v0)
	assert c.check(v1)
	assert not c.check(v2)
#

@TestCase()
def test_AND(ctx):
	v0 = Version("1.2.3")
	v1 = Version("1.2.4")
	v2 = Version("1.2.5")

	c = VersionConstraintAND(
		VersionConstraintEQ(v0),
		VersionConstraintEQ(v1),
	)

	assert not c.check(v0)
	assert not c.check(v1)
	assert not c.check(v2)
#


#
# Errors
#


# TODO



################################################################################################################################



testDriver = TestDriver()

results = testDriver.runTests([
	test_0,
	test_OR,
	test_AND,
])

#reporter = TestReporterHTML()
#reporter.report(results)
#reporter.report(results, webbrowserType="chromium")











