| Test Case Number | Input                                           | Expected Output | Reasoning                                              |
|------------------|-------------------------------------------------|-----------------|--------------------------------------------------------|
| 1                | 2, [1, 2]                                       | 0               | No identical elements.                                 |
| 2                | 3, [4, 4, 5]                                    | 1               | One pair with identical elements (4, 4).               |
| 3                | 4, [7, 7, 7, 7]                                 | 6               | All elements are identical, 6 pairs can be formed.     |
| 4                | 5, [1, 2, 3, 4, 5]                              | 0               | All elements are distinct. No pairs can be formed.     |
| 5                | 10, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]              | 5               | Multiple identical pairs exist for each unique element.|
| 6                | 5, [1000000000, 1000000000, 999999999, 999999999, 999999999] | 4               | Two sets of identical elements.                        |
| 7                | 3 test cases: [2, [3, 3]], [4, [1, 2, 3, 4]], [3, [5, 5, 5]] | 1, 0, 3         | First test case has 1 pair, second has none, third has 3.|
