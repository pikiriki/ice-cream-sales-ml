# Ice-Cream Sales from Temperature

A beginner machine-learning project that uses linear regression
to estimate ice-cream sales from temperature.

The program runs in Terminal and displays one chart.

## What the program does

1. Loads the supplied CSV.
2. Splits observations into training and test groups.
3. Fits linear regression using only training observations.
4. Evaluates the model against a simple baseline.
5. Accepts a temperature typed by the user.
6. Prints estimated sales.
7. Displays training observations, test observations, and the fitted line.

## Dataset

`sales.csv` contains 40 synthetic observations.

Each row represents one fictional day:

- `temperature_c`: temperature in degrees Celsius.
- `ice_creams_sold`: number of ice creams sold.

Temperatures range from 11°C to 36°C.

These are invented learning examples, not real business records.
Rows are treated as independent examples, not a time series.

## Files

- `main.py`: complete ML program.
- `sales.csv`: fixed synthetic dataset.
- `mae_demo.py`: small worked example of mean absolute error.
- `requirements.txt`: recorded package versions.
- `.gitignore`: excludes the Python environment and generated clutter.

## Setup on macOS

Python 3 and Git must already be available.

Open Terminal inside the project folder.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the recorded dependencies:

```bash
python -m pip install -r requirements.txt
```

The recorded package versions may require a compatible Python version.

## Run

From the project folder, with the environment activated:

```bash
python main.py
```

At the prompt, enter a plain number such as `26` or `26.5`.
Do not include `°C`.

The program prints the prediction and opens a chart.
Close the chart window to let the program finish.

To run the separate MAE example:

```bash
python mae_demo.py
```

## How the model works

The model learns:

Predicted sales = slope × temperature + intercept

Fitting chooses the slope and intercept from training examples.
Prediction applies those learned values to an input temperature.

The program trains again whenever it runs.

## Evaluation

The split uses:

- 80% training data: 32 observations.
- 20% test data: 8 observations.
- Fixed random seed: 42.

The baseline predicts the mean training sales, 95, for every test example.

Both approaches are evaluated on the same test observations using
mean absolute error (MAE).

Expected results for the supplied dataset and split:

| Approach | Test MAE |
|---|---:|
| Linear regression | Approximately 6.72 |
| Training-average baseline | 22.625 |

The model has smaller average errors than this baseline on this split.

MAE is measured in ice creams sold. Lower is better when comparing
predictions on the same examples.

Evaluation uses raw predictions. Only the displayed results table
is rounded.

## Limitations

- Synthetic data does not establish real-world forecasting accuracy.
- Temperature alone cannot explain actual shop sales.
- Eight test observations provide limited evaluation evidence.
- Predictions outside the observed temperature range may be unreliable.
- Predictions can contain decimals or even implausible values.
  The program does not clip them.
- The input must be numeric; invalid text currently produces an error.
- A convincing chart does not replace evaluation.

## What I learned

- How a CSV becomes a pandas DataFrame.
- How inputs differ from targets.
- Why training and test examples are separated.
- How fitting differs from prediction.
- What slope and intercept control.
- How to calculate and interpret MAE.
- Why a model needs comparison with a baseline.
- How to accept numeric input and display a chart.
- How to use a virtual environment and record dependencies.
- How to track meaningful changes with Git.

These examples taught the model a relationship. I tested that
relationship on examples it did not learn from, compared it with
a simple guess, and used it to predict sales for a new temperature.