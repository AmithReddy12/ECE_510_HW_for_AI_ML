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
      "id": "29fc1c09-f365-4625-bb57-649adab8afc9",
      "cell_type": "code",
      "source": "def differential_equation_solver(f, y0, t0, t_end, h):\n    t = t0\n    y = y0\n    while t < t_end:\n        k1 = h * f(t, y)\n        k2 = h * f(t + h/2, y + k1/2)\n        k3 = h * f(t + h/2, y + k2/2)\n        k4 = h * f(t + h, y + k3)\n        y += (k1 + 2*k2 + 2*k3 + k4) / 6\n        t += h\n    return y\n\ndef dy_dt(t, y):\n    return -2 * y + 1\n\nif __name__ == \"__main__\":\n    result = differential_equation_solver(dy_dt, 1, 0, 5, 0.01)\n    print(f\"Final result using RK4: {result}\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Final result using RK4: 0.5000222504757629\n"
        }
      ],
      "execution_count": 5
    },
    {
      "id": "a79927db-c464-4412-a61e-ecde7a2b5115",
      "cell_type": "code",
      "source": "import py_compile\n\npy_compile.compile(\"differential_equation_solver.py\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 6,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'__pycache__/differential_equation_solver.cpython-312.pyc'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 6
    },
    {
      "id": "73d7d754-3d2f-4c75-bc0d-cfe1cc6f03d2",
      "cell_type": "code",
      "source": "import dis\n\n# Already-defined function (from earlier cell)\ndis.dis(differential_equation_solver)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "  1           0 RESUME                   0\n\n  2           2 LOAD_FAST                2 (t0)\n              4 STORE_FAST               5 (t)\n\n  3           6 LOAD_FAST                1 (y0)\n              8 STORE_FAST               6 (y)\n\n  4          10 LOAD_FAST                5 (t)\n             12 LOAD_FAST                3 (t_end)\n             14 COMPARE_OP               2 (<)\n             18 POP_JUMP_IF_FALSE      112 (to 244)\n\n  5     >>   20 LOAD_FAST                4 (h)\n             22 PUSH_NULL\n             24 LOAD_FAST                0 (f)\n             26 LOAD_FAST                5 (t)\n             28 LOAD_FAST                6 (y)\n             30 CALL                     2\n             38 BINARY_OP                5 (*)\n             42 STORE_FAST               7 (k1)\n\n  6          44 LOAD_FAST                4 (h)\n             46 PUSH_NULL\n             48 LOAD_FAST                0 (f)\n             50 LOAD_FAST                5 (t)\n             52 LOAD_FAST                4 (h)\n             54 LOAD_CONST               1 (2)\n             56 BINARY_OP               11 (/)\n             60 BINARY_OP                0 (+)\n             64 LOAD_FAST                6 (y)\n             66 LOAD_FAST                7 (k1)\n             68 LOAD_CONST               1 (2)\n             70 BINARY_OP               11 (/)\n             74 BINARY_OP                0 (+)\n             78 CALL                     2\n             86 BINARY_OP                5 (*)\n             90 STORE_FAST               8 (k2)\n\n  7          92 LOAD_FAST                4 (h)\n             94 PUSH_NULL\n             96 LOAD_FAST                0 (f)\n             98 LOAD_FAST                5 (t)\n            100 LOAD_FAST                4 (h)\n            102 LOAD_CONST               1 (2)\n            104 BINARY_OP               11 (/)\n            108 BINARY_OP                0 (+)\n            112 LOAD_FAST                6 (y)\n            114 LOAD_FAST                8 (k2)\n            116 LOAD_CONST               1 (2)\n            118 BINARY_OP               11 (/)\n            122 BINARY_OP                0 (+)\n            126 CALL                     2\n            134 BINARY_OP                5 (*)\n            138 STORE_FAST               9 (k3)\n\n  8         140 LOAD_FAST                4 (h)\n            142 PUSH_NULL\n            144 LOAD_FAST                0 (f)\n            146 LOAD_FAST                5 (t)\n            148 LOAD_FAST                4 (h)\n            150 BINARY_OP                0 (+)\n            154 LOAD_FAST                6 (y)\n            156 LOAD_FAST                9 (k3)\n            158 BINARY_OP                0 (+)\n            162 CALL                     2\n            170 BINARY_OP                5 (*)\n            174 STORE_FAST              10 (k4)\n\n  9         176 LOAD_FAST                6 (y)\n            178 LOAD_FAST                7 (k1)\n            180 LOAD_CONST               1 (2)\n            182 LOAD_FAST                8 (k2)\n            184 BINARY_OP                5 (*)\n            188 BINARY_OP                0 (+)\n            192 LOAD_CONST               1 (2)\n            194 LOAD_FAST                9 (k3)\n            196 BINARY_OP                5 (*)\n            200 BINARY_OP                0 (+)\n            204 LOAD_FAST               10 (k4)\n            206 BINARY_OP                0 (+)\n            210 LOAD_CONST               2 (6)\n            212 BINARY_OP               11 (/)\n            216 BINARY_OP               13 (+=)\n            220 STORE_FAST               6 (y)\n\n 10         222 LOAD_FAST                5 (t)\n            224 LOAD_FAST                4 (h)\n            226 BINARY_OP               13 (+=)\n            230 STORE_FAST               5 (t)\n\n  4         232 LOAD_FAST                5 (t)\n            234 LOAD_FAST                3 (t_end)\n            236 COMPARE_OP               2 (<)\n            240 POP_JUMP_IF_FALSE        1 (to 244)\n            242 JUMP_BACKWARD          112 (to 20)\n\n 11     >>  244 LOAD_FAST                6 (y)\n            246 RETURN_VALUE\n"
        }
      ],
      "execution_count": 7
    },
    {
      "id": "269b0d7c-c9d9-4b33-bb5a-b9b905f269ef",
      "cell_type": "code",
      "source": "from collections import Counter\n\ndef count_instructions(func):\n    instructions = dis.get_instructions(func)\n    return Counter(instr.opname for instr in instructions)\n\ninstruction_counts = count_instructions(differential_equation_solver)\ninstruction_counts",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 8,
          "output_type": "execute_result",
          "data": {
            "text/plain": "Counter({'LOAD_FAST': 36,\n         'BINARY_OP': 22,\n         'STORE_FAST': 8,\n         'LOAD_CONST': 7,\n         'PUSH_NULL': 4,\n         'CALL': 4,\n         'COMPARE_OP': 2,\n         'POP_JUMP_IF_FALSE': 2,\n         'RESUME': 1,\n         'JUMP_BACKWARD': 1,\n         'RETURN_VALUE': 1})"
          },
          "metadata": {}
        }
      ],
      "execution_count": 8
    },
    {
      "id": "5e56a721-2a3b-4a81-a304-284980776dbd",
      "cell_type": "code",
      "source": "# Define arithmetic operators to count\narithmetic_operators = ['+', '-', '*', '/', '%']\n\n# Read the workload.py file\nwith open(\"differential_equation_solver.py\", \"r\", encoding=\"utf-8\") as f:\n    code = f.read()\n\n# Count occurrences of each arithmetic operator\narithmetic_counts = {op: code.count(op) for op in arithmetic_operators}\ntotal_arithmetic_instructions = sum(arithmetic_counts.values())\n\n# Print results\nprint(\"Arithmetic Operation Counts:\", arithmetic_counts)\nprint(\"Total Arithmetic Instructions:\", total_arithmetic_instructions)",
      "metadata": {
        "trusted": true,
        "scrolled": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Arithmetic Operation Counts: {'+': 24, '-': 30, '*': 14, '/': 15, '%': 1}\nTotal Arithmetic Instructions: 84\n"
        }
      ],
      "execution_count": 11
    },
    {
      "id": "52b68c59-1c9a-45c6-900f-e131d29811b7",
      "cell_type": "code",
      "source": "import cProfile\nimport pstats\nimport io\n\ndef profile_function(func, *args, **kwargs):\n    pr = cProfile.Profile()\n    pr.enable()\n    \n    # Run the function\n    result = func(*args, **kwargs)\n    \n    pr.disable()\n    \n    # Print profile report\n    s = io.StringIO()\n    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')\n    ps.print_stats()\n    \n    print(s.getvalue())\n    return result  # in case you want to use the result",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 12
    },
    {
      "id": "f80b4478-1953-479b-9e6e-4df64bf1610d",
      "cell_type": "code",
      "source": "result = profile_function(differential_equation_solver, dy_dt, 1, 0, 5, 0.01)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "         2006 function calls in 0.005 seconds\n\n   Ordered by: cumulative time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.003    0.003    0.005    0.005 <ipython-input-5-0ef8330e83d7>:1(differential_equation_solver)\n     2004    0.002    0.000    0.002    0.000 <ipython-input-5-0ef8330e83d7>:13(dy_dt)\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n\n\n\n"
        }
      ],
      "execution_count": 13
    },
    {
      "id": "c23169d4-6c20-446d-9ba9-592099da033d",
      "cell_type": "code",
      "source": "import ast\n\nclass ParallelismAnalyzer(ast.NodeVisitor):\n    def __init__(self):\n        self.loops = 0\n        self.assignments = 0\n        self.function_calls = 0\n        self.dependencies = set()\n        self.writes = set()\n        self.reads = set()\n\n    def visit_FunctionDef(self, node):\n        self.current_vars = set()\n        self.generic_visit(node)\n\n    def visit_For(self, node):\n        self.loops += 1\n        self.generic_visit(node)\n\n    def visit_While(self, node):\n        self.loops += 1\n        self.generic_visit(node)\n\n    def visit_Assign(self, node):\n        self.assignments += 1\n        for target in node.targets:\n            if isinstance(target, ast.Name):\n                self.writes.add(target.id)\n        self.generic_visit(node)\n\n    def visit_Name(self, node):\n        if isinstance(node.ctx, ast.Load):\n            self.reads.add(node.id)\n\n    def visit_Call(self, node):\n        self.function_calls += 1\n        self.generic_visit(node)\n\n    def analyze(self, code):\n        tree = ast.parse(code)\n        self.visit(tree)\n        self.dependencies = self.reads & self.writes\n        return {\n            'loops': self.loops,\n            'assignments': self.assignments,\n            'function_calls': self.function_calls,\n            'data_dependencies': list(self.dependencies),\n            'parallelizable': self.loops > 0 and not self.dependencies\n        }",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 14
    },
    {
      "id": "410f1fc1-dbf0-4098-92da-1bf37e12ac5c",
      "cell_type": "code",
      "source": "differential_equation_solver = '''\ndef differential_equation_solver(f, y0, t0, t_end, h):\n    t = t0\n    y = y0\n    while t < t_end:\n        k1 = h * f(t, y)\n        k2 = h * f(t + h/2, y + k1/2)\n        k3 = h * f(t + h/2, y + k2/2)\n        k4 = h * f(t + h, y + k3)\n        y += (k1 + 2*k2 + 2*k3 + k4) / 6\n        t += h\n    return y\n'''",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 15
    },
    {
      "id": "e2262f87-22d9-4748-88c9-2d1b87f73c1d",
      "cell_type": "code",
      "source": "analyzer = ParallelismAnalyzer()\n\ndifferential_equation_solver_result = analyzer.analyze(differential_equation_solver)\nprint(\"differential_equation_solver:\", differential_equation_solver_result)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "differential_equation_solver: {'loops': 1, 'assignments': 6, 'function_calls': 4, 'data_dependencies': ['y', 't', 'k4', 'k2', 'k3', 'k1'], 'parallelizable': False}\n"
        }
      ],
      "execution_count": 17
    },
    {
      "id": "4b24e59d-c6cc-4c47-81c0-b7df6fb0f2b7",
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