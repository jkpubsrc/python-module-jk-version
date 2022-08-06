#!/usr/bin/python3




from jk_version import *
from jk_testing import *




#
# Successes
#


@TestCase()
def test_case_regular_0(ctx):
	Assert.isEqual(Version("0"), "0")
#

@TestCase()
def test_case_regular_1(ctx):
	Assert.isEqual(Version("1"), "1")
#

@TestCase()
def test_case_regular_2(ctx):
	Assert.isEqual(Version("1.2"), "1.2")
#

@TestCase()
def test_case_regular_3(ctx):
	Assert.isEqual(Version("1.2.3"), "1.2.3")
#

@TestCase()
def test_case_regular_4(ctx):
	Assert.isEqual(Version("1.2.3.4"), "1.2.3.4")
#

@TestCase()
def test_case_regular_5(ctx):
	Assert.isEqual(Version("0"), "0")
#

@TestCase()
def test_case_regular_6(ctx):
	Assert.isEqual(Version("0.1"), "0.1")
#

@TestCase()
def test_case_regular_7(ctx):
	Assert.isEqual(Version("0.2019"), "0.2019")
#

@TestCase()
def test_case_regular_8(ctx):
	Assert.isEqual(Version("0.2019.03.02"), "0.2019.3.2")
#

@TestCase()
def test_case_with_epoch(ctx):
	v1 = Version("2:0.2019.03.02")
	Assert.isEqual(v1, Version("2:0.2019.3.2"))
	Assert.isEqual(v1, "2:0.2019.3.2")
#

@TestCase()
def test_case_epoch_comparison(ctx):
	Assert.isEqual(Version("0.2019.3.2"), "0:0.2019.3.2")
	Assert.isTrue(Version("0.2019.3.2") < "1:0.2019.3.2")
	Assert.isTrue(Version("1:0.2019.3.2") < "2:0.2019.3.2")
#

@TestCase()
def test_case_stripping_other(ctx):
	Assert.isEqual(Version("2:0.1.2-3ubuntu4"), "2:0.1.2")
#

@TestCase()
def test_case_stripping_other_1(ctx):
	v = Version("2:0.1.2-3ubuntu4")
	Assert.isEqual(v.epoch, 2)
	Assert.isEqual(v.numbers, [ 0, 1, 2 ])
	Assert.isEqual(v.extra, "3ubuntu4")
	Assert.isEqual(v, "2:0.1.2")
	Assert.isEqual(str(v), "2:0.1.2-3ubuntu4")
#

@TestCase()
def test_case_stripping_other_2(ctx):
	v = Version("2:0.1.2+3ubuntu4")
	Assert.isEqual(v.epoch, 2)
	Assert.isEqual(v.numbers, [ 0, 1, 2 ])
	Assert.isEqual(v.extra, "3ubuntu4")
	Assert.isEqual(v, "2:0.1.2")
	Assert.isEqual(str(v), "2:0.1.2-3ubuntu4")
#

@TestCase()
def test_case_stripping_other_3(ctx):
	v = Version("2:0.1.2~3ubuntu4")
	Assert.isEqual(v.epoch, 2)
	Assert.isEqual(v.numbers, [ 0, 1, 2 ])
	Assert.isEqual(v.extra, "3ubuntu4")
	Assert.isEqual(v, "2:0.1.2")
	Assert.isEqual(str(v), "2:0.1.2-3ubuntu4")
#

@TestCase()
def test_case_maven_snapshot(ctx):
	v = Version("1.2.3-SNAPSHOT")
	Assert.isEqual(v.epoch, 0)
	Assert.isEqual(v.numbers, [ 1, 2, 3 ])
	Assert.isEqual(v.extra, "SNAPSHOT")
	Assert.isEqual(v, "1.2.3")
	Assert.isEqual(str(v), "1.2.3-SNAPSHOT")
#

@TestCase()
def test_exotic_1(ctx):
	v = Version("1.2.3.foobar3")
	Assert.isEqual(v.epoch, 0)
	Assert.isEqual(v.numbers, [ 1, 2, 3 ])
	Assert.isEqual(v.extra, "foobar3")
	Assert.isEqual(v, "1.2.3")
	Assert.isEqual(str(v), "1.2.3-foobar3")
#

@TestCase()
def test_exotic_2(ctx):
	v = Version.parseFromStr("1.2.3.foobar3")
	Assert.isEqual(v.epoch, 0)
	Assert.isEqual(v.numbers, [ 1, 2, 3 ])
	Assert.isEqual(v.extra, "foobar3")
	Assert.isEqual(v, "1.2.3")
	Assert.isEqual(str(v), "1.2.3-foobar3")
#

@TestCase(
	RaisesException(Exception, "Failed to parse version string: \"1.2.3.foobar3\"")
)
def test_exotic_3(ctx):
	v = Version.parseFromStr("1.2.3.foobar3", bStrict=True)
	Assert.isEqual(v.epoch, 0)
	Assert.isEqual(v.numbers, [ 1, 2, 3 ])
	Assert.isEqual(v.extra, "foobar3")
	Assert.isEqual(v, "1.2.3")
	Assert.isEqual(str(v), "1.2.3-foobar3")
#


#
# Errors
#


# TODO


#
# Comparisons
#


@TestCase()
def test_case_comparison_1(ctx):
	Assert.isEqual(Version("0.1.2"), Version("0.1.2"))
#

@TestCase()
def test_case_comparison_2(ctx):
	Assert.isEqual(Version("0.1"), Version("0.1.0"))
#

@TestCase()
def test_case_comparison_3(ctx):
	Assert.isTrue(Version("0.1.1") > Version("0.1"))
#

@TestCase()
def test_case_comparison_4(ctx):
	Assert.isTrue(Version("2:0.1.2") > "1:1.2.3")
#

@TestCase()
def test_case_comparison_maven(ctx):
	Assert.isEqual(Version("1.2.3-SNAPSHOT"), Version("1.2.3"))
#



################################################################################################################################




testDriver = TestDriver()

results = testDriver.runTests([
	test_case_regular_0,
	test_case_regular_1,
	test_case_regular_2,
	test_case_regular_3,
	test_case_regular_4,
	test_case_regular_5,
	test_case_regular_6,
	test_case_regular_7,
	test_case_regular_8,
	test_case_with_epoch,
	test_case_stripping_other_1,
	test_case_stripping_other_2,
	test_case_stripping_other_3,
	test_case_maven_snapshot,

	test_exotic_1,
	test_exotic_2,
	test_exotic_3,

	test_case_comparison_1,
	test_case_comparison_2,
	test_case_comparison_3,
	test_case_comparison_4,
	test_case_comparison_maven,
])

#reporter = TestReporterHTML()
#reporter.report(results)
#reporter.report(results, webbrowserType="chromium")











