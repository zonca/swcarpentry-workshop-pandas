# Create a python script

    import sys
    import analyze_mosquito_data_lib as mosquito_lib
    import pandas as pd


    input_argument = sys.argv[1]
    data = pd.read_csv(input_argument)
    data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])
    figure_filename = input_argument.replace(".csv", "_fitting_plot.pdf")
    parameters = analyze(data, save_figure_as="pdf")
    parameters_filename = input_argument.replace(".csv", "_fitting_coefficients.csv")
    parameters.to_csv(parameters_filename)
