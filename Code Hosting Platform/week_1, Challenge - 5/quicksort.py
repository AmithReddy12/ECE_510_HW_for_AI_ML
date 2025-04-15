{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "76d61ad0-6499-4b8c-ac90-48dc3bdf06d3",
      "cell_type": "code",
      "source": "# quicksort.py\ndef quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    less = [x for x in arr[1:] if x <= pivot]\n    greater = [x for x in arr[1:] if x > pivot]\n    return quicksort(less) + [pivot] + quicksort(greater)\n\nif __name__ == \"__main__\":\n    print(quicksort([10, 7, 8, 9, 1, 5]))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "[1, 5, 7, 8, 9, 10]\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "500cec80-de3a-4fa1-ac5b-43443b1416ee",
      "cell_type": "code",
      "source": "import py_compile\n\npy_compile.compile(\"quicksort.py\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 2,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'__pycache__/quicksort.cpython-312.pyc'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 2
    },
    {
      "id": "a46c7a5b-95ba-475c-9c1f-35ccc3e1927d",
      "cell_type": "code",
      "source": "import dis\n\n# Already-defined function (from earlier cell)\ndis.dis(quicksort)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "  2           0 RESUME                   0\n\n  3           2 LOAD_GLOBAL              1 (NULL + len)\n             12 LOAD_FAST                0 (arr)\n             14 CALL                     1\n             22 LOAD_CONST               1 (1)\n             24 COMPARE_OP              26 (<=)\n             28 POP_JUMP_IF_FALSE        2 (to 34)\n\n  4          30 LOAD_FAST                0 (arr)\n             32 RETURN_VALUE\n\n  5     >>   34 LOAD_FAST                0 (arr)\n             36 LOAD_CONST               2 (0)\n             38 BINARY_SUBSCR\n             42 STORE_FAST               1 (pivot)\n\n  6          44 LOAD_FAST                0 (arr)\n             46 LOAD_CONST               1 (1)\n             48 LOAD_CONST               0 (None)\n             50 BINARY_SLICE\n             52 GET_ITER\n             54 LOAD_FAST_AND_CLEAR      2 (x)\n             56 SWAP                     2\n             58 BUILD_LIST               0\n             60 SWAP                     2\n        >>   62 FOR_ITER                10 (to 86)\n             66 STORE_FAST               2 (x)\n             68 LOAD_FAST                2 (x)\n             70 LOAD_FAST                1 (pivot)\n             72 COMPARE_OP              26 (<=)\n             76 POP_JUMP_IF_TRUE         1 (to 80)\n             78 JUMP_BACKWARD            9 (to 62)\n        >>   80 LOAD_FAST                2 (x)\n             82 LIST_APPEND              2\n             84 JUMP_BACKWARD           12 (to 62)\n        >>   86 END_FOR\n             88 STORE_FAST               3 (less)\n             90 STORE_FAST               2 (x)\n\n  7          92 LOAD_FAST                0 (arr)\n             94 LOAD_CONST               1 (1)\n             96 LOAD_CONST               0 (None)\n             98 BINARY_SLICE\n            100 GET_ITER\n            102 LOAD_FAST_AND_CLEAR      2 (x)\n            104 SWAP                     2\n            106 BUILD_LIST               0\n            108 SWAP                     2\n        >>  110 FOR_ITER                10 (to 134)\n            114 STORE_FAST               2 (x)\n            116 LOAD_FAST                2 (x)\n            118 LOAD_FAST                1 (pivot)\n            120 COMPARE_OP              68 (>)\n            124 POP_JUMP_IF_TRUE         1 (to 128)\n            126 JUMP_BACKWARD            9 (to 110)\n        >>  128 LOAD_FAST                2 (x)\n            130 LIST_APPEND              2\n            132 JUMP_BACKWARD           12 (to 110)\n        >>  134 END_FOR\n            136 STORE_FAST               4 (greater)\n            138 STORE_FAST               2 (x)\n\n  8         140 LOAD_GLOBAL              3 (NULL + quicksort)\n            150 LOAD_FAST                3 (less)\n            152 CALL                     1\n            160 LOAD_FAST                1 (pivot)\n            162 BUILD_LIST               1\n            164 BINARY_OP                0 (+)\n            168 LOAD_GLOBAL              3 (NULL + quicksort)\n            178 LOAD_FAST                4 (greater)\n            180 CALL                     1\n            188 BINARY_OP                0 (+)\n            192 RETURN_VALUE\n        >>  194 SWAP                     2\n            196 POP_TOP\n\n  6         198 SWAP                     2\n            200 STORE_FAST               2 (x)\n            202 RERAISE                  0\n        >>  204 SWAP                     2\n            206 POP_TOP\n\n  7         208 SWAP                     2\n            210 STORE_FAST               2 (x)\n            212 RERAISE                  0\nExceptionTable:\n  58 to 76 -> 194 [2]\n  80 to 86 -> 194 [2]\n  106 to 124 -> 204 [2]\n  128 to 134 -> 204 [2]\n"
        }
      ],
      "execution_count": 3
    },
    {
      "id": "2358bc22-c343-4863-867f-1f700907820a",
      "cell_type": "code",
      "source": "from collections import Counter\n\ndef count_instructions(func):\n    instructions = dis.get_instructions(func)\n    return Counter(instr.opname for instr in instructions)\n\ninstruction_counts = count_instructions(quicksort)\ninstruction_counts",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 4,
          "output_type": "execute_result",
          "data": {
            "text/plain": "Counter({'LOAD_FAST': 14,\n         'STORE_FAST': 9,\n         'SWAP': 8,\n         'LOAD_CONST': 6,\n         'JUMP_BACKWARD': 4,\n         'LOAD_GLOBAL': 3,\n         'CALL': 3,\n         'COMPARE_OP': 3,\n         'BUILD_LIST': 3,\n         'RETURN_VALUE': 2,\n         'BINARY_SLICE': 2,\n         'GET_ITER': 2,\n         'LOAD_FAST_AND_CLEAR': 2,\n         'FOR_ITER': 2,\n         'POP_JUMP_IF_TRUE': 2,\n         'LIST_APPEND': 2,\n         'END_FOR': 2,\n         'BINARY_OP': 2,\n         'POP_TOP': 2,\n         'RERAISE': 2,\n         'RESUME': 1,\n         'POP_JUMP_IF_FALSE': 1,\n         'BINARY_SUBSCR': 1})"
          },
          "metadata": {}
        }
      ],
      "execution_count": 4
    },
    {
      "id": "644202a9-3869-4722-a46f-d65d2c8d9d31",
      "cell_type": "code",
      "source": "# Define arithmetic operators to count\narithmetic_operators = ['+', '-', '*', '/', '%']\n\n# Read the workload.py file\nwith open(\"quicksort.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Count occurrences of each arithmetic operator\narithmetic_counts = {op: code.count(op) for op in arithmetic_operators}\ntotal_arithmetic_instructions = sum(arithmetic_counts.values())\n\n# Print results\nprint(\"Arithmetic Operation Counts:\", arithmetic_counts)\nprint(\"Total Arithmetic Instructions:\", total_arithmetic_instructions)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Arithmetic Operation Counts: {'+': 7, '-': 23, '*': 0, '/': 3, '%': 0}\nTotal Arithmetic Instructions: 33\n"
        }
      ],
      "execution_count": 5
    },
    {
      "id": "9027f294-50de-431e-9473-82c60bc80d74",
      "cell_type": "code",
      "source": "import cProfile\nimport pstats\nimport io\n\ndef profile_function(func, *args, **kwargs):\n    pr = cProfile.Profile()\n    pr.enable()\n    \n    # Run the function\n    result = func(*args, **kwargs)\n    \n    pr.disable()\n    \n    # Print profile report\n    s = io.StringIO()\n    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')\n    ps.print_stats()\n    \n    print(s.getvalue())\n    return result  # in case you want to use the result",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 8
    },
    {
      "id": "a7db3f52-521a-432f-b3a6-d4ea07d226ee",
      "cell_type": "code",
      "source": "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    lesser = [x for x in arr[1:] if x <= pivot]\n    greater = [x for x in arr[1:] if x > pivot]\n    return quicksort(lesser) + [pivot] + quicksort(greater)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 6
    },
    {
      "id": "f769608e-43cd-4db6-981c-3fe63fea93a2",
      "cell_type": "code",
      "source": "import random\n\nunsorted_list = [random.randint(0, 10000) for _ in range(1000)]\n\nprofile_function(quicksort, unsorted_list)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "         2695 function calls (1349 primitive calls) in 0.007 seconds\n\n   Ordered by: cumulative time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n   1347/1    0.007    0.000    0.007    0.007 <ipython-input-6-c299542877ee>:1(quicksort)\n     1347    0.000    0.000    0.000    0.000 {built-in method builtins.len}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n\n\n\n"
        },
        {
          "execution_count": 10,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[2,\n 7,\n 11,\n 17,\n 23,\n 26,\n 27,\n 27,\n 27,\n 44,\n 46,\n 48,\n 63,\n 78,\n 94,\n 110,\n 110,\n 112,\n 116,\n 137,\n 150,\n 165,\n 180,\n 181,\n 251,\n 287,\n 287,\n 300,\n 303,\n 343,\n 353,\n 356,\n 361,\n 394,\n 394,\n 395,\n 405,\n 416,\n 429,\n 451,\n 452,\n 469,\n 481,\n 495,\n 508,\n 508,\n 509,\n 521,\n 526,\n 526,\n 560,\n 564,\n 568,\n 568,\n 571,\n 579,\n 582,\n 582,\n 587,\n 599,\n 628,\n 640,\n 641,\n 641,\n 653,\n 668,\n 693,\n 711,\n 731,\n 732,\n 735,\n 753,\n 758,\n 762,\n 764,\n 778,\n 778,\n 785,\n 811,\n 815,\n 820,\n 851,\n 852,\n 869,\n 908,\n 910,\n 910,\n 925,\n 930,\n 963,\n 993,\n 996,\n 997,\n 1000,\n 1009,\n 1041,\n 1047,\n 1048,\n 1057,\n 1060,\n 1064,\n 1068,\n 1070,\n 1082,\n 1099,\n 1104,\n 1129,\n 1136,\n 1146,\n 1150,\n 1170,\n 1178,\n 1186,\n 1189,\n 1215,\n 1215,\n 1227,\n 1229,\n 1237,\n 1251,\n 1257,\n 1272,\n 1276,\n 1296,\n 1301,\n 1303,\n 1310,\n 1323,\n 1323,\n 1335,\n 1341,\n 1352,\n 1380,\n 1384,\n 1388,\n 1393,\n 1396,\n 1403,\n 1404,\n 1407,\n 1408,\n 1414,\n 1418,\n 1418,\n 1439,\n 1448,\n 1467,\n 1476,\n 1487,\n 1502,\n 1525,\n 1532,\n 1536,\n 1537,\n 1564,\n 1565,\n 1579,\n 1637,\n 1645,\n 1646,\n 1647,\n 1652,\n 1661,\n 1663,\n 1677,\n 1680,\n 1683,\n 1692,\n 1699,\n 1709,\n 1723,\n 1729,\n 1740,\n 1750,\n 1755,\n 1785,\n 1800,\n 1823,\n 1824,\n 1828,\n 1838,\n 1846,\n 1859,\n 1872,\n 1874,\n 1880,\n 1883,\n 1883,\n 1897,\n 1901,\n 1916,\n 1931,\n 1946,\n 1955,\n 1963,\n 1968,\n 1971,\n 1974,\n 1988,\n 2001,\n 2036,\n 2036,\n 2040,\n 2041,\n 2042,\n 2044,\n 2075,\n 2086,\n 2090,\n 2097,\n 2105,\n 2116,\n 2121,\n 2122,\n 2129,\n 2129,\n 2141,\n 2144,\n 2179,\n 2198,\n 2239,\n 2242,\n 2243,\n 2251,\n 2252,\n 2252,\n 2253,\n 2277,\n 2282,\n 2283,\n 2283,\n 2303,\n 2307,\n 2319,\n 2328,\n 2329,\n 2332,\n 2336,\n 2349,\n 2349,\n 2352,\n 2354,\n 2360,\n 2362,\n 2368,\n 2378,\n 2379,\n 2382,\n 2387,\n 2397,\n 2413,\n 2431,\n 2433,\n 2444,\n 2451,\n 2456,\n 2481,\n 2489,\n 2490,\n 2520,\n 2523,\n 2535,\n 2538,\n 2561,\n 2566,\n 2569,\n 2588,\n 2593,\n 2604,\n 2620,\n 2630,\n 2641,\n 2691,\n 2706,\n 2718,\n 2725,\n 2742,\n 2743,\n 2747,\n 2752,\n 2757,\n 2761,\n 2769,\n 2777,\n 2822,\n 2829,\n 2836,\n 2837,\n 2852,\n 2856,\n 2881,\n 2889,\n 2904,\n 2904,\n 2912,\n 2921,\n 2928,\n 2935,\n 2939,\n 2940,\n 2979,\n 3036,\n 3043,\n 3055,\n 3072,\n 3074,\n 3079,\n 3091,\n 3097,\n 3114,\n 3120,\n 3127,\n 3131,\n 3143,\n 3149,\n 3149,\n 3153,\n 3178,\n 3188,\n 3204,\n 3206,\n 3224,\n 3248,\n 3251,\n 3306,\n 3308,\n 3309,\n 3309,\n 3317,\n 3327,\n 3358,\n 3359,\n 3386,\n 3391,\n 3392,\n 3408,\n 3412,\n 3421,\n 3424,\n 3431,\n 3441,\n 3452,\n 3466,\n 3475,\n 3490,\n 3509,\n 3519,\n 3526,\n 3543,\n 3560,\n 3563,\n 3565,\n 3579,\n 3598,\n 3615,\n 3622,\n 3630,\n 3630,\n 3631,\n 3633,\n 3681,\n 3687,\n 3691,\n 3694,\n 3702,\n 3705,\n 3710,\n 3715,\n 3729,\n 3743,\n 3744,\n 3751,\n 3754,\n 3775,\n 3777,\n 3797,\n 3801,\n 3802,\n 3819,\n 3833,\n 3840,\n 3841,\n 3851,\n 3852,\n 3875,\n 3878,\n 3884,\n 3908,\n 3926,\n 3931,\n 3939,\n 3939,\n 3940,\n 3945,\n 3951,\n 3953,\n 3967,\n 3969,\n 3969,\n 3970,\n 3971,\n 3971,\n 4018,\n 4025,\n 4061,\n 4072,\n 4074,\n 4075,\n 4078,\n 4083,\n 4087,\n 4091,\n 4094,\n 4100,\n 4108,\n 4108,\n 4127,\n 4132,\n 4138,\n 4140,\n 4145,\n 4152,\n 4156,\n 4165,\n 4179,\n 4185,\n 4193,\n 4198,\n 4201,\n 4226,\n 4232,\n 4234,\n 4240,\n 4248,\n 4250,\n 4254,\n 4256,\n 4257,\n 4265,\n 4267,\n 4295,\n 4297,\n 4299,\n 4311,\n 4318,\n 4325,\n 4329,\n 4332,\n 4350,\n 4352,\n 4376,\n 4430,\n 4434,\n 4465,\n 4468,\n 4471,\n 4494,\n 4502,\n 4503,\n 4533,\n 4536,\n 4557,\n 4563,\n 4572,\n 4578,\n 4591,\n 4626,\n 4633,\n 4635,\n 4638,\n 4642,\n 4644,\n 4672,\n 4672,\n 4684,\n 4692,\n 4696,\n 4704,\n 4708,\n 4716,\n 4716,\n 4729,\n 4730,\n 4757,\n 4763,\n 4763,\n 4778,\n 4795,\n 4797,\n 4799,\n 4802,\n 4819,\n 4840,\n 4853,\n 4863,\n 4865,\n 4875,\n 4899,\n 4912,\n 4915,\n 4931,\n 4940,\n 4948,\n 4985,\n 5014,\n 5028,\n 5074,\n 5077,\n 5081,\n 5088,\n 5089,\n 5098,\n 5100,\n 5104,\n 5108,\n 5128,\n 5133,\n 5139,\n 5146,\n 5182,\n 5187,\n 5194,\n 5203,\n 5218,\n 5220,\n 5221,\n 5234,\n 5235,\n 5238,\n 5245,\n 5273,\n 5285,\n 5301,\n 5307,\n 5311,\n 5336,\n 5364,\n 5390,\n 5396,\n 5398,\n 5414,\n 5417,\n 5424,\n 5441,\n 5443,\n 5457,\n 5458,\n 5458,\n 5482,\n 5484,\n 5487,\n 5510,\n 5519,\n 5523,\n 5531,\n 5552,\n 5556,\n 5569,\n 5569,\n 5584,\n 5584,\n 5585,\n 5602,\n 5615,\n 5623,\n 5623,\n 5626,\n 5631,\n 5654,\n 5655,\n 5679,\n 5688,\n 5690,\n 5692,\n 5696,\n 5697,\n 5699,\n 5711,\n 5740,\n 5742,\n 5774,\n 5778,\n 5788,\n 5793,\n 5797,\n 5799,\n 5805,\n 5852,\n 5857,\n 5865,\n 5894,\n 5897,\n 5900,\n 5913,\n 5920,\n 5925,\n 5929,\n 5945,\n 5947,\n 5954,\n 5958,\n 5961,\n 5968,\n 5972,\n 5977,\n 5984,\n 5989,\n 6011,\n 6011,\n 6012,\n 6027,\n 6038,\n 6052,\n 6063,\n 6092,\n 6104,\n 6113,\n 6140,\n 6155,\n 6166,\n 6193,\n 6194,\n 6210,\n 6216,\n 6229,\n 6231,\n 6232,\n 6243,\n 6245,\n 6255,\n 6260,\n 6264,\n 6278,\n 6280,\n 6288,\n 6305,\n 6313,\n 6373,\n 6373,\n 6392,\n 6402,\n 6416,\n 6439,\n 6450,\n 6465,\n 6491,\n 6493,\n 6498,\n 6503,\n 6504,\n 6506,\n 6506,\n 6506,\n 6536,\n 6539,\n 6541,\n 6553,\n 6558,\n 6571,\n 6572,\n 6572,\n 6575,\n 6593,\n 6596,\n 6626,\n 6651,\n 6664,\n 6668,\n 6695,\n 6698,\n 6708,\n 6719,\n 6725,\n 6728,\n 6756,\n 6763,\n 6797,\n 6823,\n 6826,\n 6846,\n 6850,\n 6850,\n 6858,\n 6865,\n 6891,\n 6900,\n 6905,\n 6908,\n 6931,\n 6932,\n 6958,\n 6960,\n 6971,\n 6975,\n 6982,\n 7004,\n 7004,\n 7004,\n 7016,\n 7036,\n 7050,\n 7080,\n 7088,\n 7109,\n 7122,\n 7132,\n 7164,\n 7171,\n 7214,\n 7235,\n 7238,\n 7240,\n 7244,\n 7247,\n 7247,\n 7253,\n 7253,\n 7260,\n 7267,\n 7280,\n 7288,\n 7293,\n 7304,\n 7309,\n 7331,\n 7339,\n 7345,\n 7345,\n 7345,\n 7373,\n 7397,\n 7403,\n 7408,\n 7412,\n 7434,\n 7450,\n 7450,\n 7457,\n 7481,\n 7520,\n 7526,\n 7529,\n 7552,\n 7568,\n 7570,\n 7574,\n 7590,\n 7592,\n 7611,\n 7618,\n 7627,\n 7637,\n 7659,\n 7664,\n 7679,\n 7680,\n 7682,\n 7687,\n 7711,\n 7720,\n 7727,\n 7727,\n 7730,\n 7735,\n 7739,\n 7752,\n 7765,\n 7774,\n 7775,\n 7777,\n 7799,\n 7800,\n 7810,\n 7810,\n 7820,\n 7832,\n 7838,\n 7839,\n 7874,\n 7876,\n 7885,\n 7891,\n 7905,\n 7912,\n 7927,\n 7944,\n 7945,\n 7950,\n 7966,\n 7969,\n 7974,\n 7975,\n 7986,\n 7987,\n 7999,\n 8016,\n 8052,\n 8058,\n 8063,\n 8077,\n 8078,\n 8082,\n 8101,\n 8112,\n 8126,\n 8128,\n 8155,\n 8162,\n 8173,\n 8175,\n 8190,\n 8213,\n 8216,\n 8232,\n 8232,\n 8237,\n 8303,\n 8304,\n 8307,\n 8309,\n 8313,\n 8337,\n 8349,\n 8352,\n 8352,\n 8353,\n 8356,\n 8375,\n 8382,\n 8383,\n 8396,\n 8402,\n 8402,\n 8420,\n 8429,\n 8439,\n 8442,\n 8443,\n 8467,\n 8467,\n 8484,\n 8487,\n 8493,\n 8498,\n 8503,\n 8509,\n 8510,\n 8542,\n 8545,\n 8547,\n 8566,\n 8579,\n 8580,\n 8582,\n 8591,\n 8614,\n 8617,\n 8626,\n 8631,\n 8639,\n 8648,\n 8653,\n 8663,\n 8670,\n 8683,\n 8686,\n 8686,\n 8691,\n 8702,\n 8702,\n 8718,\n 8727,\n 8739,\n 8780,\n 8790,\n 8805,\n 8815,\n 8822,\n 8828,\n 8834,\n 8841,\n 8845,\n 8854,\n 8856,\n 8860,\n 8865,\n 8873,\n 8876,\n 8881,\n 8886,\n 8908,\n 8911,\n 8943,\n 8968,\n 8971,\n 8971,\n 8976,\n 8987,\n 8990,\n 9000,\n 9021,\n 9035,\n 9039,\n 9039,\n 9045,\n 9054,\n 9061,\n 9075,\n 9098,\n 9109,\n 9110,\n 9111,\n 9115,\n 9122,\n 9130,\n 9136,\n 9156,\n 9177,\n 9179,\n 9181,\n 9185,\n 9188,\n 9224,\n 9233,\n 9244,\n 9260,\n 9292,\n 9306,\n 9308,\n 9340,\n 9349,\n 9352,\n 9352,\n 9352,\n 9357,\n 9380,\n 9380,\n 9384,\n 9390,\n 9405,\n 9417,\n 9425,\n 9432,\n 9445,\n 9450,\n 9464,\n 9498,\n 9510,\n 9512,\n 9517,\n 9521,\n 9522,\n 9527,\n 9534,\n 9538,\n 9543,\n 9554,\n 9557,\n 9570,\n 9571,\n 9582,\n 9590,\n 9591,\n 9609,\n 9616,\n 9634,\n 9643,\n 9655,\n 9676,\n 9683,\n 9683,\n 9692,\n 9702,\n 9708,\n 9715,\n 9724,\n 9727,\n 9730,\n 9750,\n 9767,\n 9776,\n 9777,\n 9778,\n 9797,\n 9800,\n 9801,\n 9814,\n 9822,\n 9824,\n 9834,\n 9860,\n 9880,\n 9882,\n 9894,\n 9894,\n 9911,\n 9934,\n 9954,\n 9955,\n 9969]"
          },
          "metadata": {}
        }
      ],
      "execution_count": 10
    },
    {
      "id": "10838a35-04a6-413e-b105-194e5d0d81ee",
      "cell_type": "code",
      "source": "import ast\n\nclass ParallelismAnalyzer(ast.NodeVisitor):\n    def __init__(self):\n        self.loops = 0\n        self.assignments = 0\n        self.function_calls = 0\n        self.dependencies = set()\n        self.writes = set()\n        self.reads = set()\n\n    def visit_FunctionDef(self, node):\n        self.current_vars = set()\n        self.generic_visit(node)\n\n    def visit_For(self, node):\n        self.loops += 1\n        self.generic_visit(node)\n\n    def visit_While(self, node):\n        self.loops += 1\n        self.generic_visit(node)\n\n    def visit_Assign(self, node):\n        self.assignments += 1\n        for target in node.targets:\n            if isinstance(target, ast.Name):\n                self.writes.add(target.id)\n        self.generic_visit(node)\n\n    def visit_Name(self, node):\n        if isinstance(node.ctx, ast.Load):\n            self.reads.add(node.id)\n\n    def visit_Call(self, node):\n        self.function_calls += 1\n        self.generic_visit(node)\n\n    def analyze(self, code):\n        tree = ast.parse(code)\n        self.visit(tree)\n        self.dependencies = self.reads & self.writes\n        return {\n            'loops': self.loops,\n            'assignments': self.assignments,\n            'function_calls': self.function_calls,\n            'data_dependencies': list(self.dependencies),\n            'parallelizable': self.loops > 0 and not self.dependencies\n        }",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 11
    },
    {
      "id": "6e963954-fd48-4e11-854c-b9e97b7bdcd9",
      "cell_type": "code",
      "source": "matrix_mult_code = '''\ndef matrix_multiply(a, b):\n    result = [[0] * len(b[0]) for _ in range(len(a))]\n    for i in range(len(a)):\n        for j in range(len(b[0])):\n            for k in range(len(b)):\n                result[i][j] += a[i][k] * b[k][j]\n    return result\n'''",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 12
    },
    {
      "id": "e32ccc75-9c47-43a2-82ec-26cac7e9ddb5",
      "cell_type": "code",
      "source": "analyzer = ParallelismAnalyzer()\nmatrix_result = analyzer.analyze(matrix_mult_code)\nprint(\"Matrix Multiplication:\", matrix_result)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Matrix Multiplication: {'loops': 3, 'assignments': 1, 'function_calls': 9, 'data_dependencies': ['result'], 'parallelizable': False}\n"
        }
      ],
      "execution_count": 14
    },
    {
      "id": "0e1d6243-0395-4f27-9d8d-6680f3b8b03b",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}