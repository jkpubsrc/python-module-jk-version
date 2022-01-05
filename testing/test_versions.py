#!/usr/bin/python3




from jk_version import *
from jk_testing import *




#
# Successes
#


@TestCase()
def test_case_regular_0(ctx):
	assert Version("0") == "0"
#

@TestCase()
def test_case_regular_1(ctx):
	assert Version("1") == "1"
#

@TestCase()
def test_case_regular_2(ctx):
	assert Version("1.2") == "1.2"
#

@TestCase()
def test_case_regular_3(ctx):
	assert Version("1.2.3") == "1.2.3"
#

@TestCase()
def test_case_regular_4(ctx):
	assert Version("1.2.3.4") == "1.2.3.4"
#

@TestCase()
def test_case_regular_5(ctx):
	assert Version("0") == "0"
#

@TestCase()
def test_case_regular_6(ctx):
	assert Version("0.1") == "0.1"
#

@TestCase()
def test_case_regular_7(ctx):
	assert Version("0.2019") == "0.2019"
#

@TestCase()
def test_case_regular_8(ctx):
	assert Version("0.2019.03.02") == "0.2019.3.2"
#

@TestCase()
def test_case_with_epoch(ctx):
	v1 = Version("2:0.2019.03.02")
	assert v1 == Version("2:0.2019.3.2")
	assert v1 == "2:0.2019.3.2"
#

@TestCase()
def test_case_epoch_comparison(ctx):
	assert Version("0.2019.3.2") == "0:0.2019.3.2"
	assert Version("0.2019.3.2") < "1:0.2019.3.2"
	assert Version("1:0.2019.3.2") < "2:0.2019.3.2"
#

@TestCase()
def test_case_stripping_other(ctx):
	assert Version("2:0.1.2-3ubuntu4") == "2:0.1.2"
#

@TestCase()
def test_case_stripping_other_1(ctx):
	v = Version("2:0.1.2-3ubuntu4")
	assert v.epoch == 2
	assert v.numbers == [ 0, 1, 2 ]
	assert v.extra == "3ubuntu4"
	assert v == "2:0.1.2"
	assert str(v) == "2:0.1.2-3ubuntu4"
#

@TestCase()
def test_case_stripping_other_2(ctx):
	v = Version("2:0.1.2+3ubuntu4")
	assert v.epoch == 2
	assert v.numbers == [ 0, 1, 2 ]
	assert v.extra == "3ubuntu4"
	assert v == "2:0.1.2"
	assert str(v) == "2:0.1.2-3ubuntu4"
#

@TestCase()
def test_case_stripping_other_3(ctx):
	v = Version("2:0.1.2~3ubuntu4")
	assert v.epoch == 2
	assert v.numbers == [ 0, 1, 2 ]
	assert v.extra == "3ubuntu4"
	assert v == "2:0.1.2"
	assert str(v) == "2:0.1.2-3ubuntu4"
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
	assert Version("0.1.2") == Version("0.1.2")
#

@TestCase()
def test_case_comparison_2(ctx):
	assert Version("0.1") == Version("0.1.0")
#

@TestCase()
def test_case_comparison_3(ctx):
	assert Version("0.1.1") > Version("0.1")
#

@TestCase()
def test_case_comparison_4(ctx):
	assert Version("2:0.1.2") > "1:1.2.3"
#



################################################################################################################################




testDriver = TestDriver()

results = testDriver.runTests([
	(test_case_regular_1, True),
	(test_case_regular_2, True),
	(test_case_regular_3, True),
	(test_case_regular_4, True),
	(test_case_regular_5, True),
	(test_case_regular_6, True),
	(test_case_regular_7, True),
	(test_case_regular_8, True),
	(test_case_with_epoch, True),
	(test_case_stripping_other_1, True),
	(test_case_stripping_other_2, True),
	(test_case_stripping_other_3, True),

	(test_case_comparison_1, True),
	(test_case_comparison_2, True),
	(test_case_comparison_3, True),
	(test_case_comparison_4, True),
])

reporter = TestReporterHTML()
reporter.report(results, webbrowserType="chromium")











