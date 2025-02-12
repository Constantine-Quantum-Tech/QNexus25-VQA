from IPython.display import Math
import numpy as np
INDENT_SPACES = 3
def display_matrix(matrix):
  def indent(num_indent=1):
      """
      Number of spaces for indentation
      """
      return num_indent * INDENT_SPACES * " "

  def matrix2latex(matrix):
      """
      Convert a NumPy array to LaTeX code as a matrix
      """
      left_latex = r"\left(" + "\n" + indent(1) + r"\begin{array}"
      right_latex = indent(1) + r"\end{array}" + "\n" + r"\right)"
      m_cols = matrix.shape[1]
      array_cols = "{" + "r" * m_cols + "}\n"
      elements_latex = ""
      for row in matrix:
          elements_latex = \
            elements_latex + indent(2) + " & ".join([str(x) for x in row]) + \
              r" \\ " + "\n"
      latex = left_latex + array_cols + elements_latex + right_latex
      return f"$$\n{latex}\n$$"
  return display(Math(matrix2latex(matrix.round(2))))