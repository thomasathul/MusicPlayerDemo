import problem_set_1
import problem_set_2
import problem_set_3
import problem_set_4


def test_biggest():
    assert problem_set_1.biggest(1, 2, 3, 4) == 4


def test_armstrong():
    assert problem_set_1.armstrong(153) == "True"
    assert problem_set_1.armstrong(200) == "False"


def test_gcd():
    assert problem_set_1.gcd(2, 3) == 1
    assert problem_set_1.gcd(10, 5) == 5


def test_lcm():
    assert problem_set_1.lcm(2, 3) == 6
    assert problem_set_1.lcm(10, 20) == 20


def test_triangle():
    assert problem_set_1.triangle(5, 5, 5) == "equilateral"
    assert problem_set_1.triangle(6, 3, 6) == "isoceles"
    assert problem_set_1.triangle(3, 4, 5) == "right-angled"
    assert problem_set_1.triangle(7, 3, 5) == "scalene"


def test_vowelconsonant():
    assert problem_set_1.vowel_consonant('a') == "Vowel"
    assert problem_set_1.vowel_consonant('b') == "Consonant"


def test_leapyear():
    assert problem_set_1.leap_year(2020) == "True"
    assert problem_set_1.leap_year(2019) == "False"


def test_quadrant():
    assert problem_set_1.quadrant(1, 6) == "Q1"
    assert problem_set_1.quadrant(-1, 4) == "Q2"
    assert problem_set_1.quadrant(-5, -7) == "Q3"
    assert problem_set_1.quadrant(6, -7) == "Q4"


def test_digitalroot():
    assert problem_set_2.digital_root(7532) == 8
    assert problem_set_2.digital_root(4563) == 9


def test_factorial():
    assert problem_set_2.factorial(5) == 120
    assert problem_set_2.factorial(0) == 1


def test_sumoffactors():
    assert problem_set_2.sum_of_factors(15) == 9
    assert problem_set_2.sum_of_factors(21) == 11


def test_countprime():
    assert problem_set_2.count_prime_numbers(10) == 4
    assert problem_set_2.count_prime_numbers(30) == 10


def test_trianglenum():
    assert problem_set_2.triangle_number(21) == 1771
    assert problem_set_2.triangle_number(1) == 1


def test_maximumnum():
    assert problem_set_2.maximum_num(2112) == 212
    assert problem_set_2.maximum_num(2634) == 634


def test_combinations():
    assert problem_set_2.combinations(5, 2) == 10
    assert problem_set_2.combinations(10, 4) == 210


def test_oddman():
    assert problem_set_3.odd_man([2, 4, 2, 2, 2]) == 4
    assert problem_set_3.odd_man([6, 3, 3, 3, 3]) == 6


def test_closemean():
    assert problem_set_3.close_mean([5, 7, 3, 5, 7]) == 5
    assert problem_set_3.close_mean([10, 40, 20, 4]) == 20


def test_avgspeed():
    assert problem_set_3.average_speed([4, 6, 7, 9], 3) == 2
    assert problem_set_3.average_speed([2, 4, 7, 9], 2) == 2


def test_missingnum():
    assert problem_set_3.missing_number([3, 4, 5, 7, 1], [3, 4, 5, 7]) == {1}


def test_lownum():
    assert problem_set_3.diff_low_num([2, 4, 5, 7, 3]) == 1
    assert problem_set_3.diff_low_num([4, 6, 8, 10]) == 2


def test_smallthanmean():
    assert problem_set_3.small_than_mean([4, 10, 8, 2, 5]) == 2
    assert problem_set_3.small_than_mean([3, 5, 7, 16, 2]) == 3


def test_ipaddress():
    assert problem_set_4.ipadd("199.189.12.1") == 3351055361
    assert problem_set_4.ipadd("198.278.15.1") == 3340111617


def test_isogram():
    assert problem_set_4.isogram("hello") == "It is not an isogram"
    assert problem_set_4.isogram("Machine") == "It is an isogram"


def test_mexicanwave():
    assert problem_set_4.mexican_wave(
        "hello") == ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
    assert problem_set_4.mexican_wave(
        "okayy") == ['Okayy', 'oKayy', 'okAyy', 'okaYy', 'okayY']


def test_largenum():
    assert problem_set_4.large_num("4352") == 452
    assert problem_set_4.large_num("4653") == 653


def test_shuffle():
    assert problem_set_4.shuffle("okay") == "yoka"
    assert problem_set_4.shuffle("hello") == "ollhe"


def test_wordfreq():
    assert problem_set_4.word_freq("gdsdafsddfsa") == 2


def test_rgbhex():
    assert problem_set_4.rgb_hex((225, 225, 225)) == "0xe1e1e1"
    assert problem_set_4.rgb_hex((45, 32, 63)) == "0x2d203f"


def test_accumulate():
    assert problem_set_4.accumulate("hello") == "h-ee-lll-llll-ooooo"
    assert problem_set_4.accumulate("things") == "t-hh-iii-nnnn-ggggg-ssssss"
