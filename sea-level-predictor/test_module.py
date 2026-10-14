import unittest
import sea_level_predictor
import matplotlib as mpl
import numpy as np


# the test case
class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")

    def test_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")

    def test_plot_data_points(self):
        actual = self.ax.get_children()[0].get_offsets().data.tolist()
        expected_length = 134  # Number of data points in the EPA dataset
        self.assertEqual(len(actual), expected_length, f"Expected {expected_length} data points in scatter plot")

    def test_plot_lines(self):
        # There should be 2 lines (best fit lines)
        lines = self.ax.get_lines()
        self.assertEqual(len(lines), 2, "Expected 2 best fit lines in the plot")

    def test_first_line_extends_to_2050(self):
        lines = self.ax.get_lines()
        first_line_xdata = lines[0].get_xdata()
        self.assertEqual(first_line_xdata.iloc[-1] if hasattr(first_line_xdata, 'iloc') else first_line_xdata[-1], 2050,
                         "Expected first best fit line to extend to year 2050")

    def test_second_line_starts_at_2000(self):
        lines = self.ax.get_lines()
        second_line_xdata = lines[1].get_xdata()
        self.assertEqual(second_line_xdata.iloc[0] if hasattr(second_line_xdata, 'iloc') else second_line_xdata[0], 2000,
                         "Expected second best fit line to start at year 2000")


if __name__ == "__main__":
    unittest.main()
